from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

def get_mask():
    x,y = np.ogrid[:300,:300]
    mask = (x-150) ** 2 + (y-150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)
    return mask

if __name__ == "__main__":
    #每个词的权重
    text = {"第一":0.1,"第二":0.2,"第三":0.3,"第四":0.4,"第五":0.5}
    wc = WordCloud(background_color="white",mask=get_mask())
    wc.generate_from_frequencies(text)
    plt.axis("off")
    plt.imshow(wc,interpolation="bilinear")
    plt.show()
