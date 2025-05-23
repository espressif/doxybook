import os
import shutil
import tempfile
import time
import typing as t
from pathlib import (
    Path,
)

from jinja2 import (
    Environment,
    FileSystemLoader,
    PackageLoader,
    select_autoescape,
)

from doxybook.cache import (
    Cache,
)
from doxybook.doxygen import (
    Doxygen,
)
from doxybook.utils import (
    get_git_revision_hash,
)
from doxybook.xml_parser import (
    XmlParser,
)


def run(
    output: str,
    input_dir: str,
    target: str = 'single-markdown',
    debug: bool = False,
    link_prefix: str = '',
    template_dir: t.Optional[str] = None,
    template_lang: t.Optional[str] = 'c',
) -> bool:
    if output.endswith('.md'):
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        output_filepath = output
    else:
        os.makedirs(output, exist_ok=True)
        output_filepath = os.path.join(output, 'api.md')

    options = {'target': target, 'link_prefix': link_prefix}

    cache = Cache()
    parser = XmlParser(cache=cache, target=target)
    doxygen = Doxygen(input_dir, parser, cache, options=options)

    if debug:
        doxygen.print()

    if template_dir:
        loader = FileSystemLoader(template_dir)
    else:
        loader = PackageLoader('doxybook')
    template_lang = template_lang or 'c'

    env = Environment(loader=loader, autoescape=select_autoescape())
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as fw:
        template = env.get_template('api.jinja')
        common_args = {
            'files': doxygen.header_files.children,
            'groups': doxygen.groups.children,
            'file_template': env.get_template(f'{template_lang}/file.jinja'),
            'table_template': env.get_template('table.jinja'),
            'detail_template': env.get_template('detail.jinja'),
            'commit_sha': get_git_revision_hash(),
            'asctime': time.asctime(),
        }
        fw.write(template.render(**common_args))
        fw.flush()

        if os.path.isfile(output_filepath) and open(output_filepath).read() == open(fw.name).read():
            print(f'No changes detected in {output_filepath}')
            return False

        if not os.path.isfile(output_filepath):
            print(f'Generated single-markdown API reference: {output_filepath}')
            shutil.move(fw.name, output_filepath)
            return True

        print(f'Updated single-markdown API reference: {output_filepath}')
        shutil.move(fw.name, output_filepath)
        return True
