import pandas as pd
import xlsxwriter

with open ("/home/oiao1/") as csv:
	df = pd.read_csv(csv)


writer = pd.ExcelWriter("/home/oiao1/", engine ="xlsxwriter")
df.to_excel(writer, "Sheet1")
writer.save()
