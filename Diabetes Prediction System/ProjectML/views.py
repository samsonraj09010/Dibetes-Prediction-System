# code 
from django.shortcuts import render 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.core.interchange import column
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# for call home.html
def home(request):
	return render(request, 'home.html')

# for call predict.html
def predict(request):
	return render(request, 'predict.html')

# for display result on same page
def result(request):
	dataset = pd.read_csv(r"C:\Users\KIIT\Downloads\Compressed\archive\diabetes.csv")



	X = dataset.drop("Outcome", axis=1)
	Y = dataset['Outcome']

	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

	model = LogisticRegression()
	model.fit(X_train, Y_train)

	val1 = float(request.GET['n1']) 
	val2 = float(request.GET['n2']) 
	val3 = float(request.GET['n3']) 
	val4 = float(request.GET['n4']) 
	val5 = float(request.GET['n5']) 
	val6 = float(request.GET['n6']) 
	val7 = float(request.GET['n7']) 
	val8 = float(request.GET['n8']) 

	pred = model.predict([[val1, val2, val3, 
						val4, val5, val6, val7, val8]]) 

	result1 = "" 
	if pred == [1]: 
		result1 = "You have DIABETES BUDDY. 🥲🥲"
	else: 
		result1 = " You DON'T have diabetes BUDDY 👍👍."

	return render(request, "predict.html", {"result2": result1}) 

