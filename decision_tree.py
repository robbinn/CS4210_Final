# importing some Python libraries
from sklearn import tree
import csv

db = []

amount_range = []
for i in range(0, 1000000, 2000):
    amount_range.append(i)

with open('Training_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        temp = []
        if i > 0:  # skipping the header
            db.append(row[1:])

dict = {"Male": 1, "Female": 2,
        "No": 1, "Yes": 2,
        "0d": 1, "1d": 2, "2d": 3, "3d": 4, "4d": 5,
        "Graduate": 1, "Not Graduate": 2,
        "360m": 1, "240m": 2, "180m": 3, "120m": 4, "480m": 5, "60m": 6, "84m": 7, "36m": 8, "12m": 9, "300m": 10,
        "0": 1, "1": 2,
        "Urban": 1, "Rural": 2, "Semiurban": 3,
        "N": 1, "Y": 2,
        }

X = []
for row in db:
    temp = []
    for i in range(len(row) - 1):  # skipping the last column
        if i == 5 or i == 6:
            for k in range(len(amount_range) - 1):
                if int(row[i]) <= amount_range[k]:
                    temp.append(1)
                    break
                if amount_range[k] <= int(row[i]) <= amount_range[k + 1]:
                    temp.append(k + 1)
                    break
        else:
            temp.append(dict.get(row[i]))
    X.append(temp)

# transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
Y = []
for row in db:
    Y.append(dict.get(row[len(row) - 1]))

# for i in range(len(X)):
#     print(i+2,X[i])
# fitting the naive bayes to the data
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)

# reading the data in a csv file
dbTest = []  # String version
with open('Test_Loan_Home.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            dbTest.append(row[1:len(row)])  # Skipping the last column -- question mark

dbTestNum = []
for row in dbTest:
    temp = []
    for i in range(len(row)):
        if i == 5 or i == 6:
            for k in range(len(amount_range) - 1):
                if int(row[i]) <= amount_range[k]:
                    temp.append(1)
                    break
                if amount_range[k] <= int(row[i]) <= amount_range[k + 1]:
                    temp.append(k + 1)
                    break
        else:
            temp.append(dict.get(row[i]))
    dbTestNum.append(temp)

class_predicted = clf.predict(dbTestNum)

# 2 - Yes, 1 - No.
print(class_predicted)
