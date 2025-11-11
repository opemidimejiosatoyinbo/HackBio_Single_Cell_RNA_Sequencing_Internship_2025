"""
HackBio Internship - Stage 1 Surprise Task
Team: Glycine

# Task: Plot kernel density estimates (KDE) 'area_mean'
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

def plot_area_kde(data_url: str = DATA_URL, out_file: str = "fig_1F_area_kde.png"):
    df = pd.read_csv(data_url)
    required = {'area_mean', 'diagnosis'}
    if not required.issubset(df.columns):
        raise ValueError("Missing required columns: " + str(required - set(df.columns)))

    plt.figure(figsize=(9, 6))
    # KDE for Malignant
    sb.kdeplot(data=df[df['diagnosis'] == 'M'], x='area_mean', fill=True, alpha=0.45, label='Malignant (M)', color='red')
    # KDE for Benign
    sb.kdeplot(data=df[df['diagnosis'] == 'B'], x='area_mean', fill=True, alpha=0.45, label='Benign (B)', color='skyblue')
    plt.xlabel("area_mean")
    plt.ylabel("Density")
    plt.title("KDE of area_mean by diagnosis")
    plt.legend(title="diagnosis")
    plt.tight_layout()
    plt.savefig(out_file, dpi=300)
    plt.show()
    print("Saved KDE to", out_file)


if __name__ == "__main__":
    plot_area_kde()