"""
HackBio Internship - Stage 1 Surprise Task
Team: Glycine

# Task: Use the normalized gene expression dataset to plot a clustered heatmap of the top differentially expressed genes between _HBR_ and _UHR_ samples.
# Author: Opemidimeji Osatoyinbo
# GitHub: https://github.com/opemidimejiosatoyinbo
# LinkedIn: https://linkedin.com/in/opemidimejiosatoyinbo
"""
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

# dataset URL (as you provided)
NORMALIZED_URL = ("https://raw.githubusercontent.com/HackBio-Internship/"
                  "2025_project_collection/refs/heads/main/Python/Dataset/"
                  "hbr_uhr_top_deg_normalized_counts.csv")

sb.set(style="white", context="notebook")

def plot_heatmap(normalized_url: str = NORMALIZED_URL,
                 top_n: int = 25,
                 cmap: str = "Blues",
                 out_file: str = "fig_1A_heatmap.png"):
    """
    Load normalized counts, pick top_n genes (first rows in file assumed top),
    z-score rows and produce a clustered heatmap.

    Parameters
    ----------
    normalized_url : str
        URL to normalized counts. Expected format: 'gene' column + sample columns.
    top_n : int
        Number of genes to display (for readability).
    cmap : str
        Matplotlib colormap (Blues recommended).
    out_file : str
        Output PNG filename.
    """
    df = pd.read_csv(normalized_url)
    if "gene" in df.columns:
        df = df.set_index("gene")
    # choose top_n genes by order (dataset already top DEGs)
    df_top = df.iloc[:top_n].copy()
    # ensure numeric
    df_top = df_top.apply(pd.to_numeric, errors="coerce").fillna(0.0)

    # z-score each row (gene)
    mat = df_top.values
    row_means = np.mean(mat, axis=1, keepdims=True)
    row_stds = np.std(mat, axis=1, ddof=1, keepdims=True)
    row_stds[row_stds == 0] = 1.0
    zmat = (mat - row_means) / row_stds
    zdf = pd.DataFrame(zmat, index=df_top.index, columns=df_top.columns)

    # clustered heatmap
    g = sb.clustermap(zdf, cmap=cmap, linewidths=0.5, figsize=(10, 10))
    g.ax_heatmap.set_xlabel("Samples")
    g.ax_heatmap.set_ylabel("Genes")
    plt.suptitle("Clustered Heatmap of Top DEGs (HBR vs UHR)", y=1.02)
    plt.savefig(out_file, dpi=300, bbox_inches="tight")
    plt.show()
    print("Saved heatmap to", out_file)


if __name__ == "__main__":
    plot_heatmap()