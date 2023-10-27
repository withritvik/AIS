import pandas as pd
import numpy as np

shapes = ['circA', 'circB', 'sigDiaA', 'sigDiaB', 'sigMea1', 'sigMea2', 'sigMea3', 'sigMea4', 'sigSp1', 'sigSp2', 'sigSp3', 'sigSp4'] # Shapes drawn by the subjects
n = 38 # Max ID number

def single_pivot(path): # Flattening the data from a 10000x6 matrix to a 60000x1 vector
    df = pd.read_csv(path, sep=',', header=None)
    return df.values.ravel(order='F') # Order F is used to flatten the matrix column-wise

pivot_table_h = []
pivot_table_p = []

for i in range(n):
    pivot_h = []
    pivot_p = []
    for shape in shapes:
        file_h = 'healthy_ds\\' + shape + '-H' + str(i + 1) + '_downsampled.csv'
        file_p = 'patient_ds\\' + shape + '-P' + str(i + 1) + '_downsampled.csv'

        try:
            pivot_h = np.concatenate((pivot_h, single_pivot(file_h)), axis=0) # Concatenating the vectors of each shape (12 shapes per subject)
        except:
            pass
        
        try:
            pivot_p = np.concatenate((pivot_p, single_pivot(file_p)), axis=0)
        except:
            pass

    pivot_table_h.append(pivot_h) # Concatenating the vectors of each subject (38 subjects)
    pivot_table_p.append(pivot_p)

pivot_table_h = (pd.DataFrame(pivot_table_h)).dropna()
pivot_table_p = (pd.DataFrame(pivot_table_p)).dropna()

pivot_table_h.to_csv('pivot_table_healthy.csv', index=False, header=False) # Saving the pivot tables as csv files
pivot_table_p.to_csv('pivot_table_patient.csv', index=False, header=False)