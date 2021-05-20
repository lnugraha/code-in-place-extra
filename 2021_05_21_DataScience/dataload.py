import numpy as np
import pandas as pd
import math, csv, json, sys, os, glob

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

from abc import ABC, abstractmethod

def onlyNumber(dataIN):
    """
    Perfom data check; reject all complex or non-numbers (boolean or strings)
    Raise Type Error : if dataIN is not a number
    Raise Value Error: if dataIN is not a real number
    """
    if type(dataIN) not in [int, float, np.float64, np.float32, 
        np.int8, np.int16, np.int32, np.int64,
        np.uint8, np.uint16, np.uint32, np.uint64]:
        raise TypeError("Input data must be REAL numbers; data type is {}"
            .format(type(dataIN)))
    elif type(dataIN) in [complex, np.complex64, np.complex128]:
        raise ValueError("Input data cannot be COMPLEX numbers")
    else:
        pass

def ColoredScatterPlot(x_array, y_array, z_array,
                       title='Colored Scatter Plot',
                       x='Independent Variable', y='Dependent Variable',
                       save=False):
    color_scheme = ['red', 'blue', 'green', 'cyan', 'magenta', 'orange', 
        'purple', 'pink', 'gray', 'black']
    
    unique = np.unique(z_array)
    size = x_array.shape[0]

    for i in range(size):
        for j in range( len(unique) ):
            if (z_load[i] == unique[j]):
                plt.scatter(x_load[i], y_load[i], c=color_scheme[j])
    plt.title(title); plt.xlabel(x); plt.ylabel(y)
    plt.show()

def ScatterPlot(x_array, y_array, title='Scatter Plot',
                x='Independent Variable', 
                y='Dependent Variable',
                save=False):
    plt.title(title); plt.xlabel(x); plt.ylabel(y)
    plt.scatter(x_array, y_array, c='blue', marker='H')
    if save == False:
        plt.show()
    elif save == True:
        plt.savefig('{}.png'.format(title))

def SurfacePlot(x_array, y_array, function_model,
                title='Surface Plot',
                x='X Axis', y='Y Axis', z='Z Axis', 
                save=False):
    # TODO: Check Please
    x_array, y_array = np.meshgrid(x_array, y_array)
    z_array = function_model(x_array, y_array)
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(x_array, y_array, z_array, cmap=cm.coolwarm,
        linewidth=0, antialiased=False)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    if save == False:
        plt.show()
    elif save == True:
        plt.savefig('{}.png'.format(title))

def loadTXT(file, x_col=0, y_col=1):
    """
    Load a text file and returned as both independent and dependent arrays
    Inputs:
    file : .txt file
    x_col: independent variable column pos
    y_col: dependent variable column pos
    Outputs: x-array and y-array
    """
    # Load .txt data using np methods
    results = np.loadtxt(file, comments='#', delimiter='\t')
    # Independent Variables (Column 0)
    x = np.array( results[:, x_col], dtype=float ) 
    # Dependent Variables (Column 1)
    y = np.array( results[:, y_col], dtype=float ) 
    # Assertion
    for i in range( len(x) ):
        onlyNumber( x[i] ); onlyNumber( y[i] )
    
    x = np.reshape(x, (len(x), 1))
    y = np.reshape(y, (len(y), 1))
    return x, y

def loadCSV(file, x_col=0, y_col=1):
    # Using csv, delimiter is a comma sign (,)
    reader = csv.reader( open(file, 'r'), delimiter=',' )
    result = list(reader)

    rows = len(result) #including header
    cols = len(result[0])

    x = np.ndarray(rows, np.float64)
    y = np.ndarray(rows, np.float64)

    for i in range(rows):
        if (i != 0): # Skip the header part
            x[i] = result[i][x_col]
            y[i] = result[i][y_col]

    x = x[1:] # Decimate the very first unused element
    y = y[1:] # Decimate the very first unused element
    # Assertion
    for i in range ( len(x) ):
        onlyNumber( x[i] ); onlyNumber( y[i] )

    x = np.reshape(x, (len(x), 1))
    y = np.reshape(y, (len(y), 1))
    return x, y

def loadPANDAS(file, x_col=0, y_col=1):
    dataset = pd.read_csv(file)
    x = (dataset.iloc[:,:-1].values).astype('float32')
    y = (dataset.iloc[:, -1].values).astype('float32')
    y = np.reshape(y, (len(y),1))
    
    for i in range ( x.shape[0] ):
        onlyNumber( x[i][0] ); onlyNumber( y[i][0] )
    return x, y

def loadDAT(file, x_col=0, y_col=1):
    # Using with open built-in command
    results = open(file, 'r')
    x_list = list(); y_list = list()
    for line in results:
        fields = line.split('\t')
        x_list.append( fields[0] )
        y_list.append( fields[1] )

    x = np.zeros( len(x_list)-1 ); y = np.zeros( len(x_list)-1 )
    X = x_list[1:]; Y = y_list[1:]

    for i in range( len(X) ):
        x[i] = float( X[i] ); y[i] = float( Y[i] )
        onlyNumber(x[i]); onlyNumber(y[i])
    
    x = np.reshape(x, (len(x), 1))
    y = np.reshape(y, (len(y), 1))
    return x, y

def loadJSON(file, x_col=0, y_col=1):
    dataset = pd.read_json(file)
    x = (dataset.iloc[:,:-1].values).astype('float32')
    y = (dataset.iloc[:, -1].values).astype('float32')
    # x = np.reshape(x, (len(x), 1))
    # y = np.reshape(y, (len(y), 1))
    return x, y

class LoadDIM(ABC):
    """
    Load a data file and return THREE different arrays simultaneously
    Capable of handling multidimensional data (three dimensional)
    Only handle .csv and .txt data extension
    """
    def __init__(self, filein):
        self.filein = filein

    @abstractmethod
    def extractDIM(self, filein, col0=0, col1=1, col2=2):
        pass

class loadTXT_DIM(LoadDIM):
    def __init__(self, filein):
        self.filein = filein
    
    def extractDIM(self, col0=0, col1=1, col2=2):
        results = np.loadtxt( self.filein, comments='#', delimiter='\t')
        x = results[:,col0]; y = results[:,col1]; z = results[:,col2]
        for i in range (len(x)):
            onlyNumber(x[i]); onlyNumber(y[i]); onlyNumber(z[i])
        
        x = np.reshape(x, (len(x), 1))
        y = np.reshape(y, (len(y), 1))
        z = np.reshape(z, (len(z), 1))
        return x, y, z

class loadCSV_DIM(LoadDIM):
    def __init__(self, filein):
        self.filein = filein
    
    def extractDIM(self, col0=0, col1=1, col2=2):
        # Using csv, delimiter is a comma sign (,)
        reader = csv.reader( open(self.filein, 'r'), delimiter=',' )
        result = list(reader)
        rows = len(result) #including header

        x = np.zeros(rows); y = np.zeros(rows);z = np.zeros(rows)

        for i in range(rows):
            if (i != 0): # Skip the header part
                x[i] = result[i][col0]
                y[i] = result[i][col1]
                z[i] = result[i][col2]

        x = x[1:]; y = y[1:]; z = z[1:]
        for i in range (len(x)):
            onlyNumber(x[i]); onlyNumber(y[i]); onlyNumber(z[i])

        x = np.reshape(x, (len(x), 1))
        y = np.reshape(y, (len(y), 1))
        z = np.reshape(z, (len(z), 1))
        return x, y, z

def function_model(x_array, y_array):
    # Complete arbitrary function model here
    z_array = np.sin( np.sqrt(x_array**2 + y_array**2) )
    return z_array
    
def Himmelblau_Function(x_array, y_array):
    # Himmelblau Function
    z_array = (x_array**2 + y_array - 11)**2 + (x_array + y_array**2 - 7)**2
    return z_array

def CreateMeshData(minXY, maxXY, delta, function_model=Himmelblau_Function):
    x = np.arange(minXY, maxXY, delta)
    y = np.arange(minXY, maxXY, delta)
    X, Y = np.meshgrid(x, y)
    Z = [function_model(x,y) for (x,y) in zip(X,Y)]
    return (X, Y, Z)

if __name__ == '__main__':
    name_txt = '../data/snow/snow.txt'
    name_csv = '../data/snow/snow.csv'
    name_dat = '../data/snow/snow.dat'
    name_json = '../data/snow/snow.json'

    duration_csv = '../data/duration/duration.csv'
    wblake = '../data/triplet/wblake.txt'
    triplets = '../data/triplet/svm_test.csv'
    multiclass = '../data/triplet/wblake.txt'
    perceptron = '../data/triplet/perceptron.csv'
    cvx_data = '../data/triplet/xy_test.csv'

    # x_load, y_load = loadTXT(name_txt)
    # x_load, y_load = loadCSV(duration_csv)
    # x_load, y_load = loadDAT(name_dat)
    # x_load, y_load = loadPANDAS(name_csv)
    
    multidim_data = loadCSV_DIM(cvx_data)
    # multidim_data = loadCSV_DIM(perceptron)
    x_load, y_load, z_load = multidim_data.extractDIM()
    ColoredScatterPlot(x_load, y_load, z_load)

    """
    unique = np.unique(z_load)
    print(unique[0], unique[1])
    # print(unique)
    color_scheme = ['red', 'blue', 'green', 'orange', 'cyan', 'magenta', 'gray']
    for i in range(size):
        for j in range( len(unique) ):
            if (z_load[i] == unique[j]):
                plt.scatter(x_load[i], y_load[i], c=color_scheme[j])
    plt.show()
    """

    # multidim_data = loadCSV_DIM(perceptron)
    # x_load, y_load, z_load = multidim_data.extractDIM()

    # ScatterPlot(y_load, z_load)
    # ScatterPlot(x_load, y_load)

    """
    # Create a 2D Contour Plot
    x_array = np.arange(-6, 6, 0.1)
    y_array = np.arange(-6, 6, 0.1)
    z_array = np.zeros( len(x_array) )
    SurfacePlot(x_array, y_array, Himmelblau_Function, 'Himmelblau Function 3D')
    """

    """
    # Create a 3D Surface Plot
    (X,Y,Z) = CreateMeshData(-6, 6, 0.1, Himmelblau_Function)
    nContour = 50
    plt.contour(X, Y, Z, nContour)
    plt.title('Himmerblau Function on 2-D Surface')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()
    """
