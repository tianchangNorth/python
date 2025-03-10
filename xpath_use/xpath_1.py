from lxml import etree

xml = """
<root>
    <element1 attribute="value1">Text1</element1>
    <element2 attribute="value2">Text2</element2>
    <element3 attribute="value3">
        <subelement attribute="subvalue1">Subtext1</subelement>
        <subelement attribute="subvalue2">Subtext2</subelement>
        <element2 attribute="value2"><subelement attribute="subvalue2">Subtext2</subelement></element2>
    </element3>
</root>
"""

tree = etree.XML(xml)

# dom1 = tree.xpath('/root/element1/text()')
dom2 = tree.xpath('/root/element3//subelement/text()')

print(dom2)