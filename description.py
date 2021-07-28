import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option('expand_frame_repr', False)

class DescribeData:
    def __init__(self, data):
        self.tasks = ["\n1. Describe a specific column/ Describe the dataset",
                      "2. Data type and total number of values in each column",
                      "3. Show the dataset (Top five rows and last five rows"]
        self.data = data

    # Function to print the first 5 rows and last 5 rows
    def print_data(self):
            print(self.data.head()) # Top 5 rows
            print("\n\n")
            print(self.data.tail()) # Last 5 rows

    # Function to describe the dataset
    def describe_data(self):
        while(True):
            print("Tasks")
            for task in self.tasks:
                print(task)
            while(True):
                try:
                    choice = int(input("\nWhat do you want to do ? (Press -1 to go back) "))
                except ValueError:
                    print("Integer values only.")
                    continue
                break

            if choice==-1:
                break

            elif choice==1:
                for columns in self.data.columns:
                    print(columns, end=" ")
                while(1):
                    numerical_columns = self.data.select_dtypes(include=np.number).columns # Select numerical columns
                    categorical_columns = self.data.select_dtypes(exclude=np.number).columns # Select categorical columns
                    print("There are {0} numerical columns, which are: ".format(len(numerical_columns)))
                    for columns in numerical_columns:
                        print(columns, end=" ")
                    print("\n")
                    print("There are {0} categorical columns, which are: ".format(len(categorical_columns)))
                    for columns in categorical_columns:
                        print(columns, end=" ")
                    describe_column = input("\nEnter the name of the column or enter all for full dataset description: ")
                    try:
                        if describe_column=="all":
                            print(self.data.describe().T)
                        else:
                            print(self.data[describe_column].describe())
                    except KeyError:
                        print("No column with this name is present in the dataset.")
                        continue
                    break

            elif choice==2:
                print(self.data.info())

            elif choice==3:
                self.print_data()

            else:
                print("You have entered a wrong choice. Try again!")
