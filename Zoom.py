import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def zoom():
    setName = str(input('Input the path to data set : '))
    data = pd.read_csv(setName)
    df = pd.DataFrame(data)
    lowB = int(input('Enter lower Bound: '))
    upB = int(input('Enter upper bound: '))
    step = float(input('Enter Step Size: '))
    conLow = (lowB - lowB) * 100
    conUp = (upB - lowB) * 100
    rann = np.arange(lowB, upB, step)
    xrange = df.loc[conLow:(conUp-1)]
    yVals = xrange['0']
    # pois = np.random.poisson(yVals)
    # print(pois)
    # plot = str(input('Would you like to plot (y/n): [n] '))
    title = str(input('Enter title for Plot: '))
    fig, a = plt.subplots()
    a.plot(rann, yVals)
    a.set_title(title)
    a.set_xlabel('Frequency')
    a.set_ylabel('Zn Squared')
    plt.show()
    print('Done')
zoom()