import pickle
import tarfile 
import pandas as pd
from flask import Flask, render_template, request
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB

import tensorflow 
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.models import Model, Sequential, load_model


#from tensorflow import keras
#from keras.layers import Dense
#from keras.layers import Input
#from keras.models import Model

#from keras.models import Sequential, load_model

app = Flask(__name__)

@app.route('/', methods = ['get'])
def hello_world():
    error_message = None
    Result = None
    return render_template('index.html')


@app.route('/', methods=['post'])
def predict():
    error_message = None
    Result = None
    Name = request.form['name']
    Age = int(request.form['age'])
    Sex = int(request.form['sex'])
    BP = int(request.form['BP'])
    Cholesterol = int(request.form['cholesterol'])
    Cholesterol_check = int(request.form['cholchk'])
    Smoker = int(request.form['smoker'])
    Stroke = int(request.form['stroke'])
    Alcohol = int(request.form['alcohol'])
    Health_Care_Scheme = int(request.form['HCS'])
    Not_Consulted = int(request.form['NCTD'])
    Difficulty_Walk = int(request.form['walk'])
    BMI = int(request.form['BMI'])
    Diabetes = int(request.form['diabetes'])
    Gerenal_Health = int(request.form['GH'])
    Mental_Health = int(request.form['MH'])
    Physical_Health = int(request.form['PH'])

    if BMI<0:
        error_message='Please Enter a valid BMI'
        Result = None
    else:
        #a = pd.read_csv('heart_disease_health.csv')
        #y = a['HeartDiseaseorAttack']
        #x = a.drop(['HeartDiseaseorAttack','PhysActivity','Fruits','Veggies','Education','Income'],axis=1)
       # X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=40)
        #sc_x = StandardScaler()
        #X_train = sc_x.fit_transform(X_train)
        #X_test = sc_x.transform(X_test)

        #input_layer = Input(shape=(16,))
       # Layer_1 = Dense(16, activation="relu")(input_layer)
       # Layer_2 = Dense(16, activation="relu")(Layer_1)
        #output_layer= Dense(1, activation="sigmoid")(Layer_2)
        ##Defining the model by specifying the input and output layers
       # model = Model(inputs=input_layer, outputs=output_layer)
        ## defining the optimiser and loss function
        #model.compile(optimizer='adam',loss='mse')
        ## training the model
        #model.fit(X_train, y_train,epochs=11, batch_size=200,validation_data=(X_test,y_test))
        
        #file="Heart Wise"
       # pickle.dump(model,open(file,'wb'))
       # file.close()
        #loaded=pickle.load(open(file,'rb'))

        file1=open('./predict.p','rb+')
        loaded=pickle.load(file1)
        file1.close()

        y_pred = loaded.predict([[BP, Cholesterol, Cholesterol_check, BMI, Smoker, Stroke, Diabetes, Alcohol, Health_Care_Scheme, Not_Consulted, Gerenal_Health, Mental_Health, Physical_Health, Difficulty_Walk, Sex, Age]])
        print(y_pred[0][0])

        if y_pred>0.4:
            Result = Name+', You may have high chances of having Heart Attack. I recommend you to Consult to a doctor'
        else:
            Result = Name+', You may have low chances of having Heart Attack. Stay Healthy and take proper diet.'
    # print("1:",Name)
    # print("2:",Age)
    # print("3:",Sex)
    # print("4:",BP)
    # print("5:",Cholesterol)
    # print("6:",Cholesterol_check)
    # print("7:",Smoker)
    # print("8:",Stroke)
    # print("9:",Alcohol)
    # print("10:",Health_Care_Scheme)
    # print("11:",Not_Consulted)
    # print("12:",Difficulty_Walk)
    # print("13:",BMI)
    # print("14:",Diabetes)
    # print("15:",Gerenal_Health)
    # print("16:",Mental_Health)
    # print("17:",Physical_Health)


    return render_template('index.html', result = Result, error = error_message)


if __name__ == '__main__':
    app.run(port=3000, debug=True,host='0.0.0.0')
