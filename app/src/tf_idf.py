import numpy as np
from nltk.corpus import stopwords
import string


class TF_IDF:

    def __init__(self, corpus: list[str]) -> None:
        self.documents = []
        self.words = []
        self.words_corpus_occurence = {}
        # document pre-processing
        for document in corpus:
            document = TF_IDF.text_preprocessing(document)
            self.documents.append(document)
            for word in document.split():
                # tf-idf matrix limited to 500 columns
                if len(self.words) == 500:
                    break
                if word not in self.words:
                    self.words.append(word)
        # word occurence in corpus
        for word in self.words:
            self.words_corpus_occurence[word] = 0
            for document in self.documents:
                if word in document:
                    self.words_corpus_occurence[word] += 1
    
    # without stemming
    @staticmethod
    def text_preprocessing(text: str):
        # punctuation removal
        text = text.translate(str.maketrans('', '', string.punctuation))
        # stopwords filtering
        text = [word.lower() for word in text.split() if word.lower()
                not in stopwords.words('french') and word.lower().isalpha()]
        return " ".join(text)

    @staticmethod
    def term_frequency(word: str, document: str):
        # python str.count('word') method counts overlapping words
        freq = len([w for w in document.split() if w == word])
        return np.log(1 + freq)
    
    @staticmethod
    def inverse_document_frequency(word, total_documents: int, corpus_word_count: dict):
        try:
            word_occurence = corpus_word_count[word]
        except KeyError:
            word_occurence = 1
        return np.log(total_documents / word_occurence)
    
    def tf_idf(self, document: str):
        tf_idf_vect = np.zeros((len(self.words),))
        
        index = 0
        for word in self.words:
            tf = TF_IDF.term_frequency(word, document)
            idf = TF_IDF.inverse_document_frequency(word, len(self.documents), self.words_corpus_occurence)
            tf_idf_vect[index] = tf * idf
            index += 1
        return tf_idf_vect

# test = ["Ceci n'est pas un mail spam. S'il vous plait, repondez a cette derniere", "Bonjour, un nouveau mail en attente de votre reponse"]
# tf_idf = TF_IDF(test)
# print(tf_idf.tf_idf(tf_idf.documents[0]))