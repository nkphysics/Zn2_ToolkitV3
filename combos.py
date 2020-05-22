import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def save(array):
    save = str(input('Would you like to save the numerical results? (y/n): [n] '))
    if save == 'y' or save == 'Y':
        outpath = str(input('Enter Path for Outfile: '))
        pd.DataFrame(array).to_csv(outpath + '/TotalCombined.csv')
    else:
        pass

def findValue(array):
    quest = str(input('Search for Numerical Result? (y/n): [n] '))
    if quest == 'y':
        q2 = str(input('In a given range or a specific value? (r/s): '))
        if q2 == 's':
            spec = float(input('Enter specific Value: '))
            for i in array:
                if i == spec:
                    print('Value is found')
                else:
                    print('Value is not found')
        elif q2 == 'r':
            lowb = float(input('Enter the lower bound of the search range: '))
            upb = float(input('Enter the upper bound of the search range: '))
            for i in array:
                if lowb <= i <= upb:
                    print('Value found:' + str(i))
                else:
                    pass
        else:
            print('No input given')
            print('Exiting')
    else:
        pass

def combination():
    print('Zn2 data Combination tool')
    print('###############################################')
    totalsets = int(input('Enter the total number of data sets: '))
    start = float(input('Enter the Start Test Frequency: '))
    end = int(input('Enter the end test Frequency: '))
    stepsize = float(input('Enter Step Size: '))
    title = str(input('Input Title for the plot: '))
    setStore = np.ones(totalsets, dtype='<U256')
    weight = np.ones(totalsets, dtype='float')
    count = 1
    while count <= totalsets:
        setName = str(input('Input the path to data set ' + str(count) + ': '))
        setWeight = float(input('Weight for Data Set: '))
        weight[count-1] = setWeight
        setStore[count-1] = setName
        count = count + 1
    print('###############################################')
    scaling = float(input('Input Scaling Adjustment(If you do not want to scale enter 1): '))
    xtick = float(input('Input x - axis tick spacing: '))
    print('###############################################')
    values = []
    if totalsets == 1:
        for i in setStore:
            datafile = pd.read_csv(str(i))
            frame = pd.DataFrame(datafile)
            for j in frame['0']:
                corr = j * scaling
                values.append(corr)
        findValue(values)
        save(values)
        x = np.arange(start, end, stepsize)
        fig, a = plt.subplots()
        a.plot(x, values)
        a.set_title(title)
        a.set_xticks(np.arange(start, end, xtick))
        a.set_ylabel('Zn Squared')
        a.set_xlabel('Frequency')
        plt.show()
    else:
        final = 0
        cc = 0
        for i in setStore:
            datafile = pd.read_csv(str(i))
            frame = pd.DataFrame(datafile)
            if cc == 0:
                for j in frame['0']:
                    values.append(j)
                cc = cc + 1
            else:
                final = values + (frame['0'] * weight[cc])
                cc = cc + 1
        final = (final / totalsets) * scaling
        findValue(final)
        save(final)
        x = np.arange(start, end, stepsize)
        fig, a = plt.subplots()
        a.plot(x, final)
        a.set_xticks(np.arange(start, end, xtick))
        a.set_title(title)
        a.set_ylabel('Zn Squared')
        a.set_xlabel('Frequency')
        plt.show()
combination()