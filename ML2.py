#전역변수 선언
global select
global trainDataName
global testDataName
global x_train
global y_train
global z_train
global label_train
global x_test
global y_test
global z_test
global label_test



#입출력 구현
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

def selector():
    global select
    if(select == 1):
        logisticRegression()
    elif(select == 2):
        k_NN()
    else:
        print('out of arrange')
        exit(0)

def openText():
   global x_train; global y_train; global z_train
   global x_test ; global y_test;  global z_test
   global label_train; global label_test

   global trainDataName
   global testDataName

   x_train = []; y_train = [];z_train = []
   x_test = [];  y_test = []; z_test = []
   label_train =[] ; label_test=[]


   with open(trainDataName,mode="r") as file:
       while True:
           sentence = file.readline()
           if sentence:
               sentence = sentence.split(',')
               x_train.append(float(sentence[0]))
               y_train.append(float(sentence[1]))
               z_train.append(float(sentence[2]))
               label_train.append(int(sentence[3].rstrip('\n')))
           else:
               break

   with open(testDataName, mode="r") as file:
       while True:
           sentence = file.readline()
           if sentence:
               sentence = sentence.split(',')
               x_test.append(float(sentence[0]))
               y_test.append(float(sentence[1]))
               z_test.append(float(sentence[2]))
               label_test.append(int(sentence[3].rstrip('\n')))
           else:
               break


def logisticRegression():
    return

def k_NN():
    k = int(input('Enter value for k:'))
    return

def output(TP,FN,FP,TN):
    print('TP: {0:3d} \t\t FN: {1:3d} \nFP: {2:3d} \t\t TN: {3:3d}'.format(TP,FN,FP,TN))
    return

#메인 함수
def main():
    display()
    openText()
    selector()

    global label_test
    print(label_test)


if __name__ == "__main__":
    main()