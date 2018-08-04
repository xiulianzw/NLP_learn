import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
from PIL import Image
from os import path
import matplotlib.pyplot as plt
#用来正常显示中文
plt.rcParams["font.sans-serif"]=["SimHei"]
#用来正常显示负号
plt.rcParams["axes.unicode_minus"]=False
import os
import random,jieba

'''
绘制单个词一个圆形的词云
'''
def single_wordColud():
    text = "第一 第二 第三 第四"
    #产生一个以(150,150)为圆心,半径为130的圆形mask
    x,y = np.ogrid[:300,:300]
    mask = (x-150) ** 2 + (y-150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)
    wc = WordCloud(background_color="white",repeat=True,mask=mask)
    wc.generate(text)

    #将x轴和y轴坐标隐藏
    plt.axis("off")
    plt.imshow(wc,interpolation="bilinear")
    plt.show()

def grey_color_func(word,font_size,position,orientation,random_state=None,**kwargs):
    return "hsl(0,0%%,%d%%)"%random.randint(60,100)


'''
从文件中读取停用词
'''
def get_stopwords():
    dir_path = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    #获取停用词的路径
    stopwords_path = os.path.join(dir_path,"txt/stopwords.txt")
    #创建set集合来保存停用词
    stopwords = set()
    #读取文件
    f = open(stopwords_path,"r",encoding="utf-8")
    line_contents = f.readline()
    while line_contents:
        #去掉回车
        line_contents = line_contents.replace("\n","").replace("\t","").replace("\u3000","")
        stopwords.add(line_contents)
        line_contents = f.readline()
    return stopwords

'''
中文分词
'''
def segment_words(text):
    article_contents = ""
    #使用jieba进行分词
    words = jieba.cut(text,cut_all=False)
    for word in words:
        #使用空格来分割词
        article_contents += word+" "
    return article_contents

def drow_mask_wordColud():
    #获取当前文件的父目录
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    mask = np.array(Image.open(path.join(d,"img/test.jpg")))
    text = open(path.join(d,"txt/test.txt"),"r",encoding="utf-8").read().replace("\n","").replace("\t","").replace("\u3000","")
    #对文本进行分词
    text = segment_words(text)
    #获取停用词
    stopwords = get_stopwords()
    #创建词云
    '''
    max_words:显示词的数量
    mask:背景
    stopwords:停用词,是一个set集合
    margin:词之间的间隔
    background_color:词云图片背景颜色
    '''
    wc = WordCloud(max_words=100,mask=mask,background_color="white",stopwords=stopwords,margin=10,random_state=1).generate(text)
    default_colors = wc.to_array()
    # #保存词云图片
    # wc.to_file("test.png")
    plt.imshow(default_colors,interpolation="bilinear")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    single_wordColud()
