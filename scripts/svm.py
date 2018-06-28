import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import time
from load import load
from sklearn import svm,metrics

def supvec():
    inputs,targets = load("../proc_data/data",equalize=False)
    train_split = 0.8

    #Split between train and test
    length = len(inputs)
    split = int(length*train_split)
    inputs_train = inputs[:split]
    targets_train = targets[:split]
    inputs_test = inputs[split:]
    targets_test = targets[split:]

    print length,"total inputs"
    print len(inputs_train),"used for training"
    print len(inputs_test),"used for testing"

    start = time.time()
    clf = svm.SVC(kernel="linear",verbose=False)
    print "Training SVM..."
    clf.fit(inputs_train, targets_train)
    print "Training time:",time.time()-start

    print "Predicting tests..."
    start = time.time()
    targets_predicted = clf.predict(inputs_test)
    print "Classification time:",time.time()-start
    print metrics.classification_report(targets_test, targets_predicted)

    print "Saving classifier to disk..."
    with open("../classifiers/svm","w") as clffile:
        pickle.dump(clf,clffile)
    #drawPlot(clf,inputs_train,targets_train,inputs_test,targets_test)

def drawPlot(clf,X_train,Y_train,X_test,Y_test):
    matplotlib.rcParams.update({'font.size': 24})
    print "draw: length X_train:",len(X_train)
    X_train = np.asarray(X_train)
    Y_train = np.asarray(Y_train)

    print "draw: length X_test:",len(X_test)
    X_test = np.asarray(X_test)
    Y_test = np.asarray(Y_test)
    drawWithData(X_train,Y_train,clf,1,"Train Data")
    drawWithData(X_test,Y_test,clf,2,"Test Data")
    plt.show()

def drawWithData(X,Y,clf,fignum,title):    
    # get the separating hyperplane
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5)
    yy = a * xx - (clf.intercept_[0]) / w[1]

    # plot the parallels to the separating hyperplane that pass through the
    # support vectors (margin away from hyperplane in direction
    # perpendicular to hyperplane). This is sqrt(1+a^2) away vertically in
    # 2-d.
    margin = 1 / np.sqrt(np.sum(clf.coef_ ** 2))
    yy_down = yy - np.sqrt(1 + a ** 2) * margin
    yy_up = yy + np.sqrt(1 + a ** 2) * margin

    # plot the line, the points, and the nearest vectors to the plane
    plt.figure(fignum, figsize=(4, 3))
    plt.clf()
    plt.plot(xx, yy, 'k-')
    plt.plot(xx, yy_down, 'k--')
    plt.plot(xx, yy_up, 'k--')

    plt.scatter(X[:, 0], X[:, 1], c=Y, zorder=10, cmap=plt.cm.Paired,
                edgecolors='k')

    plt.axis('tight')
    x_min = 0.2
    x_max = 0.425
    y_min = 0.3
    y_max = 0.4
    axes = plt.gca()
    axes.set_xlim([x_min,x_max])
    axes.set_ylim([y_min,y_max])

    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.predict(np.c_[XX.ravel(), YY.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(XX.shape)
    plt.figure(fignum, figsize=(4, 3))
    plt.xlabel("neck")
    plt.ylabel("shoulder")
    plt.title(title)

if __name__ == "__main__":
    supvec()