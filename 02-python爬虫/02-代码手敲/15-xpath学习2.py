# @Date : 2024/3/19 15:21
# @Author : liming

from lxml import etree

tree = etree.parse("xpath.html")

# result = tree.xpath('/html')
ol_li_list = tree.xpath('/html/body/ol/li')
# print(result)

for li in ol_li_list:
    result = li.xpath('./a/text()')
    print(result)
    result2 = li.xpath('./a/@href')
    print(result2)