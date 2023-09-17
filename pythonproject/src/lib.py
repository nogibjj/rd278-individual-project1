"""
This module takes a csv and returns statistics about it
"""
import matplotlib.pyplot as plt
import polars as pl
import os

def is_int_or_float(value):
    return isinstance(value, (int, float))

def test_float_int(vector):
    # Use the apply method to check the data types
    results = vector.apply(is_int_or_float)

    #Allowance of 90%
    THRESHOLD=.9

    allowance=sum(results)/len(vector)>=THRESHOLD

    return allowance
    

def is_csv_file(file_path):
    # Extract the file extension from the file path
    file_extension = os.path.splitext(file_path)[-1].lower()
    return file_extension == ".csv"

def is_png_file(file_path):
    # Extract the file extension from the file path
    file_extension = os.path.splitext(file_path)[-1].lower()
    return file_extension == ".png"

def descriptive_statistics(directory_path):
    """
    Calculate descriptive statistics for a DataFrame.

    Parameters:
    data (pl.DataFrame): The input Polars DataFrame,
    which must contain numeric data.

    Returns:
    pl.DataFrame: A DataFrame containing descriptive statistics.
    """
    if is_csv_file(directory_path):
        data=pl.read_csv(directory_path)
        results=data.describe()
        results.write_csv('results.csv')

        return data,results
    else:
        raise  NotADirectoryError("This is not a valid .csv file")


def generating_plot(data, x_variable, y_variable, title, size=None):
    """
    Parameters:
        data: Polar DataFrame
        x_variable: String of the variable in axis X from data
        y_variable: String of the variable in axis Y from data
        size: String if a variable is required to
        title: String for the plot title
    """

    if test_float_int(data[x_variable]) and test_float_int(data[y_variable]) and (test_float_int(data[size]) or size is None):

        if size is None:
            area = 1
        else:
            area = data[size] * 10 / data[size].mean()

        # Labeling
        plt.scatter(data[x_variable], data[y_variable], s=area, alpha=0.5)
        plt.xlabel(x_variable)
        plt.ylabel(y_variable)
        plt.title(title)
        plt.show()
        plt.savefig(title + ".png", dpi=300, bbox_inches="tight")

    else:
        raise ValueError(f"It is possible that {x_variable}, {y_variable}, or {size} ar not float or int")