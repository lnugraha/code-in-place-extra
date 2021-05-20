# Redirect to the src/ directory to gain access to the previously written file
# import sys
# sys.path.insert(1,'../src')

import linear

import numpy as np
import matplotlib.pyplot as plt

NUMBER_DAYS = 478
dayElapsed = np.zeros(NUMBER_DAYS)
for i in range(NUMBER_DAYS):
    dayElapsed[i] = float(i+1)

def loadTextFile(textFile="./countries/China.txt"):
    # Load .txt data using np methods
    results = np.loadtxt(textFile, comments='#', delimiter='\t')
    infected = np.array( results[:], dtype=float ) 
    return infected


def statisticalAnalysis(dayElapsed, infectedPatient):
    statisticsMethod = linear.LINEAR_RSQUARE(dayElapsed, infectedPatient)
    m_infct, b_infct = statisticsMethod.slope_intercept()
    rSquare = statisticsMethod.rsquared()
    # Create the regression line using functional programming method
    regressionLine = [m_infct * day + b_infct for day in dayElapsed]
    return m_infct, b_infct, rSquare, regressionLine


def linearRegressionAnalysis(dayElapsed, infectedPatient):
    regressionMethod = linear.LINEAR_RMSE(dayElapsed, infectedPatient)

    EPOCHS = 20000 # Beyond 20k has no meaningful change
    LEARNING_RATE = 1.0e-5 # Beyond 1.0e-5 causes arithmetic overflow
    m_infct, b_infct = regressionMethod.SGD_coeff(EPOCHS, LEARNING_RATE)
    # Create the regression line
    regressionLine = m_infct * dayElapsed + b_infct
    RMSE = regressionMethod.RMSE(infectedPatient, regressionLine)
    return m_infct, b_infct, RMSE, regressionLine


def main():
    countCHN = loadTextFile()
    
    # Linear Regression using statistical analysis
    m_01, b_01, r_01, line_01 = statisticalAnalysis(dayElapsed, countCHN)
    plt.scatter(dayElapsed, countCHN, color='red')
    plt.plot(dayElapsed, line_01, color='blue')
    plt.title('Plot of Day vs Infected Patients using Statistical Analysis')
    plt.xlabel('Day Elapsed')
    plt.ylabel('Newly Infected Patient')
    plt.show()
    print(f"Statictical analysis results: slope = {m_01}; intercept = {b_01}; R-squared = {r_01}")

    # Linear Regression using machine learning analysis
    m_02, b_02, rmse, line_02 = linearRegressionAnalysis(dayElapsed, countCHN)
    plt.scatter(dayElapsed, countCHN, color='red')
    plt.plot(dayElapsed, line_02, color='blue')
    plt.title('Plot of Day vs Infected Patients using Machine Learning Analysis')
    plt.xlabel('Day Elapsed')
    plt.ylabel('Newly Infected Patient')
    plt.show()
    print(f"Machine learning results: slope = {m_02}; intercept = {b_02}")

if __name__ == "__main__":
    main()
