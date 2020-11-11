import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,recall_score,precision_score,roc_auc_score,f1_score
from sklearn.metrics import roc_curve
from sklearn.preprocessing import StandardScaler
states = 40;
pbl_data = pd.read_csv("uci-secom.csv",sep=',')
X = pd.DataFrame()
X_temp = pd.DataFrame()
X = pbl_data[['4','490','Pass/Fail']]
X = X.dropna(axis =0)
X = X.reset_index()
y = X['Pass/Fail']
X =X.drop('Pass/Fail',axis=1)
SS = StandardScaler()
SS.fit(X)
X = SS.transform(X)
log_reg = LogisticRegression(random_state=states,solver='liblinear',C=10.)
X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state = states)
if len(pd.value_counts(y_test.values, sort=False))==2 and len(pd.value_counts(y_train.values, sort=False)) ==2 :
	print (pd.value_counts(y_test.values, sort=False))
	print (pd.value_counts(y_train.values, sort=False))
	log_reg.fit(X_train,y_train)
	print (log_reg.predict_proba(X_test)[:,1])
	pred = log_reg.predict(X_test)
	print (pd.value_counts(pred, sort=False))
	print ("accuracy_score : ")
	print (accuracy_score(y_test,pred))
	print ("recall_score : ")
	print (recall_score(y_test,pred, average="weighted",zero_division=1))
	print ("f1_score : ")
	print (f1_score(y_test,pred, average="weighted",zero_division=1))
	print ("roc_auc_score : ")
	print (roc_auc_score(y_test,log_reg.decision_function(X_test), average='weighted'))