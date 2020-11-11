import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,recall_score,precision_score,roc_auc_score,f1_score
from sklearn.metrics import roc_curve
pbl_data = pd.read_csv("uci-secom.csv",sep=',')
file = open("result_data_2.txt","w")
msg = ""
states = 40
features = 589
maxlen = 3
minlen = 2
case = []
for i in range(1,minlen) :
  case.append(0)
for i in range(minlen,maxlen) :
  case.append(0)
  for j in range(0,len(case)) :
    case[j] = j
  while True :
    X = pd.DataFrame()
    X['Pass/Fail'] = pbl_data['Pass/Fail']
    for v in range(0,len(case)) :
      X[str(case[v])] = pbl_data[str(case[v])]
    X = X.dropna(axis =0)
    X = X.reset_index()
    y = X['Pass/Fail']
    X =X.drop('Pass/Fail',axis=1)
    print (case)
    msg = str(i)
    msg += ' : [ '
    for v in range(0,len(case)-1) :
      msg += str(case[v])
      msg += ' '
    msg += str(case[len(case)-1])
    msg += ' ] '
    if len((X.index)) > 50  and len(pd.value_counts(y.values, sort=False)) == 2 : 
      X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2,random_state = states)
      if len(pd.value_counts(y_train.values, sort=False)) == 2  and len(pd.value_counts(y_test.values, sort=False)) == 2 and pd.value_counts(y_test.values, sort=False)[1] > 10 : 
	      log_reg = LogisticRegression(random_state=states,solver='liblinear',C=10.)
	      log_reg.fit(X_train,y_train)
	      pred = log_reg.predict(X_test)
	      if accuracy_score(y_test,pred) != 1 :
	        msg += " accuracy : "
	        msg += str(accuracy_score(y_test,pred))
	        msg += ", recall : "
	        msg += str(recall_score(y_test,pred, average="weighted",zero_division=1))
	        msg += ", precision : "
	        msg += str(precision_score(y_test,pred, average="weighted",zero_division=1))
	        msg += ", f1 : "
	        msg += str(f1_score(y_test,pred, average="weighted",zero_division=1))
	        msg += ", roc_auc : "
	        msg += str(roc_auc_score(y_test,log_reg.predict_proba(X_test)[:,1], average='weighted'))
	        msg += '\n'
	        file.write(msg)
    end = 0;
    for k in range(0,len(case)) :
      if case[k] == features - len(case) + k :
        end = end +1
    if end == len(case) :
      break
    case[len(case)-1] = case[len(case)-1] +1
    if case[len(case)-1] > features -1 :
      for t in range(len(case)-1,0,-1):
        case[t] = case[t] +1
        if case[t] < features-1 :
          for u in range(t+1,len(case)) :
            case[u] = case[u-1] +1
          break
        else :
          if t==1 :
            case[0] = case[0] +1
            for u in range(1,len(case)) :
              case[u] = case[u-1] +1
              