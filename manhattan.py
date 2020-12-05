import hail as hl
import pandas as pd
import bokeh
import bokeh.io
with open ("/scratch/spectre/o/oiao1/JOBS/final.assoc.logistic") as file:
	df = pd.read_csv(file, sep='\s+', low_memory=False)
	data = pd.DataFrame(df)

table = hl.Table.from_pandas(data)
#table.show()
#Ref_genome = hl.genetics.ReferenceGenome.from_fasta_file("Mygenome", "/scratch/spectre/o/oiao1/Gnomad/ensgrch37toplevel.fa.gz", "/scratch/spectre/o/oiao1/Gnomad/ensgrch37toplevel.fa.gz.fai")


hover_fields = dict([("alleles", table.A1)]) 
plot = hl.plot.manhattan(table.P, hl.locus(hl.str(table.CHR), hl.int32(table.BP)), hover_fields= hover_fields, collect_all=True, title= "logistic Association analysis with PCA 5, significant line )", significance_line = 7.27e-07)
bokeh.io.show(plot)

