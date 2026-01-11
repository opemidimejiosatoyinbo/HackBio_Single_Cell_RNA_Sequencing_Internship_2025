# 🦠 SARS-CoV-2 Infection Dynamics in Bronchial Epithelium

## 📖 Overview
This analysis reproduces key findings from the study on SARS-CoV-2 infection in human bronchial epithelial cells (HBECs). We track the infection dynamics across 1, 2, and 3 days post-infection (dpi) compared to a mock control.



### 🎯 Objectives
1.  **Data Integration:** Merge data from Mock, 1dpi, 2dpi, and 3dpi timepoints.
2.  **QC & Preprocessing:** Filter low-quality cells and normalize expression.
3.  **Cell Type Identification:** Distinguish between Basal, Ciliated, and Secretory cells.
4.  **Trajectory Analysis:** Model the differentiation path of cells at 3dpi.

---

## 🛠️ Computational Workflow

### 1. Data Loading & Merging
We load sparse matrices for all timepoints. Instead of processing them individually, we concatenate them into a single `AnnData` object. This ensures that normalization and PCA are consistent across the entire experiment.

### 2. Quality Control
We use three key metrics to identify stressed or empty droplets:
* **Mitochondrial Content:** High MT% (>15%) suggests cell membrane rupture (death).
* **Library Size:** Very low counts suggest empty droplets.
* **Viral Load:** We track viral gene expression to distinguish infected cells from bystanders.



### 3. Dimensionality Reduction & Clustering
We use **PCA** to densify the data and **UMAP** to visualize it in 2D space. **Leiden clustering** groups cells with similar transcriptomic profiles.



### 4. Annotation (Manual vs. Automated)
We validate cell types using canonical markers from the reference paper:
* **Basal Cells:** *TP63, KRT5*
* **Ciliated Cells:** *FOXJ1*
* **Club/Secretory:** *SCGB1A1*



### 5. Pseudotime Analysis (3dpi)
To understand how tissue regenerates or responds to infection, we perform **Diffusion Pseudotime (DPT)** analysis on the 3dpi sample. This orders cells along a continuous "time" axis, typically starting from stem-like Basal cells.



---

## 📂 Directory Structure

```text
HackBio_Internship_SC_RNA-Seq_2025/
└── Stage_Three/
    ├── notebooks/
    │   └── sars_cov2_infection_dynamics.ipynb    # Main analysis notebook
    ├── data/
    │   └── raw/
    │       ├── mock/                   # (matrix.mtx.gz, barcodes, features inside)
    │       ├── 1dpi/
    │       ├── 2dpi/
    │       └── 3dpi/
    ├── figures/
    │   └── Project1/                   # All plots saved here
    └── sars_cov2_infection_dynamics.md