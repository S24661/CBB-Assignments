# Assignment 3: Hidden Markov Models & Viterbi Algorithm for Gene Structure Prediction

## Background

One of the fundamental problems in computational biology is identifying
the structure of genes from raw DNA sequences — specifically, finding
where **exons** (coding regions) and **introns** (non-coding regions) are
located. This is not trivial because the genome is long and the signals
that mark exon-intron boundaries are subtle.

**Hidden Markov Models (HMMs)** are a powerful statistical framework
for solving this problem. The key idea is:

- The **observed data** is the DNA sequence (A, C, G, T)
- The **hidden states** are the biological labels (Exon, Intron, Splice site)
- The model learns the probabilities of transitioning between states
  and emitting each nucleotide

The **Viterbi Algorithm** is then used to find the most probable sequence
of hidden states (gene structure) that explains the observed DNA sequence.

---

## Model Description

### Hidden States

| State | Symbol | Meaning |
|-------|--------|---------|
| Start | `s` | Beginning of sequence |
| Exon | `E` | Coding region |
| Donor splice site | `5` | Exon → Intron boundary (GT signal) |
| Intron | `I` | Non-coding region |
| End | `e` | End of sequence |

### State Transition Probabilities

```
s  → E  : 1.0   (always start in exon)
E  → E  : 0.9   (stay in exon)
E  → 5  : 0.1   (transition to splice donor)
5  → I  : 1.0   (always enter intron after splice)
I  → I  : 0.9   (stay in intron)
I  → e  : 0.1   (end intron / terminate)
```

### Emission Probabilities

| State | A | C | G | T |
|-------|---|---|---|---|
| Exon (E) | 0.25 | 0.25 | 0.25 | 0.25 | (uniform) |
| Donor (5) | 0.05 | 0.00 | 0.95 | 0.00 | (strong G signal) |
| Intron (I) | 0.40 | 0.10 | 0.10 | 0.40 | (AT-rich) |

---

## Query Sequence

```
CTTCATGTGAAAGCAGACGTAAGTCA  (26 nucleotides)
```

---

## Goals

### Part 1 — Manual Path Comparison
Compute and compare log-probabilities for different possible state paths:
- `EEEEEE5IIIIIIIIIIIIIIIIIII` (splice at position 6)
- `EEEEEEEE5IIIIIIIIIIIIIIIII` (splice at position 8)
- `EEEEEEEEEEEE5IIIIIIIIIIIII` (splice at position 12)
- `EEEEEEEEEEEEEEE5IIIIIIIIII` (splice at position 15)
- `EEEEEEEEEEEEEEEEEE5IIIIIII` (splice at position 18)
- `EEEEEEEEEEEEEEEEEEEEEE5III` (splice at position 22)
- `EEEEEEEEEEEEEEEEEEEEEEEEEE` (all exon, no intron)

### Part 2 — Viterbi Algorithm Implementation
- Design and populate the **Viterbi Value Matrix** (rows = states, cols = sequence positions)
- Design and populate the **Viterbi Trace Matrix** (for traceback)
- All calculations done in **log scale** to avoid numerical underflow

### Part 3 — Traceback
- Find the most probable hidden state path using traceback
- Interpret the biological meaning of the result

---

## Results

```
Query sequence : CTTCATGTGAAAGCAGACGTAAGTCA
Best state path: EEEEEEEEEEEEEEEEEEEEEEEEEE
Max log-prob   : -36.39
```

**Interpretation:** The Viterbi algorithm finds the all-exon path as most
probable. The sequence does not contain a strong enough GT donor signal
to overcome the E→5 transition penalty (log(0.1) = -2.303). This means
the model predicts no intron in this sequence.

---

## Key Concepts Learned

| Concept | Description |
|---------|-------------|
| HMM | Statistical model with hidden states and observed emissions |
| Viterbi Algorithm | Dynamic programming to find the most probable state path |
| Log probabilities | Used to prevent numerical underflow in long sequences |
| Traceback | Recovering the optimal path by backtracking through the trace matrix |
| Splice sites | GT-AG rule: donor site (GT) marks exon→intron boundary |

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Python 3 | Main programming language |
| NumPy | Matrix operations for Viterbi matrices |
| math | Log probability calculations |

---

## How to Run

1. Open `HMM_Virtebi.ipynb` in Jupyter or Google Colab
2. Run all cells in order
3. The final cell prints the optimal state path and its log-probability

---

## File Structure

```
assignment3_hmm/
├── README.md               ← this file
└── HMM_Virtebi.ipynb       ← full implementation
```
