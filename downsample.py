import pandas as pd
import numpy as np

def down(df): # Function to downsample the data to 10000 rows
    down_freq = df.shape[0] / 10000 # Downsampling Frequency
    downsampled_data = np.zeros((10000, df.shape[1])) # Create a numpy array of zeros

    for i in range(10000):
        downsampled_data[i] = df.iloc[int(i * down_freq)]

    return downsampled_data

shapes = ['circA', 'circB', 'sigDiaA', 'sigDiaB', 'sigMea1', 'sigMea2', 'sigMea3', 'sigMea4', 'sigSp1', 'sigSp2', 'sigSp3', 'sigSp4'] # Shapes drawn by the subjects
n = 38 # Max ID number

for shape in shapes:
    for i in range(n):
        file_h = 'healthy_csv\\' + shape + '_nometa\\' + shape + '-H' + str(i + 1) + '.csv'
        file_p = 'patient_csv\\' + shape + '_nometa\\' + shape + '-P' + str(i + 1) + '.csv'

        try:
            df_h = pd.read_csv(file_h, header=None)
            downsampled_data_h = down(df_h)
            output_path_h = 'healthy_ds\\' + shape + '-H' + str(i + 1) + '_downsampled.csv'
            pd.DataFrame(downsampled_data_h).to_csv(output_path_h, index=False, header=False)
        except:
            pass

        try:
            df_p = pd.read_csv(file_p, header=None)
            downsampled_data_p = down(df_p)
            output_path_p = 'patient_ds\\' + shape + '-P' + str(i + 1) + '_downsampled.csv'
            pd.DataFrame(downsampled_data_p).to_csv(output_path_p, index=False, header=False)
        except:
            pass