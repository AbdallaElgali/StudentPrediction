import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
from termcolor import cprint

data = pd.read_csv(r"C:\Users\scorp\Desktop\Programmin\Python\Python Projects\MachineLearning\LinearRegression\data\student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "absences", "failures"]]

max_studytime = data['studytime'].max()
predict = "G3"

x = np.array(data.drop(predict, axis=1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x , y, test_size = 0.1)



best = 0

for _ in range(10000):

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x , y, test_size = 0.1)
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train) # Finding bestfit line
    accuracy = float(linear.score(x_test, y_test))


    if accuracy > best:
        best = accuracy
        with open("studentmodelBest.pickle", "wb") as model:
            pickle.dump(linear, model)

print(best*100)

pickle_in = open("studentmodelBest.pickle", "rb")
linear = pickle.load(pickle_in)

predictions = linear.predict(x_test)

for x in range(len(predictions)):
    cprint(f'Actual: {y_test[x]}', 'yellow')
    if y_test[x]-3<=int(predictions[x])<=y_test[x]+3:
        cprint(f'Predicted: {predictions[x]}', 'green')
    else:
        cprint(predictions[x], 'red')


print("Coefficient: \n", linear.coef_)
print("Intercept: \n", linear.intercept_)


# Input to find the predicted grade of a student given the input parameters
def predict_inp():
    q = input('First Grade, Second Grade, study time, absences, failures: ')
    ql = q.split(',')
    qn = np.array(ql, dtype=float).reshape(1, -1)
    predictions = linear.predict(qn)
    print('Predicted G3: ', predictions)

predict_inp()
# Plot a graph of the data with the best fit line
p = 'G1'

# Plot a line to the graph
theta = np.polyfit(data[p], y, 1)
print(f'Parameters of the line {theta}')
y_line = theta[1] + theta[0]*data[p]
# Plot the graph
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.plot(data[p], y_line, 'b')
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()  # To show the graph
