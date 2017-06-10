'''
@Saleem
training module for dangerous speech
'''

import sys
sys.dont_write_bytecode = True

#-----------------------------------------------------------------------------------------------
def testing(test_data2, clf, count_vect, tfidf_transformer):
        test_data = []
        idlist = []
        for item in test_data2:
                test_data.append(item[1])
                idlist.append(item[0])
        X_test_counts = count_vect.transform(test_data)
        X_test_tfidf = tfidf_transformer.transform(X_test_counts)
        p = clf.predict(X_test_tfidf)
        predicted = p.tolist()
        return idlist, predicted
