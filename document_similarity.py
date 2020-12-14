import os
import numpy as np
from nltk.tokenize import word_tokenize
from global_variables import EMBEDDINGS_DICTIONARY, TF_IDF_MATRIX, SIMILARITY_MATRIX, PROCESSED_DOCUMENTS_DIRECTORY

NUMBER_OF_DOCUMENTS = 5


class DocumentSimilarity:
    def __init__(self, processed_query):
        self.processed_query = processed_query

    def find_similar_documents(self):
        query_doc = [w for w in word_tokenize(self.processed_query)]
        query_doc_bow = EMBEDDINGS_DICTIONARY.doc2bow(query_doc)

        # perform a similarity query against the corpus
        query_doc_tf_idf = TF_IDF_MATRIX[query_doc_bow]
        print('Comparing Result:', SIMILARITY_MATRIX[query_doc_tf_idf])
        results = SIMILARITY_MATRIX[query_doc_tf_idf]
        return results

    def filter_top_results(self, results):
        top_results_idx = results.argsort()[::-1][:NUMBER_OF_DOCUMENTS]
        rounded_results = [np.around(res, 4) for res in results]

        top_results = []
        for idx in top_results_idx:
            if rounded_results[idx] != 0:
                top_results.append((os.listdir(PROCESSED_DOCUMENTS_DIRECTORY)[
                                   idx].upper()[:-4], rounded_results[idx]))

        return top_results

    def generate_search_results(self):
        search_results = self.find_similar_documents()
        top_search_results = self.filter_top_results(search_results)

        return top_search_results
