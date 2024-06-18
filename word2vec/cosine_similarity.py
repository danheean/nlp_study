"""
- https://wikidocs.net/24603
"""
import pandas as pd
from repia_search_engine import load_rdata, load_di_u_conf, preprocessing, remove_stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(analyzer = 'word',
                             tokenizer = None,
                             preprocessor = None,
                             stop_words = None,
                             min_df = 2,
                             ngram_range=(1,3),
                             max_features = 2000,
                             )


di_file_path = '../data/di_u.conf'
file_path = '../data/nc_doc_1_1.1'

data = pd.DataFrame(load_rdata(di_file_path, file_path))

#print(data.head(2))

#print(data.shape)
#print(data.dtypes)

#data['ntt_sj'] = data['ntt_sj'].astype(str)

tfidf = TfidfVectorizer()
#print(data['ntt_sj'])
#print(data['ntt_sj'].describe())

#ntt_sj = data['ntt_sj'].values
#print(type(ntt_sj))
#print(ntt_sj)

# for ntt in ntt_sj:
#     print(ntt)
#     print(type(ntt))

#data['ntt_sj_preprocessing'] = data['ntt_sj'].apply(preprocessing)

#data['ntt_sj_preprocessing'] = data['ntt_sj'].apply(preprocessing)
#data['ntt_sj_preprocessed'] = data['ntt_sj_preprocessing'].apply(remove_stopwords)

#title_feature_vector = vectorizer.fit_transform(data['ntt_sj_preprocessed'])
#tfidf_matrix = tfidf.fit_transform(data['ntt_sj_preprocessed'])
#print(tfidf_matrix.shape)

data['ntt_sj'] = data['ntt_sj'].str.lower()

tfidf_matrix = tfidf.fit_transform(data['ntt_sj'])

print('TF-IDF 행렬의 크기(shape) :',tfidf_matrix.shape)

