'''
@Saleem
training module for dangerous speech
'''

import sys
sys.dont_write_bytecode = True

#-----------------------------------------------------------------------------------------------


def testing(test_data, clf, count_vect, tfidf_transformer):
    X_test_counts = count_vect.transform(test_data)
    X_test_tfidf = tfidf_transformer.transform(X_test_counts)
    p = clf.predict(X_test_tfidf)
    predicted = p.tolist()
    return predicted
