# Pulley Shakesearch Challenge

The backend is deployed on Heroku: https://pulley-challenge-harsh.herokuapp.com

## API Endpoints

### GET ```"/search"```

- Fetches a list of dictionary of all the search results (shows the first 10 search results by default)
- Request query arguments: q, start, size
- Returns: A list of dictionaries of search results containing the name of the Shakespeare play and the raw content which matches the search query

#### Sample Response

```
{
    {
        "results": [
            {
                "book": "THE COMEDY OF ERRORS",
                "raw_content": "THE COMEDY OF ERRORS\n\n\n\nSCENE: Ephesus\n\n\nACT
                    I\n\nSCENE I. A hall in the Duke's palace.\n\n Enter Duke, Egeon, Jailer, Officers and other
                    Attendants...."
            }
        ],
        "total_count": 1,
        "current_count": 1
    }
}
```

## Document Similarity Logic

### Packages Used

Gensim and NLTK

### Similarity Algorithm

#### Text Preprocessing Steps

The main steps for text preprocessing can be found in `document_preprocessor.py` which is called on the document corpus as well as the user query.

Code snippet from the `document_preprocessor.py` file:

```
self.processed_document_text = self.document_text.lower()
self.remove_punctuations()
self.remove_numbers()
self.remove_apostrophe()
self.remove_stopwords()
```

Steps
- Convert all the text to lowercase
- Remove all and any punctuations from the text
- Remove numbers from the text
- Remove different types of apostrophes from the text
- Remove English and Shakespearean stopwords from the text

#### Document Similarity Steps

The main logic of the similarity algorithm can be found in `corpus.py` wherein we are loading the complete works of Shakespeare and creating Gensim objects that we can later use to compare with the query for finding similar documents.

Code snippet from the `corpus.py` file:

```
gen_docs = self.generate_unigrams_bigrams(document_corpus)
embeddings_dictionary = gensim.corpora.Dictionary(gen_docs)
similarity_corpus = [embeddings_dictionary.doc2bow(
    gen_doc) for gen_doc in gen_docs]
tf_idf_matrix = gensim.models.TfidfModel(similarity_corpus)

# building the index
similarity_matrix = gensim.similarities.Similarity(
    SIMILARITY_INDEX_FOLDER, tf_idf_matrix[similarity_corpus], num_features=len(embeddings_dictionary))
```

Steps
- Generate unigrams and bigrams of the entire preprocessed text contained in the document corpus, which basically contains all the works of Shakespeare
- Create a Gensim Dictionary object that maps each token (unigram and bigram) to a unique id
- Create a Bag of Words corpus that contains the token id and its frequency in each document
- Generate a TF-IDF model (Term Frequency Inverse Document Frequency) which can down-weight tokens that appear in multiple documents
- Create a Similarity object, which builds an index for a given set of documents. Using this, we can compute cosine similarity of a dynamic query against a static corpus of documents
- Perform the 1st step for the query and use the Gensim TF-IDF model and similarity object to compute the top matching documents