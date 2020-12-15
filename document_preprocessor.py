import re
from global_variables import STOPWORDS_FILE


class DocumentPreprocessor:
    """
    This class takes in a document as an input and returns a processed version of it for further NLP tasks
    """

    def __init__(self, document_text):
        """
        Initialize class
        """
        self.document_text = document_text
        self.processed_document_text = ""
        self.stopwords = DocumentPreprocessor.read_stopwords()
        self.punctuation = "!\"#$%&()*+-—./:;<=>?@[\]^_`,{|}~\n"
        self.numbers_regex = r"[0-9]+"

    @staticmethod
    def read_stopwords():
        stopwords = []
        with open(STOPWORDS_FILE, 'r') as file:
            for word in file.read().split("\n"):
                stopwords.append(word)

        return stopwords

    def remove_punctuations(self):
        for symbol in self.punctuation:
            self.processed_document_text = self.processed_document_text.replace(
                symbol, ' ')

    def remove_numbers(self):
        self.processed_document_text = re.sub(
            self.numbers_regex, '', self.processed_document_text)

    def remove_apostrophe(self):
        self.processed_document_text = self.processed_document_text.replace(
            "'", "").replace("’", "").replace("‘", "")

    def remove_stopwords(self):
        valid_words = []
        for word in self.processed_document_text.split(" "):
            if not word:
                continue
            else:
                if word not in self.stopwords:
                    valid_words.append(word)

        self.processed_document_text = " ".join(valid_words)

    def process_document_text(self):
        """
        Run all functions defined above
        """

        self.processed_document_text = self.document_text.lower()
        self.remove_punctuations()
        self.remove_numbers()
        self.remove_apostrophe()
        self.remove_stopwords()

        return self.processed_document_text
