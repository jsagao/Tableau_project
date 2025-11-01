# DTSC600 Final Project — James Marvin Salarda Agao

This repository contains the essential files for the **DTSC600 Final Project** submission.  
It includes the Tableau workbook, documentation, dependency list, and `.gitignore` for clean version control.

---

## 📁 Repository Files

| File | Description |
|------|--------------|
| [.gitignore](./.gitignore) | Excludes temporary, cache, and environment files from Git tracking. |
| [DTSC600_FinalProject_JamesAgao.twb](./DTSC600_FinalProject_JamesAgao.twb) | Tableau workbook containing the final data visualizations and analysis. |
| [README.md](./README.md) | Main documentation for this project, setup instructions, and file descriptions. |
| [requirements.txt](./requirements.txt) | Python dependency list used for any preprocessing or reproducibility steps. |

---

## 🧭 How to Use

1. **Open the Tableau Workbook**  
   - Launch Tableau Desktop.  
   - Open `DTSC600_FinalProject_JamesAgao.twb`.  
   - If data sources are missing, go to **Data ▸ Replace Data Source…** and reconnect to your dataset.

2. **(Optional) Setup Python Environment**  
   If you wish to reproduce preprocessing steps:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
