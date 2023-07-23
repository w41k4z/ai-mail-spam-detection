import pandas as pd
import numpy as np
from tf_idf import TF_IDF

training_data = pd.read_excel('./training-data/data.xlsx', header=None).values.tolist()
x_data = [row[0] for row in training_data[1:]]
y_data = [row[1] for row in training_data[1:]]

# data from database here

processed_x_data = []
tf_idf = TF_IDF(x_data)
for document in tf_idf.documents:
    processed_x_data.append(tf_idf.tf_idf(document))

from sklearn.linear_model import LogisticRegression
spam_model = LogisticRegression()
spam_model.fit(processed_x_data, y_data)

from joblib import dump
dump(spam_model, './model/spam_model.joblib')
dump(tf_idf, './model/tf_idf.joblib')