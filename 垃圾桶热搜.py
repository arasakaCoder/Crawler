'''
'label_name',   沸、新、热等
 'star_word', 
 'raw_hot',     原生热度？
 'onboard_time',在榜时间 
 'subject_label', 主体标签：综艺、晚会、电影等
 'flag', 
 'realpos',     真实排名,从1开始，不包含商业推广
 'topic_flag', 
 'ad_info',     广告消息？
 'channel_type', Entertainment,应该是娱乐圈才有的标识
 'fun_word', 
 'word_scheme', 题目，带#号
 'category',    分类：美食、社会新闻、国内要闻、综艺等
 'word',        真实题目
 'subject_querys', 
 'mid', 
 'emoticon', 
 'note',        题目
 'num',         显示热度值
 'rank',        内部列表排名,从0开始,
 'mblog'        具体内容
'''

import time
import requests
from bs4 import BeautifulSoup

url = "https://weibo.com/ajax/statuses/hot_band"
resp = requests.get(url)
js = resp.json()
hotList = js["data"]['band_list']
resp.close()


def getRealPos(item):
    # 遇到商业推广会抛出异常，自动过滤
    return item["realpos"]


def getTitle(item):
    try:
        return item["word"]
    except Exception:
        return "null"


def getRawHot(item):
    try:
        return int(item["raw_hot"])
    except Exception:
        return 0


def getNum(item):
    try:
        return int(item["num"])
    except Exception:
        return -1


def getDetails(item):
    try:
        soup = BeautifulSoup(item["mblog"]["text"], "html.parser")
        return "https:" + soup.find("a").get("href")
    except Exception:
        return "null"


def getMessage():
    for item in hotList:
        try:
            print(getRealPos(item), getTitle(item), getNum(item).__str__(), getDetails(item), sep=",")
        except Exception:
            pass


def getAbnormalMessage():
    ls = []
    for item in hotList:
        try:
            if getRawHot(item) != getNum(item):
                ls.append(f"{getRealPos(item)},{getTitle(item)},{getRawHot(item)},{getNum(item)}")
        except Exception:
            pass
    return ls


def main():
    getMessage()

if __name__ == '__main__':
    main()
    print(getAbnormalMessage())
