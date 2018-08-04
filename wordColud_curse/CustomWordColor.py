from wordcloud import WordCloud,get_single_color_func
import matplotlib.pyplot as plt

'''
定义一个字体颜色设置类
'''
class GroupedColorFunc(object):
    def __init__(self,color_to_words,default_color):
        self.color_func_to_words=[
            (get_single_color_func(color),set(words))
            for (color,words) in color_to_words.items()
        ]
        self.defalt_color_func=get_single_color_func(default_color)
    def get_color_func(self,word):
        try:
            #设置每个词的颜色
            color_func = next(color_func for (color_func,words) in self.color_func_to_words
                              if word in words)
        except StopIteration:
            #词的默认颜色
            color_func = self.defalt_color_func
        return color_func
    def __call__(self,word,**kwargs):
        return self.get_color_func(word)(word,**kwargs)


if __name__ == "__main__":
    text = "第一 第二 第三 第四 第五 第六"
    #创建词云
    wc = WordCloud(collocations=False,background_color="white").generate(text)
    #设置词的颜色
    color_to_words={
        #使用RGB来设置词的颜色
        "#00ff00":["第一","第五"],
        "red":["第三","第六"],
        "yellow":["第二"]
    }
    #设置词默认的颜色
    default_color = "blue"
    grouped_color_func = GroupedColorFunc(color_to_words,default_color)
    #设置词云的颜色
    wc.recolor(color_func=grouped_color_func)
    #显示词云图
    plt.figure()
    plt.imshow(wc,interpolation="bilinear")
    plt.axis("off")
    plt.show()
