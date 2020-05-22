from astropy.io import fits
import csv

print('Zn2 Extraction Tool')
print('##############################')
print('This will convert any .lc file into a .csv format compatible with the both')
print('the CPU and GPU versions of the Zn2 Statistic Tool.')
print('##############################')
infile = str(input('Input path to .lc to be converted: '))
outpath = str(input('Input path to directory for the converted file to be saved: '))
name = str(input('Name of output file (do not include .csv): '))
col = str(input('Collect Time or BaryTime: '))
print('##############################')
print('File in now converting')
print('##############################')
times = []
def write():
    hdul = fits.open(infile)
    data = hdul[1].data
    time = data['Time']
    if col == 'BaryTime' or col == 'barytime' or col == 'Barytime' or col == 'b':
        time = data['Barytime']
    else:
        pass
    for i in time:
        times.append(i)
    # print(times)
    f = open(str(outpath) + '/' + str(name) +'.csv','w')
    writer = csv.writer(f)
    writer.writerow(['Arrival Times'])
    for i in times:
        writer.writerow([i])
    f.close()
    print('Done')
    hdul.close()

write()
