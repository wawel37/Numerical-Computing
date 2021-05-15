from pickle import FALSE
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import os
import collections
import string


def split_corpus(corpus_name='corpus.txt', dir_name='articles'):
    i = 0
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    else:
        return
    with open(corpus_name, 'r') as corpus:
        text = corpus.read()
        text = text.split("\n\n")
        for article in text:
            article_name = article.split('\n')[0]
            file_path = dir_name + f"/article_{article_name.translate(str.maketrans('', '', string.punctuation + ' '))}.txt"
            with open(file_path,'w') as result_file:
                result_file.write(article)
            i += 1
            if (i == 1000):
                break
    
class SearchEngine:
    def __init__(self, data_dir = 'articles', IDF = True):
        self.IDF = IDF
        self.files_words = {}
        self.bag_of_words = {}
        self.read_data(data_dir)
        self.get_term_by_document_matrix()
        self.get_svd_rank_r()


    def read_data(self, dir_path='articles'):
        self.N_documents = 0
        for filename in os.listdir(dir_path):
            self.get_bag_of_words_from_one_file(os.path.join(dir_path, filename))
            self.N_documents += 1
        
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            with open(file_path, 'r') as file:
                for key, value in self.files_words[file_path].items():
                    self.bag_of_words.setdefault(key, 0)
                    self.bag_of_words[key] += value
    ## preprocessing of text
    ## getting rid of punctuations and stop words
    def parse_text(self, text):
        tokens = word_tokenize(text)
        tokens = [w.lower() for w in tokens]
        puctuation_map = str.maketrans('', '', string.punctuation)
        tokens = [w.translate(puctuation_map) for w in tokens]
        words = [w for w in tokens if w.isalpha()]
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        porter = PorterStemmer()
        stemmed = [porter.stem(word) for word in words]
        return stemmed
        
    def get_bag_of_words_from_one_file(self, file_path):
        with open(file_path, "r") as file:
            text = file.read()
            parsed_text = self.parse_text(text)
            frequency = dict(collections.Counter(parsed_text))
            self.files_words[file_path] = frequency
    
    def get_freq_vector(self, freq):
        vector = []
        for word in self.bag_of_words.keys():
            if word in freq.keys():
                vector.append(freq[word])
            else:
                vector.append(0)
        return np.array(vector, dtype=np.float32)
        
    def get_term_by_document_matrix(self):
        self.matrix_terms = np.zeros((len(self.bag_of_words.keys()), len(self.files_words.keys())), dtype=np.float32)
        for count, (file, words) in enumerate(self.files_words.items()):
            vector = self.get_freq_vector(words)
            self.matrix_terms[:,count] = vector
        if self.IDF:
            self.n_w = np.array(np.log(self.N_documents / (self.matrix_terms != 0).sum(1)))
            self.matrix_terms = (self.matrix_terms.T * self.n_w).T
        self.matrix_terms = self.matrix_terms / np.linalg.norm(self.matrix_terms, axis=0)
        

    def get_correlation_matrix(self, query_vector):
        correlations = []
        for i in range(self.N_documents):
            correlations.append(query_vector.dot(self.matrix_terms[:,i]))
        return correlations

    def get_svd_rank_r(self, r=100):
        u, s, v = np.linalg.svd(self.matrix_terms, full_matrices=FALSE)
        self.matrix_terms = np.zeros((len(u), len(v)))
        for i in range(r):
            self.matrix_terms += s[i] * np.outer(u.T[i], v[i])


    def search_query(self, query):
        query_processed = self.parse_text(query)
        frequency = dict(collections.Counter(query_processed))
        query_vector = self.get_freq_vector(frequency)
        if self.IDF:
            query_vector *= self.n_w
        query_vector = query_vector / np.linalg.norm(query_vector)
        correlations = self.get_correlation_matrix(query_vector)
        correlations = [(i, val) for (i, val) in enumerate(correlations)]
        correlations.sort(key=lambda x:x[1], reverse=True)

        print("Result: " + query)
        for (idx, correlation) in correlations[:3]:
            print(f"{list(self.files_words.keys())[idx]}, correlation: {correlation}")


split_corpus()
SE = SearchEngine()
SE.search_query("south africa")
SE.search_query("mathematics")
SE.search_query("climate extreme north africa")