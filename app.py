# from flask import Flask, render_template, request, redirect, url_for

import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import re
import string

data_fake = pd.read_csv('D:/BANASTHALI VIDYAPITH/Inhouse project/fake1.csv')
data_true = pd.read_csv('D:/BANASTHALI VIDYAPITH/Inhouse project/true1.csv')
data_fake.head()
data_true.head()

data_fake['class'] = 0
data_true['class'] = 1

data_fake_manual_testing = data_fake.tail(10)
for i in range(98, 88,-1): 
    data_fake.drop([i], axis = 0, inplace = True)

data_true_manual_testing = data_true.tail(10) 
for i in range(98, 88,-1):
    data_true.drop([i], axis = 0, inplace = True)

data_fake_manual_testing['class'] = 0
data_true_manual_testing['class'] = 1

data_merge = pd.concat([data_fake, data_true], axis = 0) 
data_merge.head(10)

data = data_merge.drop(['Title', 'Subject'], axis = 1)

def wordopt(Text):
    Text=Text.lower()
    Text=re.sub('\[.*?\]','',Text)
    Text=re.sub("\\W","",Text)
    Text=re.sub('https?://\S+|www\.\S+','',Text)
    Text=re.sub('<.*?>+','',Text)
    Text=re.sub('[%s]'%re.escape(string.punctuation),'',Text)
    Text=re.sub('\n','',Text)
    Text=re.sub('\w*\d\w*','',Text)
    return Text

data['Text'] = data['Text'].apply(wordopt)

x = data['Text']
y = data['class']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)

from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(xv_train, y_train)

pred_lr = LR.predict(xv_test)
LR.score(xv_test, y_test)
print(classification_report(y_test, pred_lr))

from sklearn.tree import DecisionTreeClassifier
DT = DecisionTreeClassifier()
DT.fit(xv_train, y_train)

pred_dt = DT.predict(xv_test)
DT.score(xv_test, y_test)
print(classification_report(y_test, pred_dt))

def output_lable(n):
    if n == 0:
        return "Fake Fact"
    elif n == 1:
        return "True Fact"
def manual_testing(Fact):
    testing_news = {"Text":[Fact]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["Text"] = new_def_test["Text"].apply(wordopt)
    new_x_test= new_def_test["Text"]
    new_xv_test =vectorization.transform(new_x_test)
    pred_LR =LR.predict(new_xv_test)
    pred_DT= DT.predict(new_xv_test)
    lr_prediction = output_lable(pred_LR[0])
    dt_prediction = output_lable(pred_DT[0])

    print("Input Fact:", Fact)
    print("Processed Text:", new_x_test)
    print(lr_prediction)
    
    return f"\n\n{lr_prediction}"
Fact = str(input())


# app = Flask(__name__)
# app = Flask(__name__, template_folder='templates')

# @app.route('/')
# def index():
#     return render_template("fake_fact_detection.html")

# @app.route('/detect_fake_fact', methods=['POST'])
# def detect_fake_fact():
#     if request.method == 'POST':
#         fact = request.form['fact_input']
#         result = manual_testing(fact)
#         return render_template("output.html", result=result)
#     return render_template("output.html")

# @app.route('/output')
# def output():
#     result = request.args.get('result')
#     return render_template("output.html", result=result)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return render_template("qqq.html")

@app.route('/explore')
def explore():
    return render_template("explore.html")

@app.route('/fake_fact_detection')
def fake_fact_detection():
    return render_template("fake_fact_detection.html")

@app.route('/detect_fake_fact', methods=['POST'])
def detect_fake_fact():
    if request.method == 'POST':
        fact = request.form['fact_input']
        # Perform your fake fact detection process here
        result = manual_testing(fact)  # Replace this with your actual result
        return render_template("output.html", result=result)
    return render_template("output.html")

@app.route('/get_new_facts')
def get_new_facts():
    data = pd.read_excel('D:/BANASTHALI VIDYAPITH/Inhouse project/true1.xlsx', engine='openpyxl')
    # # Convert the data to a list of dictionaries
    # new_facts = data.sample(n=10)['Text'].tolist()
    # return jsonify({'facts': new_facts})
    new_facts = data.sample(n=10)['Text'].tolist()
    return jsonify({'facts': new_facts})

if __name__ == '__main__':
    app.run(debug=True)
