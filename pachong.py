from gevent import monkey
monkey.patch_all()
import gevent
from bs4 import BeautifulSoup  as bs
import requests

def gethtml(url):
    ret = requests.get(url)
    ret.encoding = 'utf-8'
    return ret.text

def start(capname, curl, res):
    sp = bs(gethtml(curl), 'lxml')
    rescap = str(sp.find('div', id='content')).replace('<br/><br/>', '\n')[18:-6]
    res[capname] = rescap
    



def main(url):
    soup =  bs(gethtml(url),'lxml')

    tital = soup.h1.text
    print(tital)

    sp = bs(str(soup.find('dl')), 'lxml')

    capsu  = {}
    capsr   = {}
    capsurls = []
    capsname = []

    for cap in sp.find_all('a'):
        capsname.append(cap.text)
        capsurls.append('https://www.biquge.com.cn/' + cap['href'])
        capsu[cap.text] = cap['href']

    jobs = [gevent.spawn(start, capsname[0], capsurls[0], capsr) for i in range(len(capsname))]
    gevent.joinall(jobs)

    print(capsr[capsname[0]])
    
(151, 398, 321, 228)
if __name__ == "__main__":
    main('https://www.biquge.com.cn/book/11029/')


