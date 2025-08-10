# HPC Algorithm Optimization: Pairwise Difference Performance Benchmark

## 📌 Project Overview

This project demonstrates the effectiveness of **algorithm optimization** in High Performance Computing (HPC) using a simple yet computationally intensive task: calculating the **sum of all pairwise absolute differences** in a dataset.

Two implementations are compared:

- **Naive (O(n²))** using nested Python loops
- **Optimized** using NumPy's **vectorized** operations

The goal is to showcase how replacing inefficient algorithms with optimized alternatives significantly improves performance, as discussed in the paper:
> *“An Empirical Study of High Performance Computing (HPC) Performance Bugs”*  
> — Md Abul Kalam Azad, Nafees Iqbal, Foyzul Hassan, Probir Roy

---

# 📊 Summary of Findings

## ✅ Performance Gains
- The optimized (vectorized) implementation is 30–45× faster than the naive version across all tested input sizes.
- For n = 2,000, the naive version can take ~8 seconds, while the optimized version runs in under 0.2 seconds.

## ✅ Alignment with Empirical Study
- This experiment confirms the empirical study’s findings that algorithm inefficiencies are a dominant cause of performance issues in HPC.
- A simple algorithm change (less than 20 lines of code) resulted in major performance gains—mirroring the study’s observation that performance bugs are often easily fixable.

## ⚠️ Trade-offs
- The vectorized version uses more memory, creating a full n x n matrix.
- While much faster, it may not scale efficiently beyond certain input sizes without further optimization (e.g., tiling, chunking, or sparse matrices).

---

## 🧪 How to Run

### 1. Install Requirements
```bash
pip install numpy matplotlib
python benchmark_plot.py