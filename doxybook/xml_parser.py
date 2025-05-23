from xml.etree.ElementTree import (
    Element,
)

from doxybook.cache import (
    Cache,
)
from doxybook.markdown import (
    Br,
    Code,
    Md,
    MdBlockQuote,
    MdBold,
    MdCodeBlock,
    MdHeader,
    MdImage,
    MdItalic,
    MdLink,
    MdList,
    MdParagraph,
    MdRenderer,
    MdTable,
    MdTableCell,
    MdTableRow,
    Text,
)
from doxybook.utils import (
    lookahead,
)

SIMPLE_SECTIONS = {
    'see': 'See also:',
    'note': 'Note:',
    'bug': 'Bug:',
    'warning': 'Warning:',
    'return': 'Returns:',
    'returns': 'Returns:',
    'param': 'Parameters:',
    'templateparam': 'Template parameters:',
    'retval': 'Return value:',
    'author': 'Author:',
    'authors': 'Authors:',
    'since': 'Since:',
    'pre': 'Precondition:',
    'remark': 'Remark:',
    'copyright': 'Copyright:',
    'post': 'Postcondition:',
    'rcs': 'Rcs:',
    'attention': 'Attention:',
    'invariant': 'Invariant:',
    'exception': 'Exception:',
    'date': 'Date:',
}


class XmlParser:
    def __init__(self, cache: Cache, target: str = 'gitbook'):
        self.target = target
        self.cache = cache

    def anchor(self, name: str) -> str:
        return '<a name=\"' + name + '\"></a>'

    def paras_as_str(self, p: Element, italic: bool = False, plain: bool = False) -> str:
        if plain:
            return self.plain_as_str(p)
        else:
            renderer = MdRenderer()
            for m in self.paras(p, italic=italic):
                m.render(renderer, '')
            return renderer.output.strip()

    def reference_as_str(self, p: Element) -> str:
        renderer = MdRenderer()
        refid = p.get('refid')
        if refid is not None:
            m = MdLink([MdBold([Text(p.text)])], refid)
            m.render(renderer, '')
            return renderer.output.strip()
        else:
            return p.text.strip()

    def programlisting_as_str(self, p: Element) -> str:
        renderer = MdRenderer()
        for m in self.programlisting(p):
            m.render(renderer, '')
        return renderer.output

    def plain_as_str(self, p: Element) -> str:
        return ' '.join(self.plain(p)).strip()

    def plain(self, p: Element) -> [str]:
        ret = []
        if p is None:
            return ret
        if p.text:
            ret.append(p.text.strip())
        for item in p:
            ret.extend(self.plain(item))
        if p.tail:
            ret.append(p.tail.strip())
        return ret

    def programlisting(self, p: Element) -> [Md]:
        ret = []
        # programlisting
        if p.tag == 'programlisting':
            got_lang = False
            code = MdCodeBlock([])
            for codeline in p.findall('codeline'):
                line = ''
                for highlight in codeline.findall('highlight'):
                    if (
                        not got_lang
                        and len(highlight) == 0
                        and highlight.text is not None
                        and highlight.text.startswith('{')
                        and highlight.text.endswith('}')
                    ):
                        lang = highlight.text[1:-1]
                        code.set_lang(lang)
                        got_lang = True
                        continue
                    else:
                        if highlight.text is not None:
                            line += highlight.text
                        for c in highlight:
                            if c.tag == 'sp':
                                line += ' '
                            if c.text:
                                line += c.text
                            if c.tail:
                                line += c.tail
                code.append(line)
            ret.append(Text('\n'))
            ret.append(code)
        return ret

    def paras(self, p: Element, italic: bool = False) -> [Md]:
        ret = []
        if p is None:
            return ret
        if p.text:
            if italic:
                ret.append(MdItalic([Text(p.text.strip())]))
                ret.append(Text(' '))
            else:
                ret.append(Text(p.text))
        for item in p:
            # para
            if item.tag == 'para':
                ret.append(MdParagraph(self.paras(item)))
                ret.append(Text('\n'))

            # image
            elif item.tag == 'image':
                url = item.get('name')
                ret.append(MdImage(url))

            # computeroutput
            elif item.tag == 'computeroutput':
                text = []
                if item.text:
                    text.append(item.text)
                for i in item:
                    text.extend(self.plain(i))
                ret.append(Code(' '.join(text)))

            # programlisting
            elif item.tag == 'programlisting':
                ret.extend(self.programlisting(item))

            # table
            elif item.tag == 'table':
                t = MdTable()
                for row in item.findall('row'):
                    r = MdTableRow([])
                    for cell in row.findall('entry'):
                        for para in cell.findall('para'):
                            r.append(MdTableCell(self.paras(para)))
                    t.append(r)
                ret.append(t)

            # blockquote
            elif item.tag == 'blockquote':
                b = MdBlockQuote([])
                for para in item.findall('para'):
                    b.extend(self.paras(para))
                ret.append(b)

            # heading
            elif item.tag == 'heading':
                ret.append(MdHeader(int(item.get('level')), self.paras(item)))

            # orderedlist
            elif item.tag in ('orderedlist', 'itemizedlist'):
                lst = MdList([])
                for listitem in item.findall('listitem'):
                    i = MdParagraph([])
                    for para in listitem.findall('para'):
                        i.extend(self.paras(para))
                    lst.append(i)
                ret.append(Text('\n'))  # in case there's no extra blank line before the list
                ret.append(lst)

            # Reference
            elif item.tag == 'ref':
                refid = item.get('refid')
                try:
                    ref = self.cache.get(refid)
                    if italic:
                        if item.text:
                            ret.append(MdLink([MdItalic([MdBold([Text(item.text)])])], ref.relative_link))
                        else:
                            ret.append(MdLink([MdItalic([MdBold([Text(ref.get_full_name())])])], ref.relative_link))
                    elif item.text:
                        ret.append(MdLink([MdBold([Text(item.text)])], ref.relative_link))
                    else:
                        ret.append(MdLink([MdBold([Text(ref.get_full_name())])], ref.relative_link))
                except Exception:
                    if item.text:
                        ret.append(Text(item.text))

            # sect1:
            elif item.tag == 'sect1':
                title = item.find('title').text
                ret.append(MdHeader(2, [Text(title)]))
                ret.extend(self.paras(item))

            # sect2:
            elif item.tag == 'sect2':
                title = item.find('title').text
                ret.append(MdHeader(3, [Text(title)]))
                ret.extend(self.paras(item))

            # sect3:
            elif item.tag == 'sect3':
                title = item.find('title').text
                ret.append(MdHeader(4, [Text(title)]))
                ret.extend(self.paras(item))

            # sect4:
            elif item.tag == 'sect4':
                title = item.find('title').text
                ret.append(MdHeader(5, [Text(title)]))
                ret.extend(self.paras(item))

            # sect5:
            elif item.tag == 'sect5':
                title = item.find('title').text
                ret.append(MdHeader(6, [Text(title)]))
                ret.extend(self.paras(item))

            # variablelist
            elif item.tag == 'variablelist':
                varlistentry = item.find('varlistentry')

                ret.append(MdHeader(4, self.paras(varlistentry.find('term'))))

                for listitem in item.findall('listitem'):
                    for para in listitem.findall('para'):
                        ret.append(MdParagraph(self.paras(para)))

            # parameterlist
            elif item.tag == 'parameterlist':
                parameteritems = item.findall('parameteritem')
                lst = MdList([])
                for parameteritem in parameteritems:
                    name = parameteritem.find('parameternamelist').find('parametername')
                    description = parameteritem.find('parameterdescription').findall('para')
                    par = MdParagraph([])
                    if len(name) > 0:
                        par.extend(self.paras(name))
                    else:
                        par.append(Code(name.text))
                    par.append(Text(' '))
                    for ip in description:
                        par.extend(self.paras(ip))
                    lst.append(par)
                ret.append(Br())
                ret.append(MdBold([Text(SIMPLE_SECTIONS[item.get('kind')])]))
                ret.append(Br())
                ret.append(lst)

            # simplesect
            elif item.tag == 'simplesect':
                kind = item.get('kind')
                ret.append(Br())
                ret.append(MdBold([Text(SIMPLE_SECTIONS[kind])]))
                if kind != 'see':
                    ret.append(Br())
                else:
                    ret.append(Text(' '))

                for sp, has_more in lookahead(item.findall('para')):
                    ret.extend(self.paras(sp))
                    if kind == 'see':
                        if has_more:
                            ret.append(Text(', '))
                    else:
                        ret.append(Br())

            # xrefsect
            elif item.tag == 'xrefsect':
                xreftitle = item.find('xreftitle')
                xrefdescription = item.find('xrefdescription')
                ret.append(Br())
                ret.append(MdBold(self.paras(xreftitle)))
                ret.append(Br())
                for sp in xrefdescription.findall('para'):
                    ret.extend(self.paras(sp))
                    ret.append(Br())

            # Hard link
            elif item.tag == 'ulink':
                ret.append(MdLink(self.paras(item), item.get('url')))

            # Bold
            elif item.tag == 'bold':
                ret.append(MdBold(self.paras(item)))

            # Emphasis
            elif item.tag == 'emphasis':
                ret.append(MdItalic(self.paras(item)))

            # End of the item text
            if item.tail and item.tail.strip():
                if italic:
                    ret.append(MdItalic([Text(item.tail.rstrip())]))
                else:
                    ret.append(Text(item.tail.rstrip()))
        return ret
