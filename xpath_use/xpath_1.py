from lxml import etree

xml = """
<root>
    <element1 attribute="value1">Text1</element1>
    <element2 attribute="value2">Text2</element2>
    <element3 attribute="value3">
        <subelement attribute="subvalue1">    
            <element2 attribute="value2">Text2</element2>
        </subelement>
        <subelement attribute="subvalue2">    
            <element2 attribute="value2">Text2</element2>
        </subelement>
        <element2 attribute="value2">
            <subelement attribute="subvalue2">Subtext3</subelement>
            <element2 attribute="value2">
                <subelement attribute="subvalue2">Subtext4</subelement>
            </element2>
        </element2>
    </element3>
</root>
"""

tree = etree.XML(xml)

# dom1 = tree.xpath('/root/element1/text()')
# dom2 = tree.xpath('/root/element3//subelement/text()') # 后代选择器
# dom2 = tree.xpath('/root/*//subelement/text()') # 通配符
# dom2 = tree.xpath('/root/element3/subelement[1]/text()') # 索引
# dom2 = tree.xpath('/root/element1[@attribute="value1"]/text()') # 属性选择器
dom2 = tree.xpath('/root/element3/subelement') # 属性选择器 

for dom in  dom2:
    print(dom.xpath('./element2/text()'))
    print(dom.xpath('./element2/@attribute'))

# print(dom2)
