# ------------------------------------------------------------------
# Filename:    linear_regression_1_tensorboard.py
# ------------------------------------------------------------------
# File description:
# Python and TensorFlow simple linear regression.
# ------------------------------------------------------------------

# ------------------------------------------------------
# Modules to import
# ------------------------------------------------------

import tensorflow as tf
import time
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import datetime


# ------------------------------------------------------
# Global variables
# ------------------------------------------------------

dataset = [[0, 11], [0, 8], [10, 20], [10, 23],
           [2, 12], [4, 10], [8, 15], [9, 19],
           [5, 11], [5, 10], [6, 14], [7, 15]
           ]

no_of_epochs = 10


# ---------------------------------------------------------------
# def train_the_model(x, y)
# ---------------------------------------------------------------

def train_the_model(x, y):

    print('-- Train the model')

    callback = tf.keras.callbacks.EarlyStopping(
        monitor='loss',
        min_delta=0.001,
        mode='min',
        patience=3)

    model = tf.keras.models.Sequential()

    model.add(tf.keras.layers.Dense(1, input_dim=1))

    model.compile\
        (loss='mean_squared_error',
         optimizer='sgd',
         metrics=['mean_absolute_error'])

    log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    model.fit(
        x, y,
        epochs=no_of_epochs,
        callbacks=[callback, tensorboard_callback],
        verbose=2)

    print(model.summary())

    return model


# ---------------------------------------------------------------
# def predict_from_model(model, to_predict)
# ---------------------------------------------------------------

def predict_from_model(model, to_predict):

    print('-- Predict from the trained model')

    predictions = model.predict(to_predict)
    weights = model.get_weights()

    return predictions, weights


# ---------------------------------------------------------------
# def display_details(weights, to_predict, predictions)
# ---------------------------------------------------------------

def display_details(weights, to_predict, predictions):

    print('-- Display details')

    a0 = weights[0]
    b0 = weights[1]

    a = a0[0, 0]
    b = b0[0]

    print('---------------------------------------------------')
    print(weights)

    print('-- a = ' + str(a))
    print('-- b = ' + str(b))

    if a == 0.0:
        a_print = ''
    else:
        a_print = str('%.3fx' % a)

    if b == 0.0:
        b_print = ''
    elif b < 0.0:
        b_print = str(' - %.3f' % tf.math.abs(b))
    else:
        b_print = str(' + %.3f' % b)

    print('-- Simple linear equation estimation --------------')
    print('-- Equation is y = ' + a_print + b_print)
    print('---------------------------------------------------')

    print('-- Predicted values of y --------------------------')
    print('x = ' + str(to_predict))
    print('')
    print('y = ' + str(predictions))
    print('---------------------------------------------------')


# ---------------------------------------------------------------
# def plot_data(x, y, weights, to_predict, predictions)
# ---------------------------------------------------------------

def plot_data(x, y, weights, to_predict, predictions):

    print('-- Plot the data')

    a = weights[0][0, 0]
    b = weights[1][0]

    x_predictions = np.arange(
        x[tf.argmin(x)],
        x[tf.argmax(x)],
        0.001)

    y_predictions = tf.math.add(tf.math.multiply(a, x_predictions), b)

    plt.plot(x, y, 'ro')
    plt.plot(x_predictions, y_predictions, 'g')
    plt.plot(to_predict, predictions, 'b*')
    plt.grid()
    plt.title('Simple linear regression in Python and TensorFlow')
    plt.xlabel('x data')
    plt.ylabel('y data')
    plt.show()


# ------------------------------------------------------
# def main()
# ------------------------------------------------------

def main():

    # ------------------------------------------------------
    # -- Start of script run actions
    # ------------------------------------------------------

    print('----------------------------------------------------')
    print('-- Start script run ' + str(time.strftime('%c')))
    print('----------------------------------------------------\n')
    print('-- Python version     : ' + str(sys.version))
    print('-- NumPy version      : ' + str(np.__version__))
    print('-- TensorFlow version : ' + str(tf.__version__))
    print('-- Matplotlib version : ' + str(mpl.__version__))

    # ------------------------------------------------------
    # -- Main script run actions
    # ------------------------------------------------------

    training_data = dataset

    x = [row[0] for row in training_data]
    y = [row[1] for row in training_data]

    model = train_the_model(x, y)

    to_predict = np.array([10, 11, 12, 13])
    predictions, weights = predict_from_model(model, to_predict)

    print('-- Training dataset --------------------------')
    print(training_data)
    print('-- x -----------------------------------------')
    print(x)
    print('-- y -----------------------------------------')
    print(y)
    print('-- Model and predictions ---------------------')
    display_details(weights, to_predict, predictions)
    print('----------------------------------------------')

    plot_data(x, y, weights, to_predict, predictions)

    # ------------------------------------------------------
    # -- End of script run actions
    # ------------------------------------------------------

    print('-- Weights --------------------------------------------')
    print(weights)
    print(len(weights))
    print('-----------')
    print(weights[0])
    print(len(weights[0]))
    print(weights[0].shape)
    print('-----------')
    print(weights[1])
    print(len(weights[1]))
    print(weights[1].shape)
    print('----------------------------------------------------')
    print('-- End script run ' + str(time.strftime('%c')))
    print('----------------------------------------------------\n')


# ------------------------------------------------------
# Run only if source file is run as the main script
# ------------------------------------------------------

if __name__ == '__main__':

    main()

# ------------------------------------------------------------------
# End of script
# ------------------------------------------------------------------
