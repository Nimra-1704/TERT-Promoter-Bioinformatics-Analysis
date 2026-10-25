import matplotlib.pyplot as plt

# 1. Get the filename from the user
filename = input("Enter the FASTA filename (e.g., tert_promoter.fasta): ")

dna = ""
try:
    with open(filename, "r") as file:
        for line in file:
            if line.startswith(">"):
                continue
            else:
                dna = dna + line.strip()
except FileNotFoundError:
    print("File not found. Please check the filename.")
    exit()

# 2. Nucleotide Counting
counts = {}
for letter in dna:
    if letter in counts:
        counts[letter] = counts[letter] + 1
    else:
        counts[letter] = 1

# 3. Calculate Length and GC/AT Content
totallength = len(dna)
gc_content = (counts.get('G', 0) + counts.get('C', 0)) / totallength * 100
at_content = (counts.get('A', 0) + counts.get('T', 0)) / totallength * 100

# 4. Codon Frequency Analysis
codon_counts = {}
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    if len(codon) == 3:
        if codon in codon_counts:
            codon_counts[codon] = codon_counts[codon] + 1
        else:
            codon_counts[codon] = 1

# 5. Print Results
print(f"--- Analysis for {filename} ---")
print(f"Total Sequence Length: {totallength} bp")
print(f"Nucleotide Counts: {counts}")
print(f"GC Content: {round(gc_content, 2)}%")
print(f"AT Content: {round(at_content, 2)}%")

print("\n--- Top 5 Most Frequent Codons ---")
# Sort codons by frequency to get the top 5
sorted_codons = sorted(codon_counts.items(), key=lambda x: x[1], reverse=True)
for codon, count in sorted_codons[:5]:
    print(f"Codon {codon}: {count} times")

# 6. Generate the Chart
labels = list(counts.keys())
values = list(counts.values())

plt.bar(labels, values)
plt.title(f"Nucleotide Frequency: {filename}")
plt.xlabel("Nucleotide")
plt.ylabel("Count")
plt.savefig("tert_chart.png")
print("\nChart saved as tert_chart.png")