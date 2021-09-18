# -*- coding: utf-8 -*-
"""Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iYhXBCCf7FCXiWBRxSUY32Eh6MxarVHm

**Name- Rucha Ravindra Ratnaparkhi**

TSF Internship Data Science and Business Analytics

**Task 1: Prediction using supervised ML** :
Predicting the percentage of a student based on the number of study hours and predicting the score if a student studies for 9.25 hours/day.

**Importing required libraries**
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Loading the dataset
url= "http://bit.ly/w-data"
data=pd.read_csv(url)
data.head(10)

data.describe()

"""**Visualizing dataset**


"""

#Plotting the distribution of scores
data.plot(x="Hours",y="Scores",style='o')
plt.title("Hours vs Scores")
plt.xlabel('No. of Hours studied')
plt.ylabel('Scores')
plt.show()

"""*From the above graph,we can see that there is a positive linear regression between hours and score.*

**Preparing the Data**
"""

#dividing data into "attributes"(inputs) & "labels"(outputs)
x=data.iloc[:,:-1].values
y=data.iloc[:,1].values

#splitting the data into training and test sets
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

"""**Training the Algorithm**"""

from sklearn.linear_model import LinearRegression
regr = LinearRegression()
regr.fit(x_train,y_train)

print("Training completed successfully")

#Plotting the regression line
line=regr.coef_*x+regr.intercept_
plt.scatter(x,y)
plt.plot(x,line)
plt.show()

"""**Making Predictions**"""

print(x_test)

#predicting the scores
y_predicted=regr.predict(x_test)
print(regr.predict(x_test))

d=[x_test,y_test,y_predicted]
d

"""**Comparing Actual and predicted scores**"""

df=pd.DataFrame({"Actual Value":y_test,"Predicted Value":y_predicted})
df

#Predicting Score if a student studies for 9.25 hours/day
Study_hours= 9.25
predicted_score= regr.predict([[Study_hours]])
print("Number of Hours= {}".format(Study_hours))
print("Predicted Score: {}".format(predicted_score[0]))

print("If a student studies for 9.25 hours/day , his score would be:",predicted_score)

"""**Evaluating the Model**"""

from sklearn import metrics
print('Mean Absolute Error:',metrics.mean_absolute_error(y_test,y_predicted))
