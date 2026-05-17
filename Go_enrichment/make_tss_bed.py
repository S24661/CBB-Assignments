import gzip

with gzip.open("human_gene_annotation.tsv.gz", "rt") as fin, \
     open("tss.bed", "w") as fout:

    header = fin.readline()  # skip header

    for line in fin:
        cols = line.strip().split("\t")
        chrom  = "chr" + cols[4]   # chromosome_name
        
        # Fix: Ensembl calls it MT, UCSC calls it chrM
        chrom = chrom.replace("chrMT", "chrM")

        tss    = int(cols[7])       # transcription_start_site
        gene   = cols[6]            # external_gene_name
        
        strand_raw = cols[5]
        strand = "+" if strand_raw == "1" else "-"

        start = tss
        end   = tss + 1
        name  = f"{chrom}@{start}-{end}|{gene}"

        fout.write(f"{chrom}\t{start}\t{end}\t{name}\t.\t{strand}\n")

print("Done! tss.bed created.")
