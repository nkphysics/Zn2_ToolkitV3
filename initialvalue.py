import pandas as pd
def setValue(infile):
    data = pd.read_csv(str(infile))
    df = pd.DataFrame(data)
    inval = df['Arrival Times'].iloc[1]
    return (inval)
