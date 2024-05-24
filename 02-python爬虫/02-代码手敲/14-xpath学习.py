# @Date : 2024/3/19 15:12
# @Author : liming

from lxml import etree
# from lxml import html

xml = """
    <book>
        <id>1</id>
        <name>野花遍地香</name>
        price>29.99</price>
        <nick>臭豆腐</nick>
        <author>
            <nick id="10086">张三</nick>
            <nick id="10010">李四</nick>
            <nick id="10000">王五</nick>
            <div>
                <nick>惹了</nick>
            </div>
        </author>
        <partner>
          <nick id="a">apple</nick>
          <nick id="b">banana</nick>
        </partner>
    </book>
"""

tree = etree.XML(xml)
# tree = html.etree.XML(xml)
result = tree.xpath("/book")

print(result)