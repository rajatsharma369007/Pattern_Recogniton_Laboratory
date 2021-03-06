'''
This script helps to calculate the discriminant function. This is part of 
pattern recognition assignment-1b
'''

# importing Libraries
import numpy as np
from utils import read_dataset
from utils import discriminant
from utils import plot

# reading dataset
path = "/home/rajat/Documents/8th sem/Pattern_recognition/Pattern_Recognition_Laboratory/dataset/data.xlsx"

'''
Class : create_vector()
Arguments : path --> path of the dataset file
'''

xvec1, xvec2 = read_dataset.create_vector(path)

# user input of new point which is to be classified
x = int(input("Enter the x coordinate: "))
y = int(input("Enter the y coordinate: "))

# making it a coordinate
x_point = np.array([x, y])

# prior probability
w1 = 1/2
w2 = 1/2

# calling discriminant function
'''
Class : function()
Arguments : x ---> new input point
        xvec1 ---> class1 points
        xvec2 ---> class2 points
           w1 ---> prior probability of class1
           w2 ---> prior probability of class2
'''
g1, g2 = discriminant.function(x_point, xvec1, xvec2, w1, w2)

# classifying the input point
'''
Class : classify()
Arguments : g1 : discriminant value received for class1
            g2 : discriminant value received for class2
'''
g = discriminant.classify(g1, g2)

# plotting the decision boundary
'''
Class : scatter_plot()
Arguments : x_point ---> new input point
              xvec1 ---> class1 points
              xvec2 ---> class2 points
'''
plot.scatter_plot(x_point, xvec1, xvec2, w1, w2)
