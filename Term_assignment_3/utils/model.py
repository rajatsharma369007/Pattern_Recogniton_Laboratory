'''
This script is for training and testing the model and prediction
'''

# importing libraries
import numpy as np

# function for training the model on iris dataset
def train_irismodel(X_train, y_train, epochs, learnrate, n_hidden):
    # no. of rows, no. of columns
    n_records, n_features = X_train.shape
    
    # initializing the size of weight vectors
    weights_input_hidden = np.random.normal(scale = 1 / n_features ** 0.5, size = (n_features, n_hidden))
    weights_hidden_output = np.random.normal(scale = 1 / n_features ** 0.5, size = n_hidden)
    
    for e in range(epochs):
        # initializing all the delta weights with zeros
        del_w_input_hidden = np.zeros(weights_input_hidden.shape)
        del_w_hidden_output = np.zeros(weights_hidden_output.shape)
        # In each epoch, and in each value of column
        for x, y in zip(X_train.values, y_train):
            # forward pass
            hidden_input = np.dot(x, weights_input_hidden)
            hidden_output = sigmoid(hidden_input)
            output = sigmoid(np.dot(hidden_output, weights_hidden_output))
            
            # backward pass
            error = y - output
            # calculate the error term for the output unit,
            output_error_term = error * output * (1 - output)
            
            # hidden layer's contribution to the error
            hidden_error = np.dot(output_error_term, weights_hidden_output)
            # error term for the hidden layer
            hidden_error_term = hidden_error * hidden_output * (1 - hidden_output)
            
            # update the change in weights
            del_w_hidden_output += output_error_term * hidden_output
            del_w_input_hidden += hidden_error_term * x[:, None]
        
        # updating weights
        weights_input_hidden += learnrate * del_w_input_hidden / n_records
        weights_hidden_output += learnrate * del_w_hidden_output / n_records 
        
        # Printing out the mean square error on the training set
        if e % (epochs / 10) == 0:
            print('\nepoch : ', e)
            hidden_output = sigmoid(np.dot(x, weights_input_hidden))
            out = sigmoid(np.dot(hidden_output, weights_hidden_output))
            loss = np.mean((out - y_train) ** 2)
            print("training accuracy: ", 1 - loss)

    print('\ntraining complete')
    
    model = [weights_input_hidden, weights_hidden_output]
    
    return model
    
           
# activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def predict_irismodel(X_test, y_test, model):
    
    hidden = sigmoid(np.dot(X_test, model[0]))
    out = sigmoid(np.dot(hidden, model[1]))
    # threshold
    predictions = out > 0.5
    accuracy = np.mean(predictions == y_test)
    print("\ntesting accuracy: ", accuracy)
    return predictions

