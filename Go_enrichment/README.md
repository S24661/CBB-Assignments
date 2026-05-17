# Assignment 1: GO Enrichment Analysis of NRF1 Motif

## Overview
Identifies genes with NRF1 transcription factor binding motif
(GCGC..GCGC) in promoter regions and performs GO enrichment analysis.

## Pipeline
1. Convert gene annotation to BED format (make_tss_bed.py)
2. Extend TSS 500bp upstream using bedtools slop
3. Extract promoter sequences using bedtools getfasta
4. Search for NRF1 motif using Python regex (find_nrf1.py)
5. GO enrichment analysis using clusterProfiler in R

## Results
- 4243 genes found with NRF1 motif in promoter region
- Top enriched processes: mitotic cell cycle, 
  chromosome segregation, RNA splicing

## Tools Used
- bedtools
- Python 3.12
- R / clusterProfiler (Bioconductor)
