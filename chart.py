import pandas as pd 
import matplotlib.pyplot as plot
# to import pages 
from matplotlib.backends.backend_pdf import PdfPages
#Spreadsheet to a filename 
#Dependencies on xlrd
excel_file = "/home/oiao1/GSE.xlsx"

#load spreadsheet

xl = pd.ExcelFile(excel_file)
#load a sheet into a dataframe 

#GSE_GSM = xl.parse("Sheet2")
#GSE_GSR = xl.parse("Sheet3")
GSE_SOO = xl.parse("Sheet4")



with PdfPages("/home/oiao1/GSO.pdf") as export_pdf:
    GSE_SOO.plot.bar (x="GSE", y= ["obese","Non-obese"], title = "Number of obese and non obese samples in each included study" )
    plot.tight_layout()
    export_pdf.savefig()
    plot.close()
  
   

"""
    GSE_GSM.plot.bar(x="GSE", y="GSM", title ="Number of samples (GSM) per included study (GSE)")
    plot.tight_layout()
    export_pdf.savefig()
    plot.close( )
 
    GSE_GSR.plot.bar (x="GSE", y= ["GSM","no_of_SRR"], title = "Number of samples,retrieved sequence read run per included study" )
    plot.tight_layout()
    export_pdf.savefig()
    plot.close()

    

"""    

