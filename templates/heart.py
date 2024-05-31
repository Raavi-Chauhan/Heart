import pickle  
import tensorflow
import joblib
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input,Dense
from keras.models import load_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

a = pd.read_csv('heart_disease_health.csv')
y = a['HeartDiseaseorAttack']
x = a.drop(['HeartDiseaseorAttack','PhysActivity','Fruits','Veggies','Education','Income'],axis=1)
X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=40)
sc_x = StandardScaler()
X_train = sc_x.fit_transform(X_train)
X_test = sc_x.transform(X_test)

input_layer = Input(shape=(16,))
Layer_1 = Dense(16, activation="relu")(input_layer)
Layer_2 = Dense(16, activation="relu")(Layer_1)
output_layer= Dense(1, activation="sigmoid")(Layer_2)
##Defining the model by specifying the input and output layers
model = Model(inputs=input_layer, outputs=output_layer)
## defining the optimiser and loss function
model.compile(optimizer='adam',loss='mse')
## training the model
model.fit(X_train, y_train,epochs=100, batch_size=20,validation_data=(X_test,y_test))


#joblib.dump(model, 'predict.joblib')       
model.save('predict.h5')
  
#file2=open('predict.p','wb')
#pickle.dump(model,file2)
#file2.close()
#joblib.dump(model, 'predict.joblib')        
#file2=open('predict.p','wb')
#pickle.dump(model,file2)
#file2.close()
