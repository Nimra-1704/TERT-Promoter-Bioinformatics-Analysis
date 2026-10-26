# TERT Promoter Bioinformatics Analysis 

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23659429.svg)](https://doi.org/10.5281/zenodo.23659429)

**NCBI Accession:** AF097365.1

## Background
The TERT (Telomerase Reverse Transcriptase) gene promoter is a critical region for cellular aging and oncogenesis. Its regulation is heavily influenced by epigenetic modifications (DNA methylation), which occur primarily at CpG islands. A high GC content in the promoter indicates the presence of these islands. Furthermore, GC-rich regions present structural challenges for CRISPR-Cas9 genome editing efficiency.

## Tool Capabilities
This Python tool (`bio_analyzer.py`) analyzes FASTA sequences to provide:
- Nucleotide frequency counting (A, T, C, G)
- GC Content and AT Content calculation
- Codon frequency analysis
- Bar chart visualization of nucleotide composition

## Application and Results
Analyzing the human TERT promoter sequence yielded the following results:
- **Total Sequence Length:** 4356 bp
- **GC Content:** 58.59%
- **CpG Dinucleotides:** 218 (High density indicates a strong epigenetic regulatory region)
- **Protein Translation (first 50 aa):** EFT*LRTSCTHSRPRPTPAVLF**LQSREIPAKMSFN... 

The high GC content (58.59%) and the presence of 218 CpG sites confirm the promoter is a hotspot for DNA methylation. From a CRISPR perspective, this high GC content indicates that standard Cas9 editing may face structural barriers, requiring high-fidelity enzymes. The sliding window chart shows the fluctuating GC density across the sequence.

![Nucleotide Frequency Chart](tert_chart.png)

---
*Developed by Nimra (BS Biochemistry Graduate, 2026)*