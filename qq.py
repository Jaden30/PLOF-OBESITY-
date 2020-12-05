import hail as hl
import pandas as pd 
import bokeh
import bokeh.io
with open ("/scratch/spectre/o/oiao1/final.assoc.logistic") as file:
	df = pd.read_csv(file, sep='\s+', low_memory=False)
	data = pd.DataFrame(df)

table = hl.Table.from_pandas(data)

plot = hl.plot.qq(table.P, label=None,  title = "Quantile Quantile plot for Logistic analysis with PCA(5)", xlabel='Expected -log10(p)', ylabel='Observed -log10(p)', size=6, width=800, height=800)

bokeh.io.show(plot)

