import pandas as pd
import numpy as np
from description import DescribeData

pd.set_option("display.max_columns", None)
pd.set_option('expand_frame_repr', False)


class CategoricalData:
    def __init__(self, data):
        self.tasks = ["\n1. Show categorical columns",
                      "2. Perform One Hot Encoding",
                      "3. Show the first 5 rows and last 5 rows."]
        self.data = data

    def date_time_col(self, column_name):
        # Convert the date time column to pd.datetime object
        # Extract year, month, week and day_name
        # Covert the day_name to One Hot Vector
        self.data[column_name] = pd.to_datetime(self.data[column_name])
        self.data["year"] = self.data[column_name].dt.year
        self.data["month"] = self.data[column_name].dt.month
        self.data["week"] = self.data[column_name].dt.isocalendar().week.astype("uint8")
        self.data["day_name"] = self.data[column_name].dt.day_name()
        self.data = pd.get_dummies(data=self.data, columns=["day_name"])
        self.data.drop(column_name, axis=1, inplace=True)

    def describe_categorical(self):
        print("The categorical columns are: ")
        categorical_columns = self.data.select_dtypes(exclude=np.number).columns
        for column in categorical_columns:
            print(column, end=" ")
        print("\n")
        check_date_time_col = input("Does the dataset contain a date time column: ")
        if check_date_time_col == "yes":
            col_name = input("Enter the name of the column: ")
            self.date_time_col(col_name)
            print("Date column has been dropped and new features such as year, day_name, week have been added "
                  "to the dataset.")
        if len(categorical_columns) == 0:
            print("No categorical column is present in the dataset.")
        else:
            print('\n{0:<20}'.format("Categorical Column") + '{0:<5}'.format("Unique Values"))
            for column in self.data.select_dtypes(exclude=np.number).columns:
                print("{0:<20}".format(column) + "{0:<5}".format(self.data[column].nunique()))

    # Function to encode a column or multiple column
    def encoder(self):
        categorical_columns = self.data.select_dtypes(exclude=np.number).columns
        if len(categorical_columns) == 0:
            print("There are no categorical columns present in the dataset.\n")
        else:
            print("Encoding the categorical columns...")
            self.data = pd.get_dummies(data=self.data, columns=categorical_columns)
            print("The categorical columns have been One Hot Encoded")

    # Function of Encoder class to run the above tasks
    def categorical_main(self):
        while True:
            print("\nTasks available are: ")
            for task in self.tasks:
                print(task)

            while True:
                try:
                    choice = int(input("Enter what you want to do. (-1 to go back) "))
                except ValueError:
                    print("Integer value is expected. Try again.")
                    continue
                break

            if choice == -1:
                break

            elif choice == 1:
                self.describe_categorical()

            elif choice == 2:
                self.encoder()
                # Handle missing values in categorical columns as well
                categorical_columns = self.data.select_dtypes(exclude=np.number)
                for column in categorical_columns:
                    self.data[column].fillna(method="ffill", inplace=True)

            elif choice == 3:
                DescribeData.print_data(self)  # Show the first 5 and last 5 rows.

            else:
                print("Wrong choice entered.")
        return self.data


