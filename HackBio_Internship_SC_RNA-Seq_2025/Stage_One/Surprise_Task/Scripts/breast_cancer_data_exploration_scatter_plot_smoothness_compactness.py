"""
HackBio Internship - Stage 1 Surprise Task
Team: Glycine

# Task: Plot 'compactness_mean' vs 'smoothness_mean'
# Author: Opemidimeji Osatoyinbo
# GitHub: https://github.com/opemidimejiosatoyinbo
# LinkedIn: https://linkedin.com/in/opemidimejiosatoyinbo
"""
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

DATA_URL = ("https://raw.githubusercontent.com/HackBio-Internship/"
            "2025_project_collection/refs/heads/main/Python/Dataset/data-3.csv")

sb.set(style="whitegrid", context="notebook")

def plot_smoothness_vs_compactness(data_url: str = DATA_URL,
                                   out_file: str = "fig_1E_smooth_compact.png"):
    df = pd.read_csv(data_url)
    required = {'smoothness_mean', 'compactness_mean', 'diagnosis'}
    if not required.issubset(df.columns):
        raise ValueError("Missing required columns: " + str(required - set(df.columns)))

    plt.figure(figsize=(8, 6))
    sb.scatterplot(data=df, x="smoothness_mean", y="compactness_mean", hue="diagnosis", s=70, alpha=0.85)
    plt.xlabel("smoothness_mean")
    plt.ylabel("compactness_mean")
    plt.title("compactness_mean vs smoothness_mean by diagnosis")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(title="diagnosis")
    plt.tight_layout()
    plt.savefig(out_file, dpi=300)
    plt.show()
    print("Saved scatter to", out_file)


if __name__ == "__main__":
    plot_smoothness_vs_compactness()