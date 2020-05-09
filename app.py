from flask import Flask, render_template, request, session, url_for, redirect, jsonify
import pymysql
#===============================================
import pickle
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
#import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

# %matplotlib inline
df=pd.read_csv('lymphography.csv', delimiter=',',nrows=25,skiprows=[1])
df_cancer =df


# Pick the best combination of parameters



X = df_cancer.drop(['class'], axis = 1) # We drop our "target" feature and use all the remaining features in our dataframe to train the model.
X.head()
y = df_cancer['class']
y.head()

scaler = StandardScaler()
#X_std = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state =20)
ann_clf = MLPClassifier()
acc_scorer = make_scorer(accuracy_score)

# Run grid search
parameters = {'solver': ['lbfgs'],
             'alpha':[1e-2],
             'hidden_layer_sizes':(9,14,14,2),   # 9 input, 14-14 neuron in 2 layers,1 output layer
             'random_state': [1]}
grid_obj = GridSearchCV(ann_clf, parameters, scoring=acc_scorer)
grid_obj = grid_obj.fit(X_train, y_train)
ann_clf = grid_obj.best_estimator_
ann_clf.fit(X_train, y_train)
y_pred_ann = ann_clf.predict(X_test)
filename1 = 'ann.sav'
pickle.dump(ann_clf, open(filename1, 'wb'))
svclassifierlinear = SVC(kernel='linear')
svclassifierlinear.fit(X_train,y_train)
y_pred=svclassifierlinear.predict(X_test)
accuracy_score(y_test,y_pred)
filename = 'linear_svm_model.sav'
pickle.dump(svclassifierlinear, open(filename, 'wb'))
class_obt={2:'Metastates',3:'malign lymph'}


loaded_model = pickle.load(open(filename, 'rb'))
y_gotdata=loaded_model.predict(np.array(X_test.iloc[4:5]))
y_gotdata
#class_obt.get(y_gotdata[0])

#=================================================



app = Flask(__name__)
app.secret_key = 'random string'


#Database Connection
def dbConnection():
    connection = pymysql.connect(host="localhost", user="root", password="root", database="9cancerdiseaseprediction")
    return connection


#close DB connection
def dbClose():
    dbConnection().close()
    return


#default welcome page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    if 'user' in session:
        return render_template('home.html',user=session['user'])
    return redirect(url_for('index'))


#logout code
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))


#login code
@app.route('/login', methods=["GET","POST"])
def login():
    msg = ''
    if request.method == "POST":
        #session.pop('user',None)
        mobno = request.form.get("mobno")
        password = request.form.get("pas")
        #print(mobno+password)
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute('SELECT * FROM userdetails WHERE mobile = %s AND password = %s', (mobno, password))
        #a= 'SELECT * FROM userdetails WHERE mobile ='+mobno+'  AND password = '+ password
        #print(a)
        #result_count=cursor.execute(a)
        # result = cursor.fetchone()
        if result_count>0:
            print(result_count)
            session['user'] = mobno
            return redirect(url_for('home'))
        else:
            print(result_count)
            msg = 'Incorrect username/password!'
            return msg
        #dbClose()
    return redirect(url_for('index'))


#user register code
@app.route('/userRegister', methods=["GET","POST"])
def userRegister():
    if request.method == "POST":
        try:
            status=""
            name = request.form.get("name")
            address = request.form.get("address")
            mailid = request.form.get("mailid")
            mobile = request.form.get("mobile")
            pass1 = request.form.get("pass1")

            con = dbConnection()
            cursor = con.cursor()
            cursor.execute('SELECT * FROM userdetails WHERE mobile = %s', (mobile))
            res = cursor.fetchone()
            if not res:
                sql = "INSERT INTO userdetails (name, address, email, mobile, password) VALUES (%s, %s, %s, %s, %s)"
                val = (name, address, mailid, mobile, pass1)
                cursor.execute(sql, val)
                con.commit()
                status= "success"
                return redirect(url_for('index'))
            else:
                status = "Already available"
            return status
        except:
            print("Exception occured at user registration")
            return redirect(url_for('index'))
        finally:
            dbClose()
    return redirect(url_for('index'))


@app.route('/questions', methods=["GET","POST"])
def questions():
    if 'user' in session:
        if request.method == "POST":
            v1 = request.form.get("para1")
            v2 = request.form.get("para2")
            v3 = request.form.get("para3")
            v4 = request.form.get("para4")
            v5 = request.form.get("para5")
            v6 = request.form.get("para6")
            v7 = request.form.get("para7")
            v8 = request.form.get("para8")
            v9 = request.form.get("para9")
            v10 = request.form.get("para10")
            v11 = request.form.get("para11")
            v12 = request.form.get("para12")
            v13 = request.form.get("para13")
            v14 = request.form.get("para14")
            v15 = request.form.get("para15")
            v16 = request.form.get("para16")
            v17 = request.form.get("para17")
            v18 = request.form.get("para18")

            test_list = []
            valofall = v1 + ',' + v2 + ',' + v3 + ',' + v4 + ',' + v5 + ',' + v6 + ',' + v7 + ',' + v8 + ',' + v9 + ',' + v10 + ',' + v11 + ',' + v12 + ',' + v13 + ',' + v14 + ',' + v15 + ',' + v16 + ',' + v17 + ',' + v18
            print(valofall)
            valofsplit = valofall.split(",")
            print(valofsplit)
            for i in range(0, len(valofsplit)):
                test_list.append(int(valofsplit[i]))
                # print(test_list)
            # X_std = scaler.fit_transform(X)
            print(test_list)
            print(np.array([test_list]))
            loaded_model = pickle.load(open(filename1, 'rb'))
            y_gotdata = loaded_model.predict(np.array([test_list]))
            print(y_gotdata[0])
            print("predicted cancer is " + class_obt.get(y_gotdata[0]))
            result = class_obt.get(y_gotdata[0])
        #    l.config(text="predicted cancer is " + class_obt.get(y_gotdata[0]))
            return render_template('predictresult.html',user=session['user'],result=result)
        return render_template('questions.html',user=session['user'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run("0.0.0.0")

