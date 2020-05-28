import pandas as pd
# import time
import numpy as np
import cupy as cp
from initialvalue import setValue
from tqdm import tqdm

# This is where we read in the curves

print('GPU Zn2 Statistic Tool')
print('**THIS ONLY WORKS WITH CUDA DEVICES**')
print('########################################')
dset = str(input('Input path to Data set: '))
oset = str(input('Output path for results: '))
start = float(input('Set Start Test Frequency: '))
end = float(input('Set End Test Frequency: '))
step = float(input('Step: '))
print('########################################')

# Stores generated frequencies
nu = np.arange(start, end, step)
ini = setValue(dset)
# print(ini)
# Generates the values of nu based on a set start, stop and the size of each step between values

def totalCounts(data):
    count = 0
    for i in data:
        if i==i:
            count = count+1
    return (count)

def ZnCalculation(number, array, initial):
    # Just a constant that will be subtracted in finding the difference
    # THIS MUST BE CHANGED BASED ON THE DATA-SET
    # THIS MUST BE CHANGED BASED ON THE DATA-SET
    # THIS MUST BE CHANGED BASED ON THE DATA-SET
    # THIS MUST HAVE 11 DECIMAL PLACES OF PRECISION
    t01 = (initial)
    gpuArr = cp.asarray(array)
    diffIF = cp.subtract(gpuArr, t01)
    correction = cp.multiply(diffIF, nu[number])
    ncorr1 = cp.multiply(correction, (2 * np.pi))
    cos1 = cp.cos(ncorr1)
    sin1 = cp.sin(ncorr1)
    sumCos = cp.sum(cos1)
    sumSin = cp.sum(sin1)
    twoOn = cp.divide(2, totalCounts(array))
    sC2 = cp.power(sumCos, 2)
    sS2 = cp.power(sumSin, 2)
    tots = cp.add(sC2, sS2)
    final = cp.multiply(twoOn, tots)
    return (final)

def main():
    # ss = time.time()
    chunks = (30 * 10 ** 6)
    file = pd.read_csv(dset, chunksize=(chunks))
    cc = 0
    for chunk in file:
        cc = cc + 1
        arrivalTimes = np.array([], dtype=np.float64)
        df = pd.DataFrame(chunk)
        arrivalTimes = np.append(arrivalTimes, df['Arrival Times'])
        # print(totalCounts(df['Arrival Times']))
        # print(df['Arrival Times'].iloc[0])
        count1 = 0
        result = np.ones(int((end - start) / step))
        pbar = tqdm(total=((end - start) / step))
        while count1 < ((end - start) / step):
            result[count1] = ZnCalculation(count1, arrivalTimes, ini)
            count1 = count1 + 1
            pbar.update(1)
        pbar.close()
        resultCount = 0
        for i in result:
            if i == i:
                resultCount = resultCount + 1
        scaling = result
        # ee = time.time()
        # print('Time Elaspsed: '+ str(ee-ss) + ' seconds')
        pd.DataFrame(scaling).to_csv(str(oset) +'/GResults' +str(start) + '-' + str(end) + '-' + str(step) + '-'
                                     + str(cc) + '.csv', index='Zn2 Values')

main()