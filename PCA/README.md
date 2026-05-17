# Assignment 2: PCA on Breast Cancer Gene Expression Data

## Background
Breast cancer is categorized based on expression of hormone receptors,
particularly the Estrogen Receptor (ER). ER+ and ER- breast cancers 
respond differently to treatments, making their classification a critical 
clinical problem. This project uses computational methods to explore 
gene expression patterns that distinguish these two subtypes.

The analysis reproduces Figure 1 from the Nature Biotechnology Primer 
(2008) on Principal Component Analysis in gene expression studies.

**Dataset:** GSE5325 from Gene Expression Omnibus (GEO)  
**Reference:** Nature Primer - https://www.nature.com/articles/nbt0308-303

---

## Data Description
| File | Description |
|------|-------------|
| `data/class.tsv` | Sample labels: 1 = ER+ breast cancer, 0 = ER- breast cancer |
| `data/filtered.tsv.gz` | Gene expression matrix for 105 patient samples |
| `data/columns.tsv.gz` | Gene ID to gene name mapping (e.g. 4404 → XBP1) |

---

## Goals

### Part 1 — Scatter Plot (Figure 1a)
- Extract expression levels of **XBP1** and **GATA3** across all 105 patients
- Generate scatter plot with:
  - X-axis: GATA3 expression
  - Y-axis: XBP1 expression
  - Color: ER+ (one color) vs ER- (another color)

### Part 2 — PCA Projection (Figure 1c)
- Run PCA on the full gene expression matrix
- Project all 105 samples onto **PC1**
- Visualize separation between ER+ and ER- samples

---

## Results
- XBP1 and GATA3 show clear separation between ER+ and ER- samples
- PC1 captures the major axis of variation distinguishing the two subtypes

---

## Tools Used
| Tool | Purpose |
|------|---------|
| Python 3 | Main programming language |
| pandas | Data loading and manipulation |
| numpy | Numerical computations |
| matplotlib | Plotting |
| scikit-learn | PCA implementation |

---

## How to Run
1. Open `PCA.ipynb` in Jupyter or Google Colab
2. Make sure data files are in the `data/` folder
3. Run all cells in order
