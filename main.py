"""
main.py
End-to-end Product Feedback Intelligence Pipeline.

Steps:
  1. Ingest data (CSV or synthetic fallback)
  2. Classify each item (bug / feature / usability / integration)
  3. Extract structured metadata (feature name, urgency, pain score…)
  4. Cluster into themes via embeddings + KMeans
  5. Score impact per theme (ARR × frequency × urgency)
  6. Generate quarterly roadmap + feature one-pagers via Claude
"""

import os
import sys
import pandas as pd

# Make sure imports work from project root
sys.path.insert(0, os.path.dirname(__file__))

from config.settings import (
    CSV_FILE_PATH, N_SYNTHETIC_RECORDS,
    CLASSIFIED_FEEDBACK_CSV, CLUSTERED_THEMES_CSV, OUTPUT_DIR
)
from src.utils.helpers import ensure_dir
from src.utils.logger import get_logger

logger = get_logger("main")


def run():
    ensure_dir(OUTPUT_DIR)
    logger.info("=" * 60)
    logger.info("  Product Feedback Intelligence Engine — Starting")
    logger.info("=" * 60)

    # ── Step 1: Ingest ──────────────────────────────────────────
    logger.info("\n[1/6] Ingesting feedback data…")
    df = _load_data()

    # ── Step 2: Classify ────────────────────────────────────────
    logger.info("\n[2/6] Classifying feedback…")
    from src.processing.classifier import classify_feedback
    df = classify_feedback(df)
    df.to_csv(CLASSIFIED_FEEDBACK_CSV, index=False)
    logger.info(f"      Saved → {CLASSIFIED_FEEDBACK_CSV}")

    # ── Step 3: Extract metadata ─────────────────────────────────
    logger.info("\n[3/6] Extracting feature metadata…")
    from src.processing.extractor import extract_features
    df = extract_features(df)

    # ── Step 4: Cluster ──────────────────────────────────────────
    logger.info("\n[4/6] Clustering into themes…")
    from src.clustering.theme_clusterer import cluster_feedback
    df = cluster_feedback(df)
    df.to_csv(CLUSTERED_THEMES_CSV, index=False)
    logger.info(f"      Saved → {CLUSTERED_THEMES_CSV}")

    # ── Step 5: Score ────────────────────────────────────────────
    logger.info("\n[5/6] Scoring theme impact…")
    from src.scoring.impact_scorer import score_themes
    scored_df = score_themes(df)

    # ── Step 6: Roadmap ──────────────────────────────────────────
    logger.info("\n[6/6] Generating roadmap…")
    from src.roadmap.roadmap_generator import generate_roadmap
    roadmap = generate_roadmap(scored_df, df)

    logger.info("\n" + "=" * 60)
    logger.info("  Pipeline complete! All outputs in the 'outputs/' folder.")
    logger.info("=" * 60)

    # Print a short preview
    print("\n\n── ROADMAP PREVIEW (first 40 lines) ──────────────────────")
    for line in roadmap.split("\n")[:40]:
        print(line)
    print("…  (full report in outputs/roadmap_report.md)")


def _load_data() -> pd.DataFrame:
    """Try CSV first; fall back to synthetic data."""
    try:
        from src.ingestion.csv_loader import load_csv
        df = load_csv(CSV_FILE_PATH)
        # Synthetic segment assignment (CSV doesn't have this column)
        if "segment" not in df.columns:
            import random
            random.seed(42)
            from config.settings import ARR_BY_SEGMENT
            df["segment"] = [random.choice(list(ARR_BY_SEGMENT.keys()))
                             for _ in range(len(df))]
        return df
    except FileNotFoundError as e:
        logger.warning(str(e))
        logger.warning(f"Falling back to {N_SYNTHETIC_RECORDS} synthetic records.")
        from src.ingestion.synthetic_data import generate_synthetic_feedback
        return generate_synthetic_feedback(N_SYNTHETIC_RECORDS)


if __name__ == "__main__":
    run()
