import dataload
import matplotlib.pyplot as plt
import numpy as np
from random import seed, randrange
import os, sys, glob
from abc import abstractmethod, ABC

class LINEAR_REGRESSION(object):
    def __init__(self, xs, ys):
        self.xs = xs 
        self.ys = ys
        self.size = len(xs)
        if (self.size == 0):
            print("ERROR: Data size cannot be zero")
            sys.exit()
        elif (len(xs) != len(ys)):
            print("ERROR: Independent and dependent variable length is unequal")
            sys.exit()
    
    def RegressionPlot(self, y_predict):
        pass

class LINEAR_RSQUARE(object):
    # TODO: Use super method
    def __init__(self, xs, ys):
        self.xs = xs 
        self.ys = ys
        self.size = len(xs)
        if (self.size == 0):
            print("ERROR: Data size cannot be zero")
            sys.exit()
        elif (len(xs) != len(ys)):
            print("ERROR: Independent and dependent variable length is unequal")
            sys.exit()

    def slope_intercept(self):
        n = self.size
        S_x  = sum( self.xs ); S_y  = sum( self.ys )
        S_xx = sum( self.xs**2 ); S_xy = sum( self.xs*self.ys ) 
        # S_yy = sum( ys**2 )

        m = (n*S_xy - S_x*S_y) / (n*S_xx - S_x**2)
        b = S_y/n - m*(S_x/n)
        return m, b
    
    def squared_error(self, original, estimation):
        sum_sqr_err = 0.0
        for i in range( len(original) ):
            sqr_err = (estimation[i] - original[i])**2
            sum_sqr_err += sqr_err
        return sum_sqr_err

    def rsquared(self):
        ys_original  = list(self.ys)
        m_est, b_est = self.slope_intercept()

        ys_estimation = [m_est * x + b_est for x in self.xs]   
        ys_mean_line  = [np.mean(self.ys) for y in ys_original] 
        SS_tot = self.squared_error(ys_original, ys_mean_line)
        SS_res = self.squared_error(ys_original, ys_estimation)
        return (1.0 - (SS_res/SS_tot))
    
class LINEAR_RMSE(object):
    def __init__(self, xs, ys):
        self.xs = xs
        self.ys = ys

    def predict(self, row, coeff):
        # Coefficient predicitions
        y_hat = coeff[0]
        for i in range (len(row)-1):
            y_hat += coeff[i+1] * row[i]
        return y_hat

    def SGD_coeff(self, n_epoch=10, l_rate=0.001):
        # Estimate linear regression coefficients using SGD        
        train_set = np.concatenate( (self.xs, self.ys) )
        train_set = np.reshape(train_set, (len(self.xs),2), order='F')

        coef = np.zeros( len(train_set[0]) )
        for _ in range(n_epoch):
            sum_error = 0.0
            
            for row in train_set:
                yhat       = self.predict(row, coef)
                error      = yhat - row[-1]
                sum_error += error**2
                coef[0]   -= l_rate * error
                
                for i in range(len(row)-1):
                    coef[i + 1] -= l_rate * error * row[i]
            # print('>> epoch={}, lrate={}, error={}'.format(epoch, l_rate, 
            # sum_error))
        m = np.array( [coef[1]] ); b = np.array( [coef[0]] )
        return m, b

    def RMSE(self, y_original, y_estimation):
        sum_error = 0.0
        for i in range(0, len(y_original)):
            error = y_estimation[i] - y_original[i]
            sum_error += error**2
        mean_error = sum_error/float( len(y_original) )
        return mean_error

if __name__ == '__main__':
    snow_data = '../data/snow/snow.csv'
    x_snow, y_snow = dataload.loadCSV(snow_data)
    
    linear_reg_01 = LINEAR_RSQUARE(x_snow, y_snow)
    m_snow, b_snow = linear_reg_01.slope_intercept()
    regression_line = [m_snow * x + b_snow for x in x_snow]
    rsqr = linear_reg_01.rsquared()

    print("Slope and Intercept: {} and {}".format(m_snow, b_snow) )
    print("R-square: {}".format(rsqr))
    """ Use bool flag to display graph
    plt.scatter(x_snow, y_snow, color='red')
    plt.plot(x_snow, regression_line, color='blue')
    plt.title('Plot of Snow vs Yield using Statistical Analysis')
    plt.xlabel('Snow')
    plt.ylabel('Yield')
    plt.show()
    """
    
    linear_reg_02 = LINEAR_RMSE(x_snow, y_snow)
    m, b = linear_reg_02.SGD_coeff(1000, 0.001)
    regressionline_02 = m * x_snow + b
    rmse = linear_reg_02.RMSE(y_snow, regressionline_02)
    print("Slope and Intercept: {} and {}".format(m, b) )
    print("RMSE: {}".format(rmse))
    
    """ Use bool flag to display graph
    plt.scatter(x_snow, y_snow, color='red')
    plt.plot(x_snow, regressionline_02, color='blue')
    plt.title('Plot of Snow vs Yield using Machine Learning Analysis')
    plt.xlabel('Snow')
    plt.ylabel('Yield')
    plt.show()
    """
