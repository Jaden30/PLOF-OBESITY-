#!/bin/bash
# fetching fastq files 


#PBS -N GSE95640-Fix
#PBS -l walltime=36:00:00
#PBS -l nodes=1:ppn=8
#PBS -l vmem=60gb
#PBS -m bea
#PBS -M oiao1@le.ac.uk
 
cd /scratch/spectre/o/oiao1/GSE95640

module load sratoolkit/2.9.6

for (( i =72; i <=95; i++ ))
  do
  fastq-dump --accession SRR53104$i
done

cd /scratch/spectre/o/oiao1/GSE95640

module load sratoolkit/2.9.6

for (( i =10#07; i <=47; i++ ))
  do
  fastq-dump --accession SRR53105$i
done

