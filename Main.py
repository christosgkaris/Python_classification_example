import csv
import numpy as np
import matplotlib.pyplot as plt

# Task 5, here I calculate P(F|X0,...,Xn) given P(F|X0,...,Xn-1) and Xn
def posterior(prior, xn):
    if (xn=='T'): A = 0.5 / (0.5*prior+0.75*(1-prior))
    if (xn=='H'): A = 0.5 / (0.5*prior+0.25*(1-prior))
    posteriorFairCoin = A * prior
    return posteriorFairCoin        

# Task 6, the files: coin-flips.csv and Main.py, should be in the same folder
def task6():
    
    # store the .csv contents in a list
    l = []
    # source: docs.python.org/3/library/csv.html
    with open('.\\coin-flips.csv', newline='') as f:
        buffer = csv.reader(f)
        for row in buffer:
            l.append(row)
    f.close()
    
    # experiments
    experiments = np.zeros([12, 20])
    for i in range(0, 12):
        if (l[i][0]=='T'): experiments[i][0] = 2/5    # P(F|T) = 2/5
        if (l[i][0]=='H'): experiments[i][0] = 2/3    # P(F|H) = 2/3
        for j in range(1, 20):
            experiments[i][j] = posterior(experiments[i][j-1], l[i][j])
    experiments = 1 - experiments    # P(B|X0,...,Xn) = 1 - P(F|X0,...,Xn)
    
    # plotting
    # source: stackoverflow.com/questions/6473679/transpose-list-of-lists
    plt.plot(list(map(list, zip(*experiments))))
    
    plt.title('Experiments')
    plt.xlabel('Number of experiment')
    plt.ylabel('P(B|X1,...,X20)')
    plt.show()
    
    return experiments
