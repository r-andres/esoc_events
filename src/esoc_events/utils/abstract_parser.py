from xml.etree import ElementTree


class AbstractParser:

    def __init__(self, path) -> None:
        self.path = path
        self.doc = ElementTree.parse(path)
        self.root = self.doc.getroot()
