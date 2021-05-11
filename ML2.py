import math
from sklearn.linear_model import LogisticRegression

#declare global variables
global select
global trainDataName
global testDataName
global trainSet
global trainLabel
global testSet
global testLabel
global confusionMatrix


#input/output
def display():
    global select
    global trainDataName
    global testDataName
    print('Which learning algorithm do you want to use?')
    print('1. Logistic Regression')
    print('2. k-NN')

    select = int(input('Enter the number : '))
    trainDataName = input('Enter the file name of training data :')
    testDataName = input('Enter the file name of test data :')

#select algorithm
def selector():
    global select
    if(select == 1):
        logisticRegression()
    elif(select == 2):
        k_NN()
    else:
        print('out of arrange')
        exit(0)

#open test/train dataset
def openText():
   global trainSet
   global trainLabel
   global testSet
   global testLabel
   global trainDataName
   global testDataName

   trainSet = []
   trainLabel = []
   testSet = []
   testLabel =[]

   with open(trainDataName,mode="r") as file:
       while True:
           sentence = file.readline()
           if sentence:
               sentence = sentence.split(',')
               trainSet.append([float(sentence[0]),float(sentence[1]),float(sentence[2])])
               trainLabel.append(int(sentence[3].rstrip('\n')))
           else:
               break

   with open(testDataName, mode="r") as file:
       while True:
           sentence = file.readline()
           if sentence:
               sentence = sentence.split(',')
               testSet.append([float(sentence[0]),float(sentence[1]),float(sentence[2])])
               testLabel.append(int(sentence[3].rstrip('\n')))
           else:
               break

#function to get distance
def euclideanDistance(t1,t2):
    return math.sqrt((t1[0] - t2[0]) ** 2 + (t1[1] - t2[1]) ** 2 + (t1[2] - t2[2])  ** 2)


def logisticRegression():
    global testSet
    global testLabel
    global trainSet
    global trainLabel

    global confusionMatrix
    confusionMatrix = [0, 0, 0, 0]

    #Make logistic regression model
    model = LogisticRegression(penalty='none')

    #Fit a model
    model.fit(testSet,testLabel)

    #Predict Result using testSet
    predictArr = model.predict(testSet)

    print('Model Parameters: ( %.2f, %.2f, %.2f, %.2f)' %(model.coef_[0][0],model.coef_[0][1],model.coef_[0][2],model.C))

    #Calculate Confusion Matrix
    for i in range(len(testLabel)):
        if (testLabel[i] == 1 and predictArr[i] == 1):  # TP
            confusionMatrix[0] += 1
        elif (testLabel[i] == 0 and predictArr[i] == 1):  # FN
            confusionMatrix[1] += 1
        elif (testLabel[i] == 1 and predictArr[i] == 0):  # FP
            confusionMatrix[2] += 1
        elif (testLabel[i] == 0 and predictArr[i] == 0):  # TN
            confusionMatrix[3] += 1



def classifier(arr):
    zeros = 0
    ones = 0
    for i in arr:
        if(arr[i] == 0):
            zeros += 1
        else:
            ones +=1
    if(zeros >= ones):
        return 0
    else:
        return 1


def k_NN():
    k = int(input('Enter value for k:'))

    global confusionMatrix
    confusionMatrix = [0, 0, 0, 0]

    for i in range(len(testSet)):
        # Calculate Distance
        distance = []
        major = []
        for j in range(len(trainSet)):
            distance.append([j,euclideanDistance(testSet[i], trainSet[j])])

        #Sorting by distance
        distance.sort(key = lambda x : x[1])

        #Classifier
        for t in range(k):
           major.append(trainLabel[distance[t][0]])

        #Confusion Matrix 계산
        if(testLabel[i] == 1 and classifier(major) == 1):  #TP
            confusionMatrix[0] += 1
        elif(testLabel[i] == 0 and classifier(major) == 1): #FN
            confusionMatrix[1] += 1
        elif(testLabel[i] == 1 and classifier(major) == 0): #FP
            confusionMatrix[2] += 1
        elif(testLabel[i] == 0 and classifier(major) == 0): #TN
            confusionMatrix[3] += 1

def output():
    global confusionMatrix
    print('TP: {0:3d} \t\t FN: {1:3d} \nFP: {2:3d} \t\t TN: {3:3d}'.format(confusionMatrix[0],confusionMatrix[1],confusionMatrix[2],confusionMatrix[3]))

#메인 함수
def main():
    display()
    openText()
    selector()
    output()

if __name__ == "__main__":
    main()