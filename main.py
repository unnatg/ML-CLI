import pandas as pd
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import KFold, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor
from data_input import InputData
from description import DescribeData
from preprocessing import Imputation, FeatureScaling
from categorical_data import CategoricalData

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


class Predictor:

    def __init__(self):
        self.tasks = ["\n1. Data Description",
                      "2. Handling null values",
                      "3. Encoding Categorical columns",
                      "4. Scaling the dataset",
                      "5. Build the model."]
        self.data = InputData().input_data()
        print("Dataset has been loaded successfully.")
        self.training_data = pd.DataFrame()
        self.training_labels = pd.DataFrame()

    def remove_target_column(self):
        for column in self.data.columns:
            print(column, end="  ")

        while True:
            column = input("\nWhich is the target variable:(Press -1 to exit)  ").lower()
            if column == "-1":
                exit()
            choice = input("Are you sure?(y/n) ")
            if choice == "y" or choice == "Y":
                try:
                    self.training_data = self.data.drop([column], axis=1)
                    self.training_labels = self.data[column]
                except KeyError:
                    print("No column present with this name. Try again......\U0001F974")
                    continue
                print("Done.......\U0001F601")
                break
            else:
                print("Try again with the correct column name...\U0001F974")
        return

    def model(self):
        print("Training the model, please wait....")
        models = [
            KNeighborsRegressor(n_neighbors=4),
            SVR(kernel="rbf"),
            RandomForestRegressor(n_estimators=700, n_jobs=-1),
            ExtraTreesRegressor(n_estimators=500, n_jobs=-1),
            XGBRegressor(n_jobs=-1),
            LGBMRegressor(n_jobs=-1),
            CatBoostRegressor(learning_rate=1,
                              loss_function="RMSE")
        ]
        names = [
            "KNeighborsRegressor",
            "SupportVectorMachine",
            "RandomForestRegressor",
            "ExtraTreesRegressor",
            "XGBRegressor",
            "LGBMRegressor",
            "CatBoostRegressor"
        ]
        model_scores = []
        kf = KFold(n_splits=10, shuffle=True, random_state=42)
        for name, model in zip(names, models):
            cv_score = cross_val_score(model, self.training_data, self.training_labels, cv=kf, scoring="r2",
                                       n_jobs=-1, verbose=0)
            model_scores.append(cv_score.mean())

        scores_dataframe = pd.DataFrame(model_scores, index=names, columns=["Score"])
        max_val = scores_dataframe["Score"].idxmax()
        max_score = scores_dataframe.loc[max_val, "Score"]
        print("\nHighest score has been achieved by {0} and it is {1}".format(max_val, max_score))

    def predictor_main(self):
        self.remove_target_column()
        while True:
            print("\nTasks: ")
            for task in self.tasks:
                print(task)

            while True:
                try:
                    choice = int(input("Enter your choice. (Enter -1 to exit.) "))
                except ValueError:
                    print("Enter integer values only")
                    continue
                break

            if choice == -1:
                exit()

            elif choice == 1:
                DescribeData(self.training_data).describe_data()

            elif choice == 2:
                self.training_data = Imputation(self.training_data).imputer()

            elif choice == 3:
                self.training_data = CategoricalData(self.training_data).categorical_main()

            elif choice == 4:
                self.training_data = FeatureScaling(self.training_data).scaling()

            elif choice == 5:
                self.model()

            else:
                print("Wrong choice entered. ")


if __name__ == "__main__":
    Predictor().predictor_main()