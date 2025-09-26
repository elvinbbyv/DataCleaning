import pandas as pd
import numpy as np
def import_csv():
    df = pd.read_csv("messy_dataset_large.csv")
    print("Messy Data csv file imported")
    return df

def display(df):
    print(df)

def show_file_info(df):
    print("\n--- FILE INFO ---")
    print(df.info())

def data_cleaning(df):
    print("\n--- CLEANING DATA ---")
    print("Missing values before:\n", df.isnull().sum())

    df_cleaned = df.fillna(df.mean(numeric_only=True))

    df_cleaned["Name"] = df_cleaned["Name"].fillna("Unknown")

    df_cleaned["PaymentMethod"] = df_cleaned["PaymentMethod"].fillna("Unknown")

    df_cleaned["Age"] = np.where(df_cleaned["Age"] < 0,
                                 df_cleaned["Age"].abs(),
                                 df_cleaned["Age"])
    df_cleaned["Age"] = df_cleaned["Age"].round()

    df_cleaned["PurchaseAmount"] = np.where(df_cleaned["PurchaseAmount"] < 0,
                                            df_cleaned["PurchaseAmount"].abs(),
                                            df_cleaned["PurchaseAmount"])
    df_cleaned["PurchaseAmount"] = df_cleaned["PurchaseAmount"].round()

    df_cleaned["PurchaseDate"] = pd.to_datetime(df_cleaned["PurchaseDate"], errors="coerce")

    df_cleaned = df_cleaned.drop_duplicates()

    print("Missing values after:\n", df_cleaned.isnull().sum())
    return df_cleaned

def statistics(df):
    print("\n--- STATISTICS ---")
    print(df.describe(include="all"))

def export(df, filename="cleaned_dataset_large.xlsx"):
    df.to_excel(filename, index=False)
    print(f"Cleaned data exported to {filename}")


def run_interface(df_original):
    df_cleaned = None

    while True:
        print("\n--- Welcome to CSV Data Cleaning ---")
        print("1. Show Messy Data")
        print("2. Show File Info")
        print("3. Clean the Data")
        print("4. Show Statistics")
        print("5. Export Cleaned data to Excel")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                if df_cleaned is not None:
                    display(df_cleaned)
                else:
                    display(df_original)
            case "2":
                if df_cleaned is not None:
                    show_file_info(df_cleaned)
                else:
                    show_file_info(df_original)
            case "3":
                if df_cleaned is not None:
                    df_cleaned = data_cleaning(df_cleaned)
                else:
                    df_cleaned = data_cleaning(df_original)

            case "4":
                if df_cleaned is not None:
                    statistics(df_cleaned)
                else:
                    statistics(df_original)
            case "5":
                if df_cleaned is not None:
                    export(df_cleaned)
                else:
                    export(df_original)
            case "0":
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

df_main = import_csv()
run_interface(df_main)
