import pandas as pd
from pandas import *
import tabula
import csv



print("Converting data please wait.")
file_path = ".\Qdoba_Nutrition_Information_2021.pdf"
pd.options.display.max_columns = None
df = tabula.read_pdf(file_path, pages='all')
tabula.convert_into(file_path, 'qdobaconverted.csv', output_format='csv', pages = 'all')


with open('qdobaconverted.csv') as csv_file:
     csv_reader = csv.reader(csv_file)
     dataf = pd.DataFrame([csv_reader], index = None, )



print("Data has been converted.")



#for val in list(dataf[2]):
#    print(val)
