import pandas as pd

def read_file(excel):
    df = pd.read_excel(excel)
    print(df.head())
    return df

def insert_line(df, line_data):
    df.append(line_data, ignore_index=True)
    return df

def filter_col(df, col_list):
    select = df[col_list]
    return select

def output(df, excel_name):
    df.to_excel(excel_name)

if __name__ == "__main__":
    data = read_file("inventory.xlsx")
    data = insert_line(data, [])