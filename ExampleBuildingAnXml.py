from XmlEncoder import XmlElement

root_tag = XmlElement("root")
root_tag.append_attribute("attribute", "some_value")

child_tag = XmlElement("child")
child_tag.set_valor("raw_value")

root_tag.append_child(child_tag)

print(root_tag.encode_pretty)
