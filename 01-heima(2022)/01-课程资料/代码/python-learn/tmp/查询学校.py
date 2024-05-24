# 作者：程序员石磊
# 链接：https://www.zhihu.com/question/440101289/answer/2117766557
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import requests
import json
from bs4 import BeautifulSoup
# pip install beautifulsoup4
# pip install  requests
fo = open("d:/计算机专业非全日制.txt", "w")
colIndex = [0,4,5,6,8,9]


def handleTd(trItem):
  for  index, tdItem in enumerate(trItem.select("td")):
    if index in colIndex:
      continue
    if index == 7:
      fo.writelines('| '+ '[详情](https://yz.chsi.com.cn'+tdItem.select('a')[0].attrs['href']+')' )
      fo.writelines(' |\n')
      continue
    value = tdItem.string if tdItem.string!=None else ' '
    fo.writelines(' | '+value)


def getProfession(url):
  professionHtml = requests.post(' https://yz.chsi.com.cn'+url)
  professionHtml.encoding = 'utf-8'
  professionSoup = BeautifulSoup(professionHtml.text, 'html.parser')
  trs = professionSoup.select(".more-content tr")
  for trItem in trs:
    handleTd(trItem)

def getSchool(ssdm):
  # ssdm 省市代码 yjxkdm 学科代码  zymc 专业名称 xxfs 学习方式
  r = requests.post('https://yz.chsi.com.cn/zsml/queryAction.do', params={'ssdm': ssdm, 'yjxkdm': '0854', 'zymc': '电子信息','xxfs':2})
  r.encoding = 'utf-8'
  soup = BeautifulSoup(r.text, 'html.parser')
  for item in soup.select(".ch-table a"):
    fo.writelines('## '+ item.string+'\n' )
    fo.writelines('| 院系所   |  专业  |  研究方向  |   考试范围 |  \n' )
    fo.writelines('| - | - | - |  - |   \n' )

    getProfession(item.attrs['href'])

def main():
  cities = requests.post('https://yz.chsi.com.cn/zsml/pages/getSs.jsp')
  for city in json.loads(cities.text):
    fo.writelines('# '+ city['mc']+'\n' )
    getSchool(city['dm'])

if __name__=="__main__":
  main()
  fo.close()