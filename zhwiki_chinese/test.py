import logging
from gensim import models
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

'''
获取一个圆形的mask
'''
def get_mask():
    x,y = np.ogrid[:300,:300]
    mask = (x-150) ** 2 + (y-150)**2 > 130 ** 2
    mask = 255 * mask.astype(int)
    return mask

'''
绘制词云
'''
def draw_word_cloud(word_cloud):
    wc = WordCloud(background_color="white",mask=get_mask())
    wc.generate_from_frequencies(word_cloud)
    #隐藏x轴和y轴
    plt.axis("off")
    plt.imshow(wc,interpolation="bilinear")
    plt.show()

def test():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    model = models.Word2Vec.load("model/wiki_corpus.model")
    #输入一个词找出相似的前10个词
    # one_corpus = ["人工智能"]
    # result = model.most_similar(one_corpus[0],topn=100)
    # #将返回的结果转换为字典,便于绘制词云
    # word_cloud = dict()
    # for sim in result:
    #     # print(sim[0],":",sim[1])
    #     word_cloud[sim[0]] = sim[1]
    # #绘制词云
    # draw_word_cloud(word_cloud)


    #输入两个词计算相似度
    # two_corpus = ["腾讯","阿里巴巴"]
    # res = model.similarity(two_corpus[0],two_corpus[1])
    # print("similarity:%.4f"%res)

    #输入三个词类比
    three_corpus = ["北京","上海","广州"]
    res = model.most_similar([three_corpus[0],three_corpus[1],three_corpus[2]],topn=100)
    #将返回的结果转换为字典,便于绘制词云
    word_cloud = dict()
    for sim in res:
        # print(sim[0],":",sim[1])
        word_cloud[sim[0]]=sim[1]
     #绘制词云
    draw_word_cloud(word_cloud)


if __name__ == "__main__":
    test()
