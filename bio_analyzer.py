import matplotlib.pyplot as plt
from Bio.Seq import Seq

# 1. Load Data
filename = input("Enter the FASTA filename (e.g., tert_promoter.fasta): ")
dna = ""

try:
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                continue
            else:
                dna = dna + line
except FileNotFoundError:
    print("File not found.")
    exit()

# 2. Basic Counting
counts = {}
for letter in dna:
    if letter in counts:
        counts[letter] = counts[letter] + 1
    else:
        counts[letter] = 1

totallength = len(dna)
gc_content = (counts.get('G', 0) + counts.get('C', 0)) / totallength * 100

# 3. Reverse Complement
def get_reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    rev_comp = ""
    for base in reversed(seq):
        if base in complement:
            rev_comp += complement[base]
    return rev_comp

rev_comp_dna = get_reverse_complement(dna)

# 4. CpG Island Detection
cg_count = dna.count("CG")

print(f"\n--- Sequence Analysis: {filename} ---")
print(f"Total Length: {totallength} bp")
print(f"GC Content: {round(gc_content, 2)}%")
print(f"Total CpG Dinucleotides: {cg_count}")
print(f"First 50 bases of Reverse Complement: {rev_comp_dna[:50]}...")

# 5. Advanced Biopython: Translation
dna_seq = Seq(dna)
protein_seq = dna_seq.translate()
print(f"\n--- Protein Translation ---")
print(f"First 50 Amino Acids: {protein_seq[:50]}...")

# 6. Sliding Window GC Content
window_size = 100
gc_windows = []
for i in range(0, len(dna), window_size):
    window = dna[i:i+window_size]
    if len(window) == 0: continue
    g_c = window.count('G') + window.count('C')
    window_gc = (g_c / len(window)) * 100
    gc_windows.append(window_gc)

# 7. Create Two Charts
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Chart 1: Nucleotide Frequency
labels = list(counts.keys())
values = list(counts.values())
ax1.bar(labels, values, color='skyblue')
ax1.set_title(f"Nucleotide Frequency: {filename}")
ax1.set_ylabel("Count")

# Chart 2: Sliding Window GC Content
x_axis = range(0, len(dna), window_size)
ax2.plot(x_axis, gc_windows, color='red')
ax2.set_title("GC Content Across Sequence (Sliding Window)")
ax2.set_xlabel("Position (bp)")
ax2.set_ylabel("GC Content (%)")

plt.tight_layout()
plt.savefig("tert_chart.png", dpi=300)
print("\nChart saved as tert_chart.png")