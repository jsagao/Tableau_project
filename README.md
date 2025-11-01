# DTSC 600 Final Project — Reproducible Repo

**Author:** James Marvin Salarda Agao  
**Course:** DTSC 600 — Final Project  
**Last Updated:** 2025-11-01

This repository contains a clean, reproducible structure to support your Tableau workbook and any optional Python-based data preparation.

## Repository Layout

```
DTSC600_FinalProject_Repo/
├─ DTSC600_FinalProject_JamesAgao.twb        # Tableau workbook
├─ README.md                                  # You are here
├─ requirements.txt                           # Python deps for optional data prep
├─ .gitignore
├─ src/
│  └─ preprocess.py                           # Example data cleaning pipeline
├─ notebooks/
│  └─ analysis.ipynb                          # Optional EDA / prep notebook
└─ data/
   ├─ raw/                                    # Place original CSVs here
   └─ processed/                              # Pipeline outputs
```

## Quick Start

### Option A — Tableau only
1. Open the workbook: `DTSC600_FinalProject_JamesAgao.twb` in Tableau Desktop.
2. If Tableau cannot find the data, go to **Data ▸ Replace Data Source…**, and point to the CSV(s) in `data/processed/` or `data/raw/`.
3. Refresh extracts if applicable (**Data ▸ Extract ▸ Refresh**).

### Option B — Full Reproducible Flow (Python + Tableau)
1. Create a virtual environment (recommended) and install deps:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Put your original datasets in `data/raw/` (CSV files).
3. Run the preprocessing pipeline:
   ```bash
   python src/preprocess.py
   ```
   This will output cleaned files to `data/processed/`.   **Tip:** Adjust column names and transformations in `src/preprocess.py` to match your dataset.
4. Open the Tableau workbook and **Replace Data Source** to the processed CSV in `data/processed/`.

## Notes

- Keep personally-identifiable information (PII) out of the repository, or anonymize in `src/preprocess.py` before saving to `data/processed/`.
- Large raw datasets should be excluded via `.gitignore` and provided via a project drive or a data request link.
- If your .twb references absolute file paths, use **Data ▸ Replace Data Source…** to re-point to this repo's `data/processed/` folder.

## Repro Tips

- Commit frequently with clear messages.
- Use branches for major feature changes (e.g., `feature/new-datasource`).
- Tag final submission versions (e.g., `v1.0`).
