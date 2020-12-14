import os
import gensim
from nltk.tokenize import word_tokenize

# globals
PROCESSED_DOCUMENTS_DIRECTORY = os.path.join(
    os.getcwd(), "processed_documents")
SIMILARITY_INDEX_FOLDER = "index"


class Corpus:
    def __init__(self):
        self.all_processed_docs = []

    def load_document_corpus(self):
        for filename in os.listdir(PROCESSED_DOCUMENTS_DIRECTORY):
            if filename.endswith(".txt"):
                filepath = os.path.join(
                    PROCESSED_DOCUMENTS_DIRECTORY, filename)
                print(filepath)
                with open(filepath, 'r') as file:
                    document_text = file.read()

                self.all_processed_docs.append(document_text)

            else:
                continue

        return self.all_processed_docs

    def generate_similarity_index(self, document_corpus):
        gen_docs = [[w for w in word_tokenize(text)]
                    for text in document_corpus]
        embeddings_dictionary = gensim.corpora.Dictionary(gen_docs)
        similarity_corpus = [embeddings_dictionary.doc2bow(
            gen_doc) for gen_doc in gen_docs]
        tf_idf_matrix = gensim.models.TfidfModel(similarity_corpus)

        # building the index
        similarity_matrix = gensim.similarities.Similarity(
            SIMILARITY_INDEX_FOLDER, tf_idf_matrix[similarity_corpus], num_features=len(embeddings_dictionary))

        return embeddings_dictionary, tf_idf_matrix, similarity_matrix
