import os
import typing as t
from xml.etree import (
    ElementTree,
)

from doxybook.cache import (
    Cache,
)
from doxybook.constants import (
    Kind,
    Visibility,
)
from doxybook.node import (
    Node,
)
from doxybook.xml_parser import (
    XmlParser,
)


class Doxygen:
    def __init__(self, index_path: str, parser: XmlParser, cache: Cache, options: dict = {}):
        path = os.path.join(index_path, 'index.xml')
        print('Loading XML from: ' + path)
        xml = ElementTree.parse(path).getroot()

        self.parser = parser
        self.cache = cache
        self._options = options
        self.root = Node('root', None, self.cache, self.parser, None, options=self._options)
        self.groups = Node('root', None, self.cache, self.parser, None, options=self._options)
        self.files = Node('root', None, self.cache, self.parser, None, options=self._options)
        self.pages = Node('root', None, self.cache, self.parser, None, options=self._options)
        self.header_files = Node('root', None, self.cache, self.parser, None, options=self._options)

        for compound in xml.findall('compound'):
            kind = Kind.from_str(compound.get('kind'))
            refid = compound.get('refid')
            node = Node(
                os.path.join(index_path, refid + '.xml'),
                None,
                self.cache,
                self.parser,
                self.root,
                options=self._options,
            )
            node._visibility = Visibility.PUBLIC
            if kind.is_language():
                self.root.add_child(node)
            elif kind == Kind.GROUP:
                self.groups.add_child(node)
            elif kind in (Kind.FILE, Kind.DIR):
                self.files.add_child(node)
                if node.is_header_file:
                    self.header_files.add_child(node)
            elif kind == Kind.PAGE:
                self.pages.add_child(node)

        print('Extracting members from groups...')
        self._extract_group_members()

        print('Deduplicating data... (may take a minute!)')
        for i, child in enumerate(self.root.children.copy()):
            self._fix_duplicates(child, self.root, [])

        for i, child in enumerate(self.groups.children.copy()):
            self._fix_duplicates(child, self.groups, [Kind.GROUP])

        for i, child in enumerate(self.files.children.copy()):
            self._fix_duplicates(child, self.files, [Kind.FILE, Kind.DIR])

        self._fix_parents(self.files)

        print('Sorting...')
        self._recursive_sort(self.root)
        self._recursive_sort(self.groups)
        self._recursive_sort(self.files)
        self._recursive_sort(self.pages)

    def _extract_group_members(self):
        """
        Extract functions, macros, and other members from groups and add them to their respective files,
        effectively flattening the group hierarchy and treating group members as regular items.
        """
        extracted_refids = set()  # Track already extracted members to avoid duplicates

        def find_file_for_member(member: Node) -> t.Optional[Node]:
            """Find the appropriate file node for a member based on its location"""
            member_location = member.location
            if not member_location:
                return None

            # Search through all files to find the one that matches the member's location
            for file_node in self.files.children:
                if file_node.is_file and file_node.location == member_location:
                    return file_node
            return None

        def extract_from_group(group_node: Node):
            """Recursively extract members from a group and its subgroups"""
            members_to_extract = []

            for child in group_node.children:
                if child.kind == Kind.GROUP:
                    # Recursively process subgroups
                    extract_from_group(child)
                elif child.kind.is_language() and child.refid not in extracted_refids:
                    # This is a function, macro, variable, etc. - add it to extraction list
                    members_to_extract.append(child)
                    extracted_refids.add(child.refid)

            # Add extracted members to their respective files
            for member in members_to_extract:
                target_file = find_file_for_member(member)
                if target_file:
                    # Update parent reference to point to the file instead of group
                    member._parent = target_file
                    if member not in target_file.children:
                        target_file.add_child(member)
                else:
                    # If no file found, add to root as fallback
                    member._parent = self.root
                    self.root.add_child(member)

        # Process all groups
        for group in self.groups.children:
            extract_from_group(group)

    def _fix_parents(self, node: Node):
        if node.is_dir or node.is_root:
            for child in node.children:
                if child.is_file:
                    child._parent = node
                if child.is_dir:
                    self._fix_parents(child)

    def _recursive_sort(self, node: Node):
        node.sort_children()
        for child in node.children:
            self._recursive_sort(child)

    def _is_in_root(self, node: Node, root: Node):
        for child in root.children:
            if node.refid == child.refid:
                return True
        return False

    def _remove_from_root(self, refid: str, root: Node):
        for i, child in enumerate(root.children):
            if child.refid == refid:
                root.children.pop(i)
                return

    def _fix_duplicates(self, node: Node, root: Node, filter: t.List[Kind]):
        for child in node.children:
            if len(filter) > 0 and child.kind not in filter:
                continue
            if self._is_in_root(child, root):
                self._remove_from_root(child.refid, root)
            self._fix_duplicates(child, root, filter)

    def print(self):
        for node in self.root.children:
            self.print_node(node, '')
        for node in self.groups.children:
            self.print_node(node, '')
        for node in self.files.children:
            self.print_node(node, '')

    def print_node(self, node: Node, indent: str):
        print(indent, node.kind, node.name)
        for child in node.children:
            self.print_node(child, indent + '  ')
