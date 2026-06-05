import unittest
from xml.etree.ElementTree import (
    Element,
    SubElement,
)

from doxybook.cache import (
    Cache,
)
from doxybook.constants import (
    Kind,
)
from doxybook.node import (
    Node,
)
from doxybook.property import (
    Property,
)
from doxybook.utils import (
    sanitize_anonymous_compound_type,
)
from doxybook.xml_parser import (
    XmlParser,
)


class TestAnonymousCompounds(unittest.TestCase):
    def setUp(self):
        self.cache = Cache()
        self.parser = XmlParser(cache=self.cache, target='single-markdown')
        self.options = {'target': 'single-markdown', 'link_prefix': ''}
        self.root = Node('root', None, self.cache, self.parser, None, options=self.options)

    def _create_compound_node(self, refid: str, kind: str, name: str) -> Node:
        xml = Element('compounddef', {'id': refid, 'kind': kind})
        SubElement(xml, 'name').text = name
        return Node(None, xml, self.cache, self.parser, self.root, options=self.options)

    def _create_type_property(self, type_element: Element) -> Property.Type:
        xml = Element('memberdef', {'kind': 'variable'})
        xml.append(type_element)
        return Property.Type(xml, self.parser, Kind.VARIABLE)

    def test_sanitize_qualified_anonymous_names(self):
        self.assertEqual(sanitize_anonymous_compound_type('union outer_t::@123 slot'), 'anonymous union slot')
        self.assertEqual(sanitize_anonymous_compound_type('struct @456 flags'), 'anonymous struct flags')

    def test_type_ref_to_anonymous_compound_uses_placeholder(self):
        anonymous_union = self._create_compound_node('anon_union', 'union', 'outer_t::@123')
        self.assertTrue(anonymous_union.is_anonymous_synthetic)

        typ = Element('type')
        typ.text = 'union '
        SubElement(typ, 'ref', {'refid': 'anon_union', 'kindref': 'compound'}).text = 'outer_t::@123'

        prop = self._create_type_property(typ)
        self.assertEqual(prop.md(), 'anonymous union')
        self.assertEqual(prop.plain(), 'anonymous union')

    def test_named_type_link_is_kept(self):
        self._create_compound_node('struct_named__t', 'struct', 'named_t')

        typ = Element('type')
        typ.text = 'struct '
        SubElement(typ, 'ref', {'refid': 'struct_named__t', 'kindref': 'compound'}).text = 'named_t'

        prop = self._create_type_property(typ)
        rendered = prop.md()
        self.assertIn('[**named\\_t**](#struct-named_t)', rendered)
        self.assertNotIn('@', rendered)

    def test_anonymous_node_display_name(self):
        anonymous_struct = self._create_compound_node('anon_struct', 'struct', '@999')
        self.assertEqual(anonymous_struct.name, 'anonymous struct')
        self.assertEqual(anonymous_struct.name_short, 'anonymous struct')
        self.assertEqual(anonymous_struct.name_long, 'anonymous struct')


if __name__ == '__main__':
    unittest.main()
