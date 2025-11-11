"""
HackBio Internship - Stage 1 Surprise Task
Team: Glycine

# Task: Plot 'texture_mean' vs 'radius_mean'
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

def plot_radius_vs_texture(data_url: str = DATA_URL,
                           out_file: str = "fig_1C_radius_texture.png"):
    """
    Plot texture_mean vs radius_mean colored by diagnosis (M/B).
    """
    df = pd.read_csv(data_url)
    required = {'radius_mean', 'texture_mean', 'diagnosis'}
    if not required.issubset(df.columns):
        raise ValueError("Missing required columns for scatter plot: " + str(required - set(df.columns)))

    plt.figure(figsize=(8, 6))
    sb.scatterplot(data=df, x="radius_mean", y="texture_mean", hue="diagnosis", s=70, alpha=0.8)
    plt.xlabel("radius_mean")
    plt.ylabel("texture_mean")
    plt.title("radius_mean vs texture_mean by diagnosis")
    plt.legend(title="diagnosis")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(out_file, dpi=300)
    plt.show()
    print("Saved scatter plot to", out_file)


if __name__ == "__main__":
    plot_radius_vs_texture()