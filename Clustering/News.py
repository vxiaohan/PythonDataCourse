import pandas
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import numpy

df = pandas.read_excel('../Data/news.xlsx')
print(df.head())

titles = []
articles = []
for rec in df.iterrows():
    articles.append(' '.join(jieba.cut(rec[1].content)))
    titles.append(rec[1].title)
print(articles)
vectorier = CountVectorizer()
x = vectorier.fit_transform(articles)
cosine_similarities = cosine_similarity(x, x)
c = KMeans(n_clusters=10, init='k-means++', random_state=123)
k_data = c.fit_predict(cosine_similarities)
titles_array = numpy.array(titles)
print(titles_array[k_data == 8])
