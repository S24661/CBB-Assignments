import re

pattern = re.compile(r'GCGC[ATGCN]{2}GCGC', re.IGNORECASE)

genes_with_motif = set()
current_gene = None
current_seq = []

with open("tss_upstream_500.fa") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            # Check previous sequence
            if current_gene and current_seq:
                seq = "".join(current_seq)
                if pattern.search(seq):
                    genes_with_motif.add(current_gene)
            # Get gene name from header
            # Header looks like: >chrM@577-578|MT-TF::chrM:77-578(+)
            header = line.split("|")[1].split("::")[0]
            current_gene = header
            current_seq = []
        else:
            current_seq.append(line)

    # Check last sequence
    if current_gene and current_seq:
        seq = "".join(current_seq)
        if pattern.search(seq):
            genes_with_motif.add(current_gene)

import os
os.makedirs("gene_list_tss_upstream_with_pattern", exist_ok=True)

outfile = "gene_list_tss_upstream_with_pattern/optimal_site_nrf1_in_hg38_tss_upstream_500.genes.tsv"
with open(outfile, "w") as out:
    for gene in sorted(genes_with_motif):
        out.write(gene + "\n")

print(f"Total genes with NRF1 motif: {len(genes_with_motif)}")
