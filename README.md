# DataCleaning
This project demonstrates a practical approach to data cleaning in Python using pandas and NumPy. The goal of the project is to take a messy dataset in CSV format, identify common data quality issues, clean them systematically, and finally export the cleaned data into an Excel file for further analysis or reporting.

The dataset used in this project was intentionally created to include a variety of issues that analysts often face in real-world scenarios. These include:

-Missing values in numerical and categorical columns.

--Negative values where only positive values make sense (e.g., age or purchase amounts).

---Inconsistent or invalid dates, which are coerced into proper datetime format.

----Duplicate rows that must be removed to ensure accuracy.

-The script provides a menu-driven interface that allows the user to:

--Import and display the raw messy dataset.

---Show detailed file information using df.info().

----Perform a series of data-cleaning operations such as filling missing values, replacing negative values, rounding numbers, parsing dates, and removing duplicates.

-----Display descriptive statistics across all columns to get insights into the cleaned dataset.

------Export the cleaned dataset to an Excel file for reporting or further visualization.
