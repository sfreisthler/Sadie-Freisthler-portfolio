#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from pandas.io.parsers import read_csv
import math

def euclidean_distance(a,b):
    diff = a - b
    return np.sqrt(np.dot(diff, diff))

def load_data(csv_filename):
    """ 
    Returns a numpy ndarray in which each row repersents
    a wine and each column represents a measurement. There should be 11
    columns (the "quality" column cannot be used for classificaiton).
    """

    df = read_csv(csv_filename, delimiter=';')

    # remove the quality column 
    df = df.drop('quality', axis = 1)

    # convert from pandas dataframe to numpy array 
    np_array = df.to_numpy()

    return(np_array)


def split_data(dataset, ratio = 0.9):
    """
    Return a (train, test) tuple of numpy ndarrays. 
    The ratio parameter determines how much of the data should be used for 
    training. For example, 0.9 means that the training portion should contain
    90% of the data. You do not have to randomize the rows. Make sure that 
    there is no overlap. 
    """
    train_number = (ratio * len(dataset)) // 1
    train_number = int(train_number)

    train = dataset[:(train_number+1)]
    test = dataset[(train_number+2):]

    return(train, test)
    

def compute_centroid(data):
    """
    Returns a 1D array (a vector), representing the centroid of the data
    set. 
    """
    return sum(data[:,:]) / data.shape[0]
    

def experiment(ww_train, rw_train, ww_test, rw_test):
    """
    Train a model on the training data by creating a centroid for each class.
    Then test the model on the test data. Prints the number of total 
    predictions and correct predictions. Returns the accuracy. 
    """
    # compute centroids from training data
    wine_to_centroid = {}

    ww_centroid = compute_centroid(ww_train)
    wine_to_centroid['ww'] = ww_centroid 
    rw_centroid = compute_centroid(rw_train)
    wine_to_centroid['rw'] = rw_centroid

    # compare distance from test point to centroid to predict if it is red or white wine
    correct = 0
    wrong = []
    total_predictions = 0

    for unlabeled_point in ww_test:
        closest_class = None
        closest_distance = math.inf

        for key in wine_to_centroid:
            centroid = wine_to_centroid[key]
            distance = euclidean_distance(centroid,unlabeled_point)
            if distance < closest_distance:
                closest_class = key
                closest_distance = distance

        if closest_class == "ww":
            correct += 1
        else:
            wrong.append(unlabeled_point)

        total_predictions += 1

    for unlabeled_point in rw_test:
        closest_class = None
        closest_distance = math.inf

        for key in wine_to_centroid:
            centroid = wine_to_centroid[key]
            distance = euclidean_distance(centroid, unlabeled_point)
            if distance < closest_distance:
                closest_class = key
                closest_distance = distance 
        if closest_class == "rw":
            correct += 1
        else:
            wrong.append(unlabeled_point)

        total_predictions += 1

    accuracy = correct / total_predictions

    # print total predictions made and accuracy
    print(total_predictions)
    print(correct)
    print(accuracy)

    # return accuracy
    return accuracy 

    
def cross_validation(ww_data, rw_data, k):
    """
    Perform k-fold crossvalidation on the data and print the accuracy for each
    fold. 
    """
    # crossvalidation for ww
    counter = 1
    accuracy_list = []
    size = len(ww_data) // k

    # iterate over k-partitions 
    while counter <= k:
        upper_bound = size * counter
        lower_bound = (size * counter) - size

        # define upper and lower bounds of white wine test and training datasets
        ww_test = ww_data[lower_bound:(upper_bound)+1]
        if counter == 1:
            ww_train = ww_data[upper_bound+1:]
        else:
            ww_train1 = ww_data[0:lower_bound]
            ww_train2 = ww_data[upper_bound+1:]
            ww_train = np.vstack((ww_train1,ww_train2))
        
        # define upper and lower bounds of red wine test and training datasets
        rw_test = rw_data[lower_bound:upper_bound+1]
        if counter == 1:
            rw_train = ww_data[upper_bound+1:]
        else:
            rw_train1 = rw_data[0:lower_bound]
            rw_train2 = rw_data[upper_bound+1:]
            rw_train = np.vstack((rw_train1, rw_train2))
        
        accuracy = experiment(ww_train, rw_train, ww_test, rw_test)
        accuracy_list.append(accuracy)

        # increment the counter by 1
        counter += 1
    
    # compute average accuracy of all partitions 
    average_accuracy = sum(accuracy_list) / len(accuracy_list)
    return average_accuracy


    
if __name__ == "__main__":
    
    ww_data = load_data('whitewine.csv')
    rw_data = load_data('redwine.csv')


    # Uncomment the following lines for step 2: 
    ww_train, ww_test = split_data(ww_data, 0.9)
    print(ww_train)
    print(ww_test)
    rw_train, rw_test = split_data(rw_data, 0.9)
    experiment(ww_train, rw_train, ww_test, rw_test)
    
    # Uncomment the following lines for step 3:
    k = 10
    acc = cross_validation(ww_data, rw_data, k)
    print("{}-fold cross-validation accuracy: {}".format(k,acc))
    
