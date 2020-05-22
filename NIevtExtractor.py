from astropy.io import fits
import csv
print('Zn2 Extraction Tool For NICER EVENT Files')
print('##############################')
print('This will convert any .evt file into a .csv format compatible with the both')
print('the CPU and GPU versions of the Zn2 Statistic Tool.')
print('##############################')
infile = str(input('Input path to .evt to be converted: '))
outpath = str(input('Input path to directory for the converted file to be saved: '))
name = str(input('Name of output file (do not include .csv): '))
print('##############################')
print('File in now converting')
print('##############################')
times = []
def write():
    hdul = fits.open(infile)
    data = hdul[1].data
    time = data['Time']
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