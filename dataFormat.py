import pandas as pd
import numpy as np
import PyPDF2
import tabula



file_path = ".\Qdoba_Nutrition_Information_2021.pdf"

df = tabula.read_pdf(file_path, pages='all')
print(df)
