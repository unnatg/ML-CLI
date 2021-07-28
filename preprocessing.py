import pandas as pd
from description import DescribeData
from sklearn.preprocessing import StandardScaler

class Imputation:

    def __init__(self, data):
        self.tasks = ["\n1. Show the number of null values in each column.",
                      "2. Remove column(s).",
                      "3. Fill null values with mean.",
                      "4. Fill null values with median",
                      "5. Fill null values with mode",
                      "6. Show the dataset."]
        self.data = data

    def null_values(self):
        print("Null values present in each column: ")
        for column in self.data.columns:
            # Print out the null value associated with each column
            print("{0:<25}".format(column) + "{0:<5}".format(sum(pd.isnull(self.data[column]))))
        print("\n")
        return

    def remove_columns(self):
        for col in self.data.columns:
            print(col, end=" ")
        print("\n")
        remove_cols = str(input("Enter the columns you wish to drop/remove from the dataset: (If you wish to remove "
                                "multiple columns enter them with a space in a single line separated by a comma) ")).split(",")
        print("The following columns would be dropped from the dataset: ", remove_cols)
        try:
            self.data.drop(remove_cols, axis=1, inplace=True)
            print("The columns have been dropped.")
        except KeyError:
            print("One or more column is not present in the dataset.")

    def fill_with_mean(self):
        while True:
            self.null_values()
            print("\n")
            column_name = input("Enter the column name: (Enter -1 to go back) ")
            if column_name == -1:
                break
            confirm = input("Enter yes to confirm: ")
            if confirm == "yes":
                try:
                    self.data[column_name] = self.data[column_name].fillna(self.data[column_name].mean())
                except KeyError:
                    if self.data[column_name].dtype.name == "object":
                        print("This column cannot be filled with mean value since it is a categorical column. "
                              "\n(Categorical columns containing missing values would be filled by forward fill "
                              "method.)")
                        continue
                print("Done....")
                break
            else:
                print("Not fill the missing value in the column entered with mean of values in the column.")
        return

    def fill_with_median(self):
        while True:
            self.null_values()
            print("\n")
            column_name = input("Enter the column name: (Enter -1 to go back) ")
            if column_name == -1:
                break
            confirm = input("Enter yes to confirm: ")
            if confirm == "yes":
                try:
                    self.data[column_name] = self.data[column_name].fillna(self.data[column_name].median())
                except KeyError:
                    if self.data[column_name].dtype.name == "object":
                        print("This column cannot be filled with mean value since it is a categorical column. "
                              "\n(Categorical columns containing missing values would be filled by forward fill "
                              "method.)")
                        continue
                print("Done....")
                break
            else:
                print("Not fill the missing value in the column entered with mean of values in the column.")
        return

    def fill_with_mode(self):
        while True:
            self.null_values()
            print("\n")
            column_name = input("Enter the column name: (Enter -1 to go back) ")
            if column_name == -1:
                break
            confirm = input("Enter yes to confirm: ")
            if confirm == "yes":
                try:
                    self.data[column_name] = self.data[column_name].fillna(self.data[column_name].mode())
                except KeyError:
                    if self.data[column_name].dtype.name == "object":
                        print("This column cannot be filled with mean value since it is a categorical column. "
                              "\n(Categorical columns containing missing values would be filled by forward fill "
                              "method.)")
                        continue
                print("Done....")
                break
            else:
                print("Not fill the missing value in the column entered with mean of values in the column.")
        return

    def imputer(self):
        while True:
            print("\nImputation tasks are: ")
            for task in self.tasks:
                print(task)
            while True:
                try:
                    choice = int(input("Enter your choice: (Enter -1 to go back) "))
                except ValueError:
                    print("Enter integer values only.")
                    continue
                break

            if choice == -1:
                break

            elif choice == 1:
                self.null_values()

            elif choice == 2:
                self.remove_columns()

            elif choice == 3:
                self.fill_with_mean()

            elif choice == 4:
                self.fill_with_median()

            elif choice == 5:
                self.fill_with_mode()

            elif choice == 6:
                DescribeData.print_data(self)

            else:
                print("Wrong choice entered. Try again")

        return self.data


class FeatureScaling:
    # Normalization typically means rescale the values into a range of [0,1].
    # Standardization typically means rescale the data to have a mean of 0 and a standard deviation of 1 unit variance.
    def __init__(self, data):
        self.data = data

    def scale_data(self):
        self.data = StandardScaler().fit_transform(self.data)

    def scaling(self):
        self.scale_data()
        return self.data


