import os
import numpy as np
import gensim
from nltk.tokenize import word_tokenize
from global_variables import PLAYS_DIRECTORY

PAGES_SIMILARITY_INDEX_FOLDER = "index_pages"


class PageSimilarity:
    def __init__(self, processed_query, top_documents):
        self.processed_query = processed_query
        self.top_documents = top_documents
        self.final_file_names = []

    def load_page_corpus(self):
        pages_corpus = []

        for document in self.top_documents:
            for filename in os.listdir(os.path.join(PLAYS_DIRECTORY, document[0], "processed_pages")):
                if filename.endswith(".txt"):
                    self.final_file_names.append(filename)
                    filepath = os.path.join(
                        PLAYS_DIRECTORY, document[0], "processed_pages", filename)
                    with open(filepath, 'r') as file:
                        page_text = file.read()

                    pages_corpus.append(page_text)

                else:
                    continue

        return pages_corpus

    def generate_pages_similarity_index(self, pages_corpus):
        gen_pages = [[w for w in word_tokenize(text)] for text in pages_corpus]
        dictionary_pages = gensim.corpora.Dictionary(gen_pages)

        pages_similarity_corpus = [dictionary_pages.doc2bow(
            gen_page) for gen_page in gen_pages]
        tf_idf_pages = gensim.models.TfidfModel(pages_similarity_corpus)

        # building the index
        index_pages_folder = PAGES_SIMILARITY_INDEX_FOLDER
        pages_similarity_matrix = gensim.similarities.Similarity(
            index_pages_folder, tf_idf_pages[pages_similarity_corpus], num_features=len(dictionary_pages))

        return dictionary_pages, tf_idf_pages, pages_similarity_matrix

    def find_similar_pages(self, dictionary_pages, tf_idf_pages, pages_similarity_matrix):
        query_doc = [w for w in word_tokenize(self.processed_query)]
        query_doc_bow = dictionary_pages.doc2bow(query_doc)

        # perform a similarity query against the pages corpus
        query_doc_tf_idf = tf_idf_pages[query_doc_bow]
        print('Comparing Result:', pages_similarity_matrix[query_doc_tf_idf])
        results = pages_similarity_matrix[query_doc_tf_idf]
        return results

    def filter_top_pages(self, results):
        top_results_idx = results.argsort()[::-1]

        top_pages = []
        for idx in top_results_idx:
            if results[idx] != 0:
                filename = self.final_file_names[idx]
                document_name = filename[:filename.find("_page")].upper()
                top_pages.append((filename, document_name, results[idx]))

        return top_pages

    def generate_page_search_results(self):
        pages_corpus = self.load_page_corpus()
        dictionary_pages, tf_idf_pages, pages_similarity_matrix = self.generate_pages_similarity_index(
            pages_corpus)
        search_results = self.find_similar_pages(
            dictionary_pages, tf_idf_pages, pages_similarity_matrix)
        top_search_pages = self.filter_top_pages(search_results)

        return top_search_pages
