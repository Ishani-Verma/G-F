from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import re
import string

app = Flask(__name__)

# Load and preprocess data
data_fake = pd.read_csv('D:/BANASTHALI VIDYAPITH/Inhouse project/FakeFinal.csv')
data_true = pd.read_csv('D:/BANASTHALI VIDYAPITH/Inhouse project/TrueFinal.csv')


data_fake["class"] = 0
data_true['class'] = 1



data_fake_manual_testing=data_fake.tail(10)
for i in range (20,10,-1):
    data_fake.drop([i],axis=0,inplace=True)
data_true_manual_testing=data_true.tail(10)
for i in range (20,10,-1):
    data_true.drop([i],axis=0,inplace=True)
    
data_fake_manual_testing['class'] = 0
data_true_manual_testing['class'] = 1

data_merge = pd.concat([data_fake, data_true], axis=0)
data = data_merge.drop(['Title', 'Subject', 'Date'], axis=1)

def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W","", text)
    text = re.sub('https?://\S+|www\.\S+','', text)
    text = re.sub('<.*?>+','', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n','', text)
    text = re.sub('\w*\d\w*','', text)
    return text

data['Text'] = data['Text'].apply(wordopt)

x = data['Text']
y = data['class']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25)
#xv = TfidfVectorizer()
#xv.fit(x)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)


from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(xv_train, y_train)
#xv_train = xv.transform(x)

# LR = LogisticRegression()
# LR.fit(xv_train, y)

pred_lr = LR.predict(xv_test)
LR.score(xv_test, y_test)
print(classification_report(y_test, pred_lr))

#DT = DecisionTreeClassifier()
#DT.fit(xv_train, y)

from sklearn.tree import DecisionTreeClassifier
DT = DecisionTreeClassifier()
DT.fit(xv_train, y_train)

pred_dt = DT.predict(xv_test)
DT.score(xv_test, y_test)
print(classification_report(y_test, pred_dt))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
# def output_label(n):
#     if n == 0:
#         return "Fake Fact"
#     elif n == 1:
#         return "True Fact"
# def predict():
#     news_text = request.form['news_text']
#     testing_news = {"Text": [news_text]}
#     new_def_test = pd.DataFrame(testing_news)
#     new_def_test["Text"] = new_def_test["Text"].apply(wordopt)
#     new_x_test = new_def_test["Text"]
#     #new_xv_test = xv.transform(new_x_test)
#     new_xv_test = vectorization.transform(new_x_test)
#     pred_LR = LR.predict(new_xv_test)
#     pred_DT = DT.predict(new_xv_test)
#     return jsonify({'LR_prediction': output_label(pred_LR[0]), 'DT_prediction': output_label(pred_DT[0])})
def predict():
    @app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            news_text = request.form['news_text']
            
            # Preprocess the input text
            preprocessed_text = wordopt(news_text)
            
            # Use the TfidfVectorizer to transform the input text
            new_xv_test = vectorization.transform([preprocessed_text])
            
            # Make predictions
            pred_LR = LR.predict(new_xv_test)
            pred_DT = DT.predict(new_xv_test)
            
            # Return the predictions as JSON
            return jsonify({'LR_prediction': int(pred_LR[0]), 'DT_prediction': int(pred_DT[0])})
        except Exception as e:
            return jsonify({'error': str(e)})
    catch(error => console.error('Error:', error));
    #     news_text = request.form['news_text']
    #     print(f"Received text: {news_text}")
    #     return jsonify({'message': 'Data received successfully'})
    # news_text = request.form['news_text']
    # testing_news = {"Text": [news_text]}
    # new_def_test = pd.DataFrame(testing_news)
    # new_def_test["Text"] = new_def_test["Text"].apply(wordopt)
    # new_x_test = new_def_test["Text"]
    # new_xv_test = vectorization.transform(new_x_test)
    # pred_LR = LR.predict(new_xv_test)
    # pred_DT = DT.predict(new_xv_test)
    # return jsonify({'LR_prediction': "Fake Fact" if pred_LR[0] == 0 else "True Fact",
    #                 'DT_prediction': "Fake Fact" if pred_DT[0] == 0 else "True Fact"})


# def output_label(n):
#     if n == 0:
#         return "Fake Fact"
#     elif n == 1:
#         return "True Fact"

if __name__ == '__main__':
    app.run(debug=True)
