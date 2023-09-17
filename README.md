[![Test workflow for Python template](https://github.com/nogibjj/rd278-individual-project1/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/nogibjj/rd278-individual-project1/actions/workflows/pythonapp.yml)

# Descriptive Statistics 

## Goals:
The template created in week one was updatedfor this assignment, particularly polars was added to have descriptive statistics.
A jupyter notebook was added with the same things in the file.

## Functions implemented

Data is loaded using **polars.read_csv**, and the function **dataframe.describe()** is used in module **lib.py** to return the mean, min, percentiles and max.

## Test:
Besides linting and formating, the code had two test:
1. Checks if the file path is a csv file
2. Checks if the output is a polar DataFrame
3. A Notebook.ipynb is created and tested with nbval



# A Scatter plot

Just for the sake of ilustration, a plot was added to see the relationship between the GDP per Capita and the Average income, the data is for Countries and the size of each circle is proportional to the population of each country.

![Scatter Plot](https://github.com/nogibjj/rd278-w3-polars/blob/main/GDP%20per%20Capita%20vs%20Avg%20income%20(size%20proportional%20Population).png)

# Requirements
The project structure must include the following files:
-  Jupyter Notebook with:
- [x] Cells that perform descriptive statistics using Polars or Panda.
- [x] Tested by using nbval plugin for pytest
- [x] Python Script performing the same descriptive statistics using Polars or Panda
- [x] lib.py file that shares the common code between the script and notebook
- Makefile with the following:
- [x] Run all tests (must test notebook and script and lib)
- [x] Formats code with Python black
- [x] Lints code with Ruff
- [x] Installs code via:  pip install -r requirements.txt
- [ ] test_script.py to test script
- [x] test_lib.py to test library
- [ ] Pinned requirements.txt
- [x] GitHub Actions performs all four Makefile commands with badges for each one in the README.md

