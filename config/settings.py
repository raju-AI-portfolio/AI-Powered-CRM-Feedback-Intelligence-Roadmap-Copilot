"""
config/settings.py
Central configuration for the Product Feedback Intelligence Engine.
"""

import os

# ─────────────────────────────────────────
# API Keys
# ─────────────────────────────────────────
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "sk-ant-your-key-here")

# ─────────────────────────────────────────
# Model
# ─────────────────────────────────────────
CLAUDE_MODEL = "claude-sonnet-4-20250514"
MAX_TOKENS = 1500

# ─────────────────────────────────────────
# Data Sources
# ─────────────────────────────────────────
# Path to downloaded Kaggle CSV
CSV_FILE_PATH = "data/app_store_reviews.csv"

# If CSV not found, we use N_SYNTHETIC_RECORDS synthetic rows instead
N_SYNTHETIC_RECORDS = 200

# ─────────────────────────────────────────
# Processing
# ─────────────────────────────────────────
BATCH_SIZE = 10          # Records per Claude API call (batching saves tokens)

# ─────────────────────────────────────────
# Clustering
# ─────────────────────────────────────────
N_CLUSTERS = 8           # Number of theme clusters
EMBEDDING_MODEL = "all-MiniLM-L6-v2"   # Sentence-transformers model (offline)

# ─────────────────────────────────────────
# Impact Scoring Weights  (must sum to 1.0)
# ─────────────────────────────────────────
ARR_WEIGHT        = 0.40
FREQUENCY_WEIGHT  = 0.35
URGENCY_WEIGHT    = 0.25

# Synthetic ARR tiers per customer segment (USD)
ARR_BY_SEGMENT = {
    "Enterprise": 120_000,
    "Mid-Market": 40_000,
    "SMB": 8_000,
    "Free":       0,
}

# ─────────────────────────────────────────
# Roadmap
# ─────────────────────────────────────────
TOP_N_FEATURES = 5       # Features to include in roadmap
QUARTERS = ["Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026"]

# ─────────────────────────────────────────
# Output paths
# ─────────────────────────────────────────
OUTPUT_DIR              = "outputs"
CLASSIFIED_FEEDBACK_CSV = f"{OUTPUT_DIR}/classified_feedback.csv"
CLUSTERED_THEMES_CSV    = f"{OUTPUT_DIR}/clustered_themes.csv"
IMPACT_SCORES_CSV       = f"{OUTPUT_DIR}/impact_scores.csv"
ROADMAP_REPORT_MD       = f"{OUTPUT_DIR}/roadmap_report.md"
ONEPAGERS_DIR           = f"{OUTPUT_DIR}/feature_onepagers"
