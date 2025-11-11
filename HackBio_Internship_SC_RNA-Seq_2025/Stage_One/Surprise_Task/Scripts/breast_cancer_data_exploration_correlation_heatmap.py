"""
HackBio Internship - Stage 1 Surprise Task
Team: Glycine

# Task: Compute the correlation matrix of six key features: 'radius_mean', 'texture_mean'. 'perimeter_mean', 'area_mean', 'smoothness_mean', 'compactness_mean'.
# Author: Opemidimeji Osatoyinbo
# GitHub: https://github.com/opemidimejiosatoyinbo
# LinkedIn: https://linkedin.com/in/opemidimejiosatoyinbo
"""
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

DATA_URL = ("https://raw.githubusercontent.com/HackBio-Internship/"
            "2025_project_collection/refs/heads/main/Python/Dataset/data-3.csv")

sb.set(style="white", context="notebook")

def plot_correlation_heatmap(data_url: str = DATA_URL,
                             features=None,
                             out_file: str = "fig_1D_corrheatmap.png"):
    """
    Compute correlation matrix and plot as annotated heatmap.
    """
    if features is None:
        features = ['radius_mean', 'texture_mean', 'perimeter_mean',
                    'area_mean', 'smoothness_mean', 'compactness_mean']

    df = pd.read_csv(data_url)
    missing = set(features) - set(df.columns)
    if missing:
        raise ValueError("Missing expected features: " + str(missing))

    corr_mat = df[features].corr()
    plt.figure(figsize=(7, 6))
    sb.heatmap(corr_mat, annot=True, fmt=".2f", cmap="Blues", linewidths=0.5, square=True,
               cbar_kws={"shrink": 0.7})
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(out_file, dpi=300)
    plt.show()
    print("Saved correlation heatmap to", out_file)


if __name__ == "__main__":
    plot_correlation_heatmap()