# Import the Libraries
import numpy as np
import matplotlib.pyplot as plt
from parser_data import reader
from sklearn import svm, datasets
from State_temperature import weather

list_confirmed = reader('dataset/covid_19_confirmed.csv')
list_deaths = reader('dataset/covid_19_deaths.csv')

date=list_confirmed[0].dates
for i,row in enumerate(list_confirmed):
    for j,col in enumerate(date):
        if  i>0:
            # print(list_confirmed[i].dates[j])
            # print(list_confirmed[i].country)
            print(list_confirmed[i].lat,list_confirmed[i].long,date[j])
            print(weather(list_confirmed[i].lat,list_confirmed[i].long,date[j]))

# Import some Data from the iris Data Set
# iris = datasets.load_iris()
# # print (iris)
# # Take only the first two features of Data.
# # To avoid the slicing, Two-Dim Dataset can be used
#
# X = iris.data[:, :2]
# # print(X)
# y = iris.target
# # print(y)
#
# # C is the SVM regularization parameter
# C = 1.0
#
# # Create an Instance of SVM and Fit out the data.
# # Data is not scaled so as to be able to plot the support vectors
# svc = svm.SVC(kernel ='linear', C = 1).fit(X, y)
#
# # create a mesh to plot
# x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# h = (x_max / x_min)/100
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
# 		np.arange(y_min, y_max, h))
#
# # Plot the data for Proper Visual Representation
# plt.subplot(1, 1, 1)
#
# # Predict the result by giving Data to the model
# Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)
# plt.contourf(xx, yy, Z, cmap = plt.cm.Paired, alpha = 0.8)
#
# plt.scatter(X[:, 0], X[:, 1], c = y, cmap = plt.cm.Paired)
# plt.xlabel('Sepal length')
# plt.ylabel('Sepal width')
# plt.xlim(xx.min(), xx.max())
# plt.title('SVC with linear kernel')
#
# # Output the Plot
# plt.show()
