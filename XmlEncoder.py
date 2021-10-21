import os
import xml.dom.minidom as md


class XmlElement:
    def __init__(self, tag_name):
        self.__tag_name = tag_name
        self.__value = ""
        # All attributes must be of type dict with key and value (literally)
        self.__attibutes = []
        # All children must be of type XmlElement
        self.__childs = []
        self.__start_prefix = "<{}".format(tag_name)
        self.__close_suffix = ">"
        self.__end_suffix = "</{}>".format(self.__tag_name)

    def append_child(self, child):
        if len(self.__value) > 0:
            raise Exception("You can't set a value and set a child at in the same tag")
        self.__childs.append(child)

    def remove_child(self, child):
        self.__childs.remove(child)

    def append_attribute(self, key, value):
        self.__attibutes.append({"key": key, "value": value})

    def remove_attribute(self, attribute):
        self.__attibutes.remove(attribute)

    def set_valor(self, value):
        if len(self.__childs) > 0:
            raise Exception("You can't set a value and set a child at in the same tag")
        self.__value = value

    @property
    def childs(self):
        child_values = ""
        for c in self.__childs:
            child_values += c.encode + ""
        return child_values

    @property
    def attributes(self):
        attributes = ""
        for atr in self.__attibutes:
            attributes += ' {}="{}"'.format(atr["key"], atr["value"])
        return attributes

    @property
    def encode(self):
        return self.__start_prefix + self.attributes + self.__close_suffix + self.__value + self.childs + self.__end_suffix

    @property
    def encode_pretty(self):
        xml = self.encode
        dom = md.parseString(xml)
        pretty_xml = dom.toprettyxml()
        return os.linesep.join([s for s in pretty_xml.splitlines() if s.strip()]).replace("?>", 'encoding="UTF-8"?>')
