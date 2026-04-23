from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import math
corpus = [
    "the sky is blue",
    "the sun is bright",
    "the sun in the sky"
]


def tokenizer(doc): 
    return [w for w in word_tokenize(doc) if w not in stopwords.words('english')]

corpus_tokens = [tokenizer(doc) for doc in corpus]

print(corpus_tokens)
#[['sky', 'blue'], ['sun', 'bright'], ['sun', 'sky']]


def tf(t, doc_tokens):
    N = len(doc_tokens)
    res = 0
    for t_ in doc_tokens:
        if t == t_:
            res += 1
    return res / N

def doc_tf_old(doc_tokens):
    res = {}
    N = len(doc_tokens)
    for t in doc_tokens:
        res[t] = tf(t,doc_tokens) 
    return res


def doc_tf(doc_tokens):
    N = len(doc_tokens)
    count = Counter(doc_tokens)
    for c in count:
        count[c] /= N 
    return count

# idf(t, D) = log10(N/df)
def idf_aux(t, corpus_tokens):
    N = len(corpus_tokens)
    df = 0
    for d in corpus_tokens:
        if t in d:
            df = df + 1
    return math.log( N / df, 10)
    

def idf(corpus_tokens):
    tokens = set([token for d in corpus_tokens for token in d])
    res = {}
    for t in tokens:
        res[t] = idf_aux(t,corpus_tokens)
    return res

#print(idf(corpus_tokens))


def tf_idf(corpus_tokens):
    res = []
    idf_dict = idf(corpus_tokens)
    for doc_tokens in corpus_tokens:
        tf_idf_dict = {}
        tf_dict = doc_tf(doc_tokens)
        for termo in tf_dict:
            tf_idf_dict[termo] = idf_dict[termo] * tf_dict[termo]
        res.append(tf_idf_dict)
    return res  


def vectorize(tf_idf_list):
    vocab = set([token for d in corpus_tokens for token in d])
    res = []
    for doc in tf_idf_list:
        res.append([doc.get(token, 0) for token in vocab])
    return res

tf_idf_list = tf_idf(corpus_tokens)
doc_vectors = vectorize(tf_idf_list)
print(doc_vectors)

query = "The bright sun"

query_tokens = tokenizer(query)








#{sky:0.176, blue: 0.477, sun: 0.176, bright:0.477} 

#{sky:0.5, blue: 0.5}  
# 
#   



