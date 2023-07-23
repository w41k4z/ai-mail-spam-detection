from joblib import load

class SpamRecognition:

    def __init__(self):
        self.model = load('./model/spam_model.joblib')
        self.tf_idf = load('./model/tf_idf.joblib')

    def predict(self, mail: str):
        mail = self.tf_idf.tf_idf(self.tf_idf.text_preprocessing(mail))
        result = self.model.predict([mail])[0]
        return 'spam' if result == 1 else 'ham'

mail = 'Merci a votre famille pour votre visite chez nous. Nous tenons a vous remercier.'
spam_recognition = SpamRecognition()
print(spam_recognition.predict(mail))