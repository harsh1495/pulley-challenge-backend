import os
import gensim
import nltk
from nltk.tokenize import word_tokenize

# globals
PROCESSED_DOCUMENTS_DIRECTORY = os.path.join(
    os.getcwd(), "processed_documents")
SIMILARITY_INDEX_FOLDER = "index"


class Corpus:
    def __init__(self, PLAYS_DIRECTORY):
        self.PLAYS_DIRECTORY = PLAYS_DIRECTORY
        self.all_plays = []
        self.all_processed_docs = []
        self.final_file_names = []

    def load_all_plays(self):
        for play in os.listdir(self.PLAYS_DIRECTORY):
            self.all_plays.append(play)

    def load_document_corpus(self):
        self.load_all_plays()
        for play in self.all_plays:
            for filename in os.listdir(os.path.join(self.PLAYS_DIRECTORY, play, "processed_pages")):
                # print(filename)
                if filename.endswith(".txt"):
                    self.final_file_names.append(filename)
                    filepath = os.path.join(
                        self.PLAYS_DIRECTORY, play, "processed_pages", filename)
                    with open(filepath, 'r', encoding="latin-1") as file:
                        page_text = file.read()

                    self.all_processed_docs.append(page_text)

                else:
                    continue

        return self.all_processed_docs, self.final_file_names

    def generate_unigrams_bigrams(self, document_corpus):
        gen_docs = []
        for text in document_corpus:
            gen_doc_play = []

            # unigrams
            tokens = word_tokenize(text)
            gen_doc_play.extend(tokens)

            # bigrams
            bigrm = nltk.bigrams(tokens)
            for bg in bigrm:
                gen_doc_play.append(' '.join(bg))

            gen_docs.append(gen_doc_play)

        return gen_docs

    def generate_similarity_index(self, document_corpus):
        gen_docs = self.generate_unigrams_bigrams(document_corpus)
        embeddings_dictionary = gensim.corpora.Dictionary(gen_docs)
        similarity_corpus = [embeddings_dictionary.doc2bow(
            gen_doc) for gen_doc in gen_docs]
        tf_idf_matrix = gensim.models.TfidfModel(similarity_corpus)

        # building the index
        similarity_matrix = gensim.similarities.Similarity(
            SIMILARITY_INDEX_FOLDER, tf_idf_matrix[similarity_corpus], num_features=len(embeddings_dictionary))

        return embeddings_dictionary, tf_idf_matrix, similarity_matrix
