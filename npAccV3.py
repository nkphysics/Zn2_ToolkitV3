import pandas as pd
# import time
import numpy as np
from numpy.core._multiarray_umath import ndarray
from tqdm import tqdm
from initialvalue import setValue

# This is where we read in the curves
print('CPU Zn2 Statistic Tool Version 3.0')
print('########################################')
dset = str(input('Input path to Data set: '))
oset = str(input('Output path for results: '))
start = float(input('Set Start Test Frequency: '))
end = float(input('Set End Test Frequency: '))
step = float(input('Step: '))
print('########################################')

# Stores generated frequencies
nu = np.arange(start,end,step)
ini = setValue(dset)
# Generates the values of nu based on a set start, stop and the size of each step between values
def totalCounts(dataset):
    count = 0
    for i in dataset:
        if i==i:
            count = count+1
    return (count)
def ZnCalculation(number, array):
    # Just a constant that will be subtracted in finding the difference
    # THIS MUST BE CHANGED BASED ON THE DATA-SET
    # THIS MUST BE CHANGED BASED ON THE DATA-SET
    # THIS MUST BE CHANGED BASED ON THE DATA-SET
    # THIS MUST HAVE 11 DECIMAL PLACES OF PRECISION
    correction = np.multiply(array, nu[number])
    ncorr1 = np.multiply(correction, (2*np.pi))
    cos1 = np.cos(ncorr1)
    sin1 = np.sin(ncorr1)
    sumCos = np.sum(cos1)
    sumSin = np.sum(sin1)
    twoOn = 2 / totalCounts(array)
    sC2 = sumCos ** 2
    sS2 = sumSin ** 2
    final = twoOn*(sC2 + sS2)
    return (final)

def main():
    # This is where we read in the curves
    # ss = time.time()
    chunks = (105000000)
    file = pd.read_csv(dset, chunksize=(chunks))
    cc = 0
    for chunk in file:
        arrivalTimes: ndarray = np.array([], dtype=np.float64)
        df = pd.DataFrame(chunk)
        arrivalTimes = np.append(arrivalTimes, df['Arrival Times'])
        arrivalTimes = np.subtract(arrivalTimes, ini)
        # print(totalCounts(df['Arrival Times']))
        # print(df['Arrival Times'].iloc[0])
        cc = cc + 1
        count1 = 0
        result = np.ones(int((end-start)/step))
        pbar = tqdm(total=((end-start)/step))
        while count1 <((end-start)/step):
            result[count1]= ZnCalculation(count1, arrivalTimes)
            count1 = count1 +1
            pbar.update(1)
            # print('Iteration: '+ str(count1))
            # print('Iterarion Time: ' + str(et - st) + 'seconds')
            # print(result)
        pbar.close()
        resultCount = 0
        for i in result:
            if i==i:
                resultCount = resultCount+1
        scaling = result
        # ee = time.time()
        # print('Time Elaspsed: '+ str(ee-ss) + ' seconds')
        pd.DataFrame(scaling).to_csv(str(oset) +'/Tresult'+ str(start)+'-'+str(end)+'-' + str(step)+ '-'+
                                     str(cc)+'.csv', index= 'Zn2 Values')
main()