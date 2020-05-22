import pandas as pd
import numpy as np
from tqdm import tqdm
from initialvalue import setValue


print('CPU Zn2 Statistic Tool Bare Bones Version V3.0')
print('CAUTION: Large Files may not process')
print('########################################')
dset = str(input('Input path to Data set: '))
oset = str(input('Output path for results: '))
start = float(input('Set Start Test Frequency: '))
end = float(input('Set End Test Frequency: '))
step = float(input('Step: '))
print('########################################')
nu = np.arange(start, end, step)
ini = setValue(dset)
print('Initial Value: ' + str(ini))

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
    return float(final)

def main():
    # This is where we read in the curves
    file = pd.read_csv(dset)
    arrivalTimes = np.array([], dtype=np.float64)
    df = pd.DataFrame(file)
    at = df['Arrival Times']
    at1 = at.drop(0)
    at2 = at1.drop(1)
    arrivalTimes1 = np.append(arrivalTimes, at2)
    arrivalTimes2 = np.subtract(arrivalTimes1, ini)
    count1 = 0
    result = np.zeros(int((end-start)/step))
    pbar = tqdm(total=((end-start)/step))
    while count1 < ((end-start)/step):
        result[count1] = ZnCalculation(count1, arrivalTimes2)
        count1 = count1 + 1
        pbar.update(1)
    pbar.close()
    pd.DataFrame(result).to_csv(str(oset) + '/BBresult' + str(start)+'-'+str(end)+'-' + str(step) + '.csv', index='Zn2 Values')


if __name__ == '__main__':
    main()