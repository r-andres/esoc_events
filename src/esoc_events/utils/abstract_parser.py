from xml.etree import ElementTree
from typing import Any


class AbstractParser:

    def __init__(self, path: Any) -> None:
        self.path = path
        self.doc = ElementTree.parse(path)
        self.root = self.doc.getroot()
