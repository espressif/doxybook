import argparse
import os
import shlex
import shutil
import subprocess
import sys
from shutil import (
    copytree,
)

from doxybook.constants import (
    DEFAULT_TEMPLATES_DIR,
    SUPPORTED_LANGS,
)
from doxybook.runner import (
    run,
)
from doxybook.utils import (
    error,
)


def parse_options():
    parser = argparse.ArgumentParser(description='Convert doxygen XML output into GitBook or Vuepress markdown output.')
    parser.add_argument(
        '-t',
        '--target',
        choices=['single-markdown'],
        help='markdown type',
        default='single-markdown',
    )
    parser.add_argument('-i', '--input', help='Path to doxygen generated xml folder')
    parser.add_argument('-o', '--output', help='Path to the destination folder')
    parser.add_argument(
        '-l',
        '--link-prefix',
        type=str,
        help='Adds a prefix to all links. '
        'You can use this to specify an absolute path if necessary. Docsify might need this. (default: "")',
        default='',
    )
    parser.add_argument(
        '-d', '--debug', type=bool, help='Debug the class hierarchy (default: false)', required=False, default=False
    )
    parser.add_argument(
        '--template-dir',
        help='Would use this template dir instead of the default one if set. '
        'Suggest use "doxygen generate-templates" at first to generate the defaults template dir, '
        'and then make your own changes on it.',
    )
    parser.add_argument(
        '--template-lang',
        choices=SUPPORTED_LANGS,
        default='c',
        help='specifies your project\'s main language.',
    )
    parser.add_argument(
        '--doxygen-bin',
        default='doxygen',
        help='doxygen binary path',
    )
    parser.add_argument(
        '--doxygen-extra-args', default='', help='extra argument passed into doxygen. should be doublequoted'
    )
    parser.add_argument(
        '--doxygen-config',
        default='Doxyfile',
        help='Path to the Doxygen config file',
    )

    action = parser.add_subparsers(dest='action')
    generate_templates = action.add_parser('generate-templates')
    generate_templates.add_argument(
        'output_dir', nargs='?', default=os.getcwd(), help=f'generate default template files. (Default: {os.getcwd()})'
    )

    args = parser.parse_args()

    return args


def _main() -> bool:
    args = parse_options()
    if args.action:
        if os.path.isfile(args.output_dir):
            raise Exception('The [OUTPUT_DIR] should be a directory')

        output_dir = os.path.join(args.output_dir, 'templates')
        if os.path.exists(output_dir):
            raise ValueError(f'{output_dir} folder already exists')

        copytree(DEFAULT_TEMPLATES_DIR, output_dir)
        print(f'Copied the default template files to {output_dir}')
        return

    doxygen_bin = shutil.which(args.doxygen_bin)
    if not doxygen_bin:
        raise RuntimeError(f'{args.doxygen_bin} not found in your PATH')

    doxygen_cmd = [doxygen_bin, args.doxygen_config]
    doxygen_cmd.extend(shlex.split(args.doxygen_extra_args))

    proc = subprocess.run(doxygen_cmd, capture_output=True)  # noqa: PLW1510
    if proc.returncode != 0:
        error(f'Failed to run command \"{" ".join(doxygen_cmd)}\":')
        error(proc.stderr.decode('utf-8'))
        sys.exit(1)

    if args.input is None or args.output is None:
        raise ValueError('-i/--input and -o/--output are required')

    return run(
        input_dir=args.input,
        output=args.output,
        target=args.target or 'single-markdown',
        debug=args.debug,
        link_prefix=args.link_prefix,
        template_dir=args.template_dir,
        template_lang=args.template_lang,
    )


def main_pre_commit():
    if _main():
        print('Please stage the modified file and run "git commit" again')
        sys.exit(1)


def main():
    _main()


if __name__ == '__main__':
    main()
