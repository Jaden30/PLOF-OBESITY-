# adding chr to my Gnomad to make it "usable"
myStr = "chr"
with open("/home/oiao1/Gnomad/gnomad.v2.1.1.all_lofs.txt", "r") as file: 
		original = file.readlines()
		with open("/home/oiao1/Gnomad/Gnomad.txt", "w") as out:
			for line in original:
				file.seek(0,0)
				out.write("chr" + line)

		out.close()
file.close()
