import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
data=pd.read_csv('Crop_recommendation.csv')
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
le = LabelEncoder()
y =  le.fit_transform(y)
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=0.2,random_state=0)
rfc=RandomForestClassifier(n_estimators=100,criterion='entropy')
rfc.fit(x_train,y_train)
pickle.dump(rfc,open('model.pkl','wb'))


