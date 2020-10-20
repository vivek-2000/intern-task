import pandas as pd
import subprocess
# using subprocess to run script.py and creating csv file

subprocess.call("scrapy runspider script.py -o report.csv", shell=True)

# using  dataframe to convert csv into xls
read_file = pd.read_csv ("report.csv")
read_file.to_excel ("report.xls", index = None, header=True)