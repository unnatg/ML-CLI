# ML-CLI
## Machine Learning Command Line tool to load and preprocess the data for final model building without writting any code.
### data_input.py is used to load the data by passing it as an argument in the command line
### description.py describes the data, displays the data type of each column present in the dataset and also prints out the first and last 5 rows of the dataset
### preprocessing.py
    This python file contains two classes which are Imputation and FeatureScaling
      1) Imputation Class
          This class has the following tasks:
            i) Show the number of null values in each column
            2) Remove column(s)
            3) Fill the null values with mean
            4) Fill the null values with median
            5) Fill the null values with mode
      
      2) FeatureScaling
          This class is used to scale the data using StandardScaler provided by sklearn library.

### categorical.py
    This python file is used to print out the categorical columns present and also perform One Hot Encoding of the categorical columns.
    When the user selects the option to show the categorical columns, the program also asks the user whether the dataset contains a date/date_time column which can be converted to 
    a pandas datetime object. If yes features like year, month, week and day_name would be extracted from the date column.

### main.py
    This is the main file for running the above scripts
    To build the model I have used:
      1) KNeighborsRegressor
      2) SupportVectorRegressor
      3) RandomForestRegressor
      4) ExtraTreesRegressor
      5) XGBRegressor
      6) LGBMRegressor
      7) CatBoostRegressor
    I have used Kfold cross validation with n_splits=10, to evaluate the above models on unseen data.
    The model which gives the highest cross_val_score is selected and printed out on the console with the name of the model that gave the highest score.
    
