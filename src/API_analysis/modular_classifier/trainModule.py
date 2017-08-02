'''
@Saleem
training module for dangerous speech
'''

import sys
sys.dont_write_bytecode = True

#-----------------------------------------------------------------------------------------------
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression

#-----------------------------------------------------------------------------------------------
def training(data2, target, algo):
        data = []
        for item in data2:
                data.append(item[1])
        count_vect = CountVectorizer()
        X_train_counts = count_vect.fit_transform(data)
        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
        if algo == 'nb':
                clf = MultinomialNB().fit(X_train_tfidf,target)
        if algo == 'svm':
                clf = LinearSVC().fit(X_train_tfidf, target)
        if algo == 'lr':
                clf = LogisticRegression().fit(X_train_tfidf, target)

        return clf, count_vect, tfidf_transformer

	
