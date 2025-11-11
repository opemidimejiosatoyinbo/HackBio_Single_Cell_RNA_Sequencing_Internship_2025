"""
HackBio Internship - Stage 1 Surprise Task
Team: Glycine

# Task: Plot 'log2FoldChange' vs 'log10(Padj)' the DEG results.
# Author: Opemidimeji Osatoyinbo
# GitHub: https://github.com/opemidimejiosatoyinbo
# LinkedIn: https://linkedin.com/in/opemidimejiosatoyinbo
"""
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

DEG_URL = ("https://raw.githubusercontent.com/HackBio-Internship/"
           "2025_project_collection/refs/heads/main/Python/Dataset/"
           "hbr_uhr_deg_chr22_with_significance.csv")

sb.set(style="whitegrid", context="notebook")

def plot_volcano(deg_url: str = DEG_URL,
                 lfc_col: str = "log2FoldChange",
                 padj_col: str = "padj",
                 out_file: str = "fig_1B_volcano.png",
                 lfc_cutoff: float = 1.0):
    """
    Create a volcano plot from DEG results.

    Parameters
    ----------
    deg_url : str
        URL to DEG CSV. Expected columns: gene, log2FoldChange, padj, (optional Significance).
    lfc_col : str
        Column name for log2 fold change.
    padj_col : str
        Column name for adjusted p-value.
    out_file : str
        Output filename.
    lfc_cutoff : float
        Threshold for considering up/down regulation.
    """
    deg = pd.read_csv(deg_url)
    # ensure padj exists
    if padj_col not in deg.columns:
        # try to detect padj-like column
        possible = [c for c in deg.columns if 'pad' in c.lower() or 'adj' in c.lower()]
        if possible:
            padj_col = possible[0]
            print("Using detected padj column:", padj_col)
        else:
            raise ValueError("Adjusted p-value column (padj) not found.")

    # replace zeros (avoid -log10(0))
    deg[padj_col] = deg[padj_col].apply(lambda x: np.nextafter(0, 1) if x <= 0 else x)

    # determine significance (use provided column if exists)
    sig_col = None
    for c in ['Significance', 'significance', 'sig']:
        if c in deg.columns:
            sig_col = c
            break

    if sig_col:
        deg['significance'] = deg[sig_col].astype(str).str.lower().replace({
            'upregulated': 'up', 'downregulated': 'down'
        }).fillna('ns')
    else:
        deg['significance'] = 'ns'
        deg.loc[(deg[lfc_col] >= lfc_cutoff) & (deg[padj_col] < 0.05), 'significance'] = 'up'
        deg.loc[(deg[lfc_col] <= -lfc_cutoff) & (deg[padj_col] < 0.05), 'significance'] = 'down'

    color_map = {'up': 'green', 'down': 'orange', 'ns': 'grey'}
    colors = deg['significance'].map(color_map).fillna('grey')

    plt.figure(figsize=(9, 6))
    plt.scatter(deg[lfc_col], -np.log10(deg[padj_col]), c=colors, s=20, alpha=0.7)
    plt.axvline(x=lfc_cutoff, color='black', linestyle='--')
    plt.axvline(x=-lfc_cutoff, color='black', linestyle='--')
    plt.xlabel("log2FoldChange")
    plt.ylabel("-log10(padj)")
    plt.title("Volcano Plot (Chr22)")

    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='green', label='Upregulated', markersize=6),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', label='Downregulated', markersize=6),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='grey', label='Not significant', markersize=6)
    ]
    plt.legend(handles=legend_elements, title="Significance", loc="upper right")
    plt.tight_layout()
    plt.savefig(out_file, dpi=300, bbox_inches="tight")
    plt.show()
    print("Saved volcano plot to", out_file)


if __name__ == "__main__":
    plot_volcano()