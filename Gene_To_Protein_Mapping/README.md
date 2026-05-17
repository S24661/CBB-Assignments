# Assignment 4: From Gene to Protein — Coordinate Mapping with Ensembl

## Background

Every human gene goes through a journey: **DNA → RNA → Protein**. But
the relationship between these layers is not straightforward. A single
gene can produce **multiple transcripts** (alternative splicing), and
only some transcripts are translated into **proteins**. Understanding
which parts of the genome encode which proteins — and exactly where —
is a fundamental problem in genomics.

This project explores that journey using the **HLA-A gene** as a case
study. HLA-A (Human Leukocyte Antigen A) is one of the most important
immune system genes in humans — it presents peptide fragments to T-cells
and plays a critical role in organ transplantation compatibility and
immune response.

We use **Ensembl's coordinate mapping tools** in R to:
- Retrieve all human genes, transcripts, and proteins
- Map HLA-A protein sequences back to their genomic coordinates
- Visualize the gene structure in **IGV (Integrative Genomics Viewer)**

---

## The Central Dogma in Numbers

| Level | Count (Human) |
|-------|--------------|
| Genes (ENSG) | ~70,000 |
| Transcripts (ENST) | ~280,000 |
| Proteins (ENSP) | ~100,000 |

> One gene → many transcripts → fewer proteins (not all transcripts are translated)

---

## Case Study: HLA-A Gene

| Property | Value |
|----------|-------|
| Gene ID | `ENSG00000206503` |
| Location | Chromosome 6 |
| Function | Immune peptide presentation (MHC Class I) |
| Why important | Organ transplant matching, cancer immunotherapy, vaccine design |

---

## Goals

### Part 1 — Retrieve All Human Genes, Transcripts, Proteins
- Connect to **Ensembl 110** database via `AnnotationHub`
- Extract all human gene IDs (`ENSG...`)
- Extract all human transcript IDs (`ENST...`)
- Extract all human protein IDs (`ENSP...`)
- Save each as a `.tsv` file

### Part 2 — HLA-A Transcripts and Proteins
- Filter all transcripts to HLA-A only
- Filter all proteins to HLA-A only
- Inspect transcript biotypes and CDS coordinates

### Part 3 — Protein → Genome Coordinate Mapping
- Map each HLA-A protein sequence back to its **genomic coordinates**
- Use `proteinToGenome()` from `ensembldb`
- Identify which exons encode which parts of the protein
- Save a per-protein summary table

### Part 4 — Transcript → Genome Coordinate Mapping
- Map each HLA-A transcript to its **genomic coordinates**
- Use `transcriptToGenome()` from `ensembldb`
- Account for splicing (sum of exon widths = actual transcript length)

### Part 5 — IGV Visualization
- Load the genome coordinate mappings into **IGV**
- Visualize the exon structure of HLA-A transcripts
- Take IGV snapshots showing gene structure

---

## Output Files Generated

| File | Description |
|------|-------------|
| `all_human_genes.tsv` | All human gene IDs (ENSG) |
| `all_human_transcripts.tsv` | All human transcript IDs (ENST) |
| `all_human_proteins.tsv` | All human protein IDs (ENSP) |
| `HLAA_transcripts.tsv` | All HLA-A transcripts with biotype and coordinates |
| `HLAA_proteins.tsv` | All HLA-A protein sequences |
| `HLAA_protein_to_genome_map.tsv` | Protein → genome coordinate mapping |
| `HLAA_protein_summary.tsv` | Per-protein summary (chromosome, start, end, exon count) |
| `HLAA_transcript_to_genome_map.tsv` | Transcript → genome coordinate mapping |
| `IGV_snapshot.png` | IGV visualization of HLA-A gene structure |

---

## Key Concepts Learned

| Concept | Description |
|---------|-------------|
| ENSG / ENST / ENSP | Ensembl IDs for genes, transcripts, proteins |
| Alternative splicing | One gene → multiple transcripts via different exon combinations |
| CDS | Coding sequence — the part of mRNA that gets translated |
| `proteinToGenome()` | Maps amino acid positions → genomic coordinates |
| `transcriptToGenome()` | Maps mRNA positions → genomic coordinates |
| IGV | Integrative Genomics Viewer — tool to visualize genome tracks |
| IRanges | R object for representing genomic intervals |

---

## Tools Used

| Tool | Purpose |
|------|---------|
| R | Main programming language |
| `ensembldb` | Ensembl database queries and coordinate mapping |
| `AnnotationHub` | Access to Ensembl 110 human annotation (AH119325) |
| `IRanges` | Genomic interval arithmetic |
| IGV | Visual inspection of gene structure |

---

## How to Run

1. Open `GeneToProtein.ipynb` in Google Colab or Jupyter
2. Run cells in order — first cell installs required R packages
3. Allow ~5 minutes for `AnnotationHub` to download Ensembl 110 database
4. All output `.tsv` files will be saved in the working directory
5. Load `HLAA_transcript_to_genome_map.tsv` into IGV to view gene structure

---

## IGV Snapshot

The IGV snapshot below shows the exon-intron structure of HLA-A transcripts
mapped back to chromosome 6. Each block represents an exon, and the
gaps between blocks represent introns that are spliced out.

> See `IGV_snapshot.png` in this folder

---

## File Structure

```
assignment4_gene_to_protein/
├── README.md                            ← this file
├── GeneToProtein.ipynb                  ← full R analysis notebook
├── IGV_snapshot.png                     ← IGV visualization of HLA-A
├── all_human_genes.tsv                  ← all ENSG IDs
├── all_human_transcripts.tsv            ← all ENST IDs
├── all_human_proteins.tsv               ← all ENSP IDs
├── HLAA_transcripts.tsv                 ← HLA-A transcripts
├── HLAA_proteins.tsv                    ← HLA-A protein sequences
├── HLAA_protein_to_genome_map.tsv       ← protein coordinate mapping
├── HLAA_protein_summary.tsv             ← per-protein summary
└── HLAA_transcript_to_genome_map.tsv    ← transcript coordinate mapping
```
