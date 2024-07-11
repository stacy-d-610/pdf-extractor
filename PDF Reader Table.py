from tabula import read_pdf
#from tabulate import tabulate
import pandas as pd

# Read tables from PDF file
dfs = read_pdf("sample.pdf", pages="all", multiple_tables=True)

# Print each table using tabulate (view in Python)
#for df in dfs:
    #print(tabulate(df, headers='keys', tablefmt='psql'))  # Adjust tablefmt as needed
    #print("\n")  # Separate tables with a newline


# Export tables to an Excel file
excel_filename = "tables_extracted.xlsx"

with pd.ExcelWriter(excel_filename) as writer:
    for i, df in enumerate(dfs, start=1):
        sheet_name = f"Table_{i}"
        df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Tables extracted from PDF have been saved to '{excel_filename}'.")




