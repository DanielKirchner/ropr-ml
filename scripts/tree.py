import random
import sys
import pickle
import numpy as np
from sklearn import metrics,tree
from load import load
import graphviz
import matplotlib.pyplot as plt
import matplotlib
import time

pltindex = 0
matplotlib.rcParams.update({'font.size': 24})

def dectree():
    inputs,targets = load("../proc_data/data",equalize=False,shuffle=True)
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
    clf = tree.DecisionTreeClassifier(criterion="entropy",max_depth=6,random_state=42)
    print "Training Tree..."
    clf.fit(inputs_train, targets_train)
    print "Training time:",time.time()-start

    print "Predicting tests..."
    start = time.time()
    targets_predicted = clf.predict(inputs_test)
    print "Classification time:",time.time()-start
    print metrics.classification_report(targets_test, targets_predicted)
    

    print "Saving classifier to disk..."
    with open("../classifiers/tree","w") as clffile:
        pickle.dump(clf,clffile)

    #drawTree(clf)
    #plotData()

def drawTree(clf):
    with open("../proc_data/featureNames") as featureNames:
        line = featureNames.readline()

    features = line.split(";")
    features = features[:2]
    
    dot_data = tree.export_graphviz(clf, out_file=None,feature_names=features) 
    graph = graphviz.Source(dot_data) 
    graph.render(view=True)
    
def scatterFeature(feature_arr,name,nrGroups):
    global pltindex
    plt.figure(pltindex)
    pltindex += 1
    colors = ["red","green","gray","blue"]
    items_per_group = len(feature_arr)/nrGroups
    chunks = [feature_arr[x:x+items_per_group] for x in xrange(0, len(feature_arr), items_per_group)]
    
    for i,chunk in enumerate(chunks):
        plt.scatter(range(items_per_group*i,items_per_group*(i+1)),chunk,color=colors[i],s=3)

    plt.title(name)

def plotData():
    """ 
    ONLY for data set with: 
        "p007" in line or "p008" in line or "p009" in line or "p001" in line) and (i%16==0 or i%16==1)
    in make_inputfile.py:21
    """
    inputs,targets = load("../proc_data/data",equalize=True,shuffle=False,chunksize=2)
    foreArms,upperArms,shoulderLeft = [],[],[]
    for point in inputs:
        foreArms.append(point[0])
        upperArms.append(point[1])
    scatterFeature(foreArms,"Unterarm",4)
    plt.axhline(y=0.32,color="black",ls="dotted")
    scatterFeature(upperArms,"Oberarm",4)
    plt.axhline(y=0.256,color="black",ls="dashed")
    plt.axhline(y=0.265,color="black",ls="dotted")
    plt.show()

if __name__ == "__main__":
    dectree()