from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import string

def text_preprocess(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word.lower() not in  stopwords.words('french')]
    return " ".join(text)

vectorizer = TfidfVectorizer(stop_words=stopwords.words('french'))
message_mat = vectorizer.fit_transform(["Ceci n'est pas un mail spam. S'il vous plait, repondez a cette derniere", "Bonjour, un nouveau mail en attente de votre reponse"])
print(vectorizer.get_feature_names_out())
print(message_mat.toarray()[0])