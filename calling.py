import os
import hail as hl
import bokeh
import bokeh.io


vcf = hl.import_vcf("sig.vcf",skip_invalid_loci = True, array_elements_required=False). write("/scratch/spectre/o/oiao1/data.mt", overwrite= True)


mt =hl.read_matrix_table("/scratch/spectre/o/oiao1/data.mt")
#mt.s.show(10)

mt_grouped = (mt
		.group_rows_by(mt.locus)
		.aggregate_entries(call= hl.agg.collect_as_set(mt.GT))
		.result()
	     )

tb = (mt_grouped
      .entries()
      .export("/scratch/spectre/o/oiao1/geno.txt"))



