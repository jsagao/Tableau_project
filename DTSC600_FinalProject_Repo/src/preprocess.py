#!/usr/bin/env python
"""Minimal preprocessing script.

- Reads all CSVs from data/raw/
- Applies simple cleaning (trim cols, drop dupes, parse dates example)
- Writes a single merged file to data/processed/clean_dataset.csv

Customize the SCHEMA and TRANSFORMS for your project.
"""
from __future__ import annotations
import os
import glob
import pandas as pd

RAW_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "processed")
os.makedirs(OUT_DIR, exist_ok=True)

def load_raw_csvs() -> list[pd.DataFrame]:
    paths = sorted(glob.glob(os.path.join(RAW_DIR, "*.csv")))
    if not paths:
        print("No CSVs found in data/raw/. Place your raw CSVs there and re-run.")
        return []
    frames = []
    for p in paths:
        try:
            df = pd.read_csv(p)
            frames.append(df)
            print(f"Loaded {p} -> {df.shape[0]} rows, {df.shape[1]} cols")
        except Exception as e:
            print(f"ERROR reading {p}: {e}")
    return frames

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    # Strip whitespace in column names
    df.columns = [c.strip() for c in df.columns]

    # Example: attempt to parse common date-like columns
    for col in df.columns:
        if any(k in col.lower() for k in ["date", "time", "timestamp"]):
            try:
                df[col] = pd.to_datetime(df[col], errors="ignore")
            except Exception:
                pass

    # Drop exact duplicate rows
    df = df.drop_duplicates()

    return df

def main():
    frames = load_raw_csvs()
    if not frames:
        return
    # Simple union (aligns columns by name). Consider custom joins for your data.
    df = pd.concat(frames, ignore_index=True, sort=False)
    df = basic_clean(df)
    out_path = os.path.join(OUT_DIR, "clean_dataset.csv")
    df.to_csv(out_path, index=False)
    print(f"Wrote {out_path} -> {df.shape[0]} rows, {df.shape[1]} cols")

if __name__ == "__main__":
    main()
