import pandas as pd
# import time
import numpy as np
from tqdm import tqdm
from initialvalue import setValue

# This is where we read in the curves
print('CPU Z22 Statistic Tool V3.0 ')
print('!ALERT!: This version does two harmonics only!')
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
    t01 = float(ini)
    diffIF = array - t01
    correction = diffIF * nu[number]
    ncorr2 = correction * (4*np.pi)
    ncorr1 = correction * (2*np.pi)
    cos2 = np.cos(ncorr2)
    sin2 = np.sin(ncorr2)
    cos1 = np.cos(ncorr1)
    sin1 = np.sin(ncorr1)
    totCos = cos2 + cos1
    totSin = sin2 + sin1
    sumCos = np.sum(totCos)
    sumSin = np.sum(totSin)
    twoOn = 2 / totalCounts(array)
    sC2 = sumCos ** 2
    sS2 = sumSin ** 2
    final = twoOn*(sC2 + sS2)
    return (final)
def main():
    # This is where we read in the curves
    # ss = time.time()
    chunks = (150 * 10 ** 6)
    file = pd.read_csv(dset, chunksize=(chunks))
    cc = 0
    for chunk in file:
        arrivalTimes = np.array([], dtype=np.float64)
        df = pd.DataFrame(chunk)
        arrivalTimes = np.append(arrivalTimes, df['Arrival Times'])
        # print(totalCounts(df['Arrival Times']))
        # print(df['Arrival Times'].iloc[0])
        cc = cc + 1
        count1 = 0
        result = np.zeros(int((end-start)/step))
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
        scaling = result * 10000
        # ee = time.time()
        # print('Time Elaspsed: '+ str(ee-ss) + ' seconds')
        pd.DataFrame(scaling).to_csv(str(oset) +'/Tresult'+ str(start)+'-'+str(end)+'-' + str(step)+ '-'+
                                     str(cc)+'.csv', index= 'Zn2 Values')
main()
