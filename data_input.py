from os import path
import sys
import pandas as pd

class InputData:
    def __init__(self):
        self.supported_file_extensions = [".csv"]

    # Function to change the columns to lower case
    def change_columns_to_LowerCase(self, data):
        for column in data.columns:
            data.rename(columns = {column: column.lower()}, inplace=True)
        return data

    # Function to take input of dataset and convert it into a pandas dataframe
    def input_data(self):
        try:
            file_name, file_ext = path.splitext(sys.argv[1])
            if file_ext == "":
                raise SystemExit("Provide the dataset with the file extension.")

            if file_ext not in self.supported_file_extensions:
                raise SystemExit("The file extension is not supported as of yet.")

        except IndexError:
            raise SystemExit("Provide the dataset name with extension.")

        try:
            data = pd.read_csv(file_name+file_ext)

        except pd.errors.EmptyDataError:
            raise SystemExit("The file is empty.")

        except FileNotFoundError:
            raise SystemExit("File doesn't exist.")

        # Change the columns to lower case
        data = self.change_columns_to_LowerCase(data)
        return data
