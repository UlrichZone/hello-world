##爬取网页信息
# request
# BeautifulSoup

import requests
from bs4 import BeautifulSoup
import xlwt
import time

def spider(page):
    url = 'https://www.rong360.com/gl/daikuangonglue/list_1_{0}.html'.format(str(page))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
    response = requests.get(url, headers=headers).content
    soup = BeautifulSoup(response, 'lxml')
    list = soup.find_all('h3')
    global num
    for item in list:
        data_url = 'https://www.rong360.com' + item.a['href']
        data = requests.get(data_url, headers=headers).content
        data_soup = BeautifulSoup(data, 'lxml')
        try:
            tmp = data_soup.find_all('div', class_='act-content')[0]
            title = tmp.h1.text
            sentence = tmp.find_all('p')
            result = []
            for s in sentence:
                result.extend(s.text.strip().replace('\n', ''))
            context = ''.join(result)
            num += 1
            print("第{0}篇文章已爬取完成".format(num))
            sheet.write(num, 0, title)
            sheet.write(num, 1, context)
        except:
            pass

if __name__ == '__main__':
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('金融新闻数据')
    sheet.write(0, 0, '文章标题')
    sheet.write(0, 1, '文章内容')
    num = 0
    for i in range(1, 4472):
        spider(i)
        time.sleep(3)
    print("共爬取{0}篇文章".format(num))
    book.save(u"rong360爬虫结果.xls")


##存储为daatframe
pandas

##导出为csv


##数据库建表


##写入数据库
sqlalchemy
