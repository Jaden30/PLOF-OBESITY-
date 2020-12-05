
 data <- read.csv(file = "/home/oiao1/Gnomad/phe.csv", sep=" ", header = T)
 write.table(data,file="/home/oiao1/Gnomad/phe", sep= " " ,row.names = F, quote=FALSE)