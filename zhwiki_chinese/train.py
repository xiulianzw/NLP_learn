import logging
from gensim.models import word2vec

def main():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    sentences = word2vec.LineSentence("D:/dataset/NLP/zhwiki/AA/wiki_corpus")
    model = word2vec.Word2Vec(sentences,size=250)
    #保存模型
    model.save("model/wiki_corpus.model")

if __name__ == "__main__":
    main()
