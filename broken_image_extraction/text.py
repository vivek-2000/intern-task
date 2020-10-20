import pandas as pd
import subprocess
subprocess.call("scrapy runspider script.py -o report.csv", shell=True)
read_file = pd.read_csv ("report.csv")
read_file.to_excel ("report.xls", index = None, header=True)