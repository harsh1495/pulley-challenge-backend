import os
import pickle

print("loading global variables...")

# file names
SHAKESPEARE_WORKS_FILE = "data/completeworks.txt"
STOPWORDS_FILE = "data/stopwords.txt"
FINAL_FILE_NAMES_FILE = "data/filenames.pickle"
EMBEDDINGS_FILE = "data/embeddings.pickle"
TF_IDF_MATRIX_FILE = "data/tfidf.pickle"
SIMILARITY_MATRIX_FILE = "data/similarity.pickle"

# folder names
DOCUMENTS_DIRECTORY = os.path.join(os.getcwd(), "documents")
PROCESSED_DOCUMENTS_DIRECTORY = os.path.join(
    os.getcwd(), "processed_documents")
PLAYS_DIRECTORY = os.path.join(os.getcwd(), "plays")

# list of shakespeare plays under consideration
SHAKESPEARE_WORKS = ["ALL’S WELL THAT ENDS WELL", "ANTONY AND CLEOPATRA", "AS YOU LIKE IT", "THE COMEDY OF ERRORS", "THE TRAGEDY OF CORIOLANUS", "CYMBELINE", "THE TRAGEDY OF HAMLET, PRINCE OF DENMARK", "THE FIRST PART OF KING HENRY THE FOURTH", "THE SECOND PART OF KING HENRY THE FOURTH", "THE LIFE OF KING HENRY V", "THE FIRST PART OF HENRY THE SIXTH", "THE SECOND PART OF KING HENRY THE SIXTH", "THE THIRD PART OF KING HENRY THE SIXTH", "KING HENRY THE EIGHTH", "KING JOHN", "THE TRAGEDY OF JULIUS CAESAR", "THE TRAGEDY OF KING LEAR", "LOVE’S LABOUR’S LOST", "MACBETH",
                     "MEASURE FOR MEASURE", "THE MERCHANT OF VENICE", "THE MERRY WIVES OF WINDSOR", "A MIDSUMMER NIGHT’S DREAM", "MUCH ADO ABOUT NOTHING", "OTHELLO, THE MOOR OF VENICE", "PERICLES, PRINCE OF TYRE", "KING RICHARD THE SECOND", "KING RICHARD THE THIRD", "THE TRAGEDY OF ROMEO AND JULIET", "THE TAMING OF THE SHREW", "THE TEMPEST", "THE LIFE OF TIMON OF ATHENS", "THE TRAGEDY OF TITUS ANDRONICUS", "THE HISTORY OF TROILUS AND CRESSIDA", "TWELFTH NIGHT: OR, WHAT YOU WILL", "THE TWO GENTLEMEN OF VERONA", "THE TWO NOBLE KINSMEN", "THE WINTER’S TALE", "A LOVER’S COMPLAINT"]

# load corpus of shakespeare plays divided by pages
# from corpus import Corpus

# corpus_obj = Corpus(PLAYS_DIRECTORY)
# documents_corpus, FINAL_FILE_NAMES = corpus_obj.load_document_corpus()
# EMBEDDINGS_DICTIONARY, TF_IDF_MATRIX, SIMILARITY_MATRIX = corpus_obj.generate_similarity_index(
#     documents_corpus)

# with open('data/filenames.pickle', 'wb') as f:
#     pickle.dump(FINAL_FILE_NAMES, f)

# with open('data/embeddings.pickle', 'wb') as f:
#     pickle.dump(EMBEDDINGS_DICTIONARY, f)

# with open('data/tfidf.pickle', 'wb') as f:
#     pickle.dump(TF_IDF_MATRIX, f)

# with open('data/similarity.pickle', 'wb') as f:
#     pickle.dump(SIMILARITY_MATRIX, f)

# load corpus of shakespeare plays divided by pages
with open(FINAL_FILE_NAMES_FILE, 'rb') as f:
    FINAL_FILE_NAMES = pickle.load(f)

with open(EMBEDDINGS_FILE, 'rb') as f:
    EMBEDDINGS_DICTIONARY = pickle.load(f)

with open(TF_IDF_MATRIX_FILE, 'rb') as f:
    TF_IDF_MATRIX = pickle.load(f)

with open(SIMILARITY_MATRIX_FILE, 'rb') as f:
    SIMILARITY_MATRIX = pickle.load(f)
