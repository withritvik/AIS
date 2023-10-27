import pandas as pd

# This function removes the metadata from the input files and returns the dataframe without the metadata
def nometa(path):
    input = open(path, 'r') # Open the file
    lines = input.readlines() # Read the lines
    input.close() # Close the file

    del lines[0:17] # Delete the metadata
    lines = [line.replace('\t', ',') for line in lines] # Replace the tabs with commas
    lines = [line.replace('\n', '') for line in lines] # Remove the new line characters
    lines = [line.replace(' ', ',') for line in lines] # Replace the spaces with commas
    df = pd.DataFrame([sub.split(",") for sub in lines]) # Create a dataframe from the lines
    return df

# This function saves the dataframe to a csv file
def tocsv(path, df):
    df.to_csv(path, index=False, header=False) 

shapes = ['circA', 'circB', 'sigDiaA', 'sigDiaB', 'sigMea1', 'sigMea2', 'sigMea3', 'sigMea4', 'sigSp1', 'sigSp2', 'sigSp3', 'sigSp4'] # Shapes drawn by the subjects
n = 38 # Max ID number

# This loop creates a csv file for each subject after removing the metadata
for shape in shapes:
    for i in range(n):
        file_h = 'healthy_txt\\' + shape + '-H' + str(i + 1) + '.txt' # Input file
        file_p = 'patient_txt\\' + shape + '-P' + str(i + 1) + '.txt'

        try:
            input_h = nometa(file_h) # Remove the metadata
            out_path_h = 'healthy_csv\\' + shape + '_nometa\\' + shape + '-H' + str(i + 1) + '.csv' # Output file
            tocsv(out_path_h, input_h) # Save the healthy subject's dataframe to a csv file
        except:
            pass

        try:
            input_p = nometa(file_p)
            out_path_p = 'patient_csv\\' + shape + '_nometa\\' + shape + '-P' + str(i + 1) + '.csv'
            tocsv(out_path_p, input_p) # Save the patient's dataframe to a csv file
        except:
            pass