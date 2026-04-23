# 🧠 AI-Powered CRM Feedback Intelligence & Roadmap Copilot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Claude_API-Anthropic-6B48FF?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/sentence--transformers-HuggingFace-FFD21E?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Production_Ready-28A745?style=for-the-badge"/>
</p>

<p align="center">
  <strong>An end-to-end Generative AI pipeline that transforms raw customer feedback from 15+ sources into data-driven, quarterly roadmap proposals — replacing days of manual analysis with minutes.</strong>
</p>

---

## 📌 Problem Statement

Product teams are drowning in feedback scattered across support tickets, NPS surveys, app store reviews, sales calls, and community forums. Prioritisation decisions are largely subjective, ARR-weighted customer voices get lost, and the gap between customer pain and roadmap reality grows wider every sprint.

> **This project solves that.** It aggregates all feedback, uses Claude AI to extract themes and feature requests, calculates data-driven impact scores, and auto-generates quarterly roadmap recommendations — complete with customer-quote justifications and stakeholder-ready one-pagers.

---

## 🎯 Business Impact

| Metric | Before | After |
|--------|--------|-------|
| Feedback coverage | ~40% (manual sampling) | **100%** (automated ingestion) |
| Time to roadmap decision | 3–5 days | **< 30 minutes** |
| Prioritisation basis | Opinion-driven | **ARR × Frequency × Urgency score** |
| Customer-driven features | ~20% of roadmap | **Target: 45%+** |
| Stakeholder one-pagers | 2–3 hrs per feature | **Auto-generated** |

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         DATA SOURCES                                │
│  App Store Reviews │ NPS Surveys │ Sales Notes │ Support Tickets    │
│         Community Forums │ In-App Feedback │ CRM Data              │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
                    ┌───────▼────────┐
                    │  ① INGEST      │  csv_loader.py / synthetic_data.py
                    │  pandas DF     │  Kaggle CSV or synthetic fallback
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  ② CLASSIFY    │  Claude API (batch=10)
                    │  4 categories  │  bug · feature · usability · integration
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  ③ EXTRACT     │  Claude API (structured JSON)
                    │  metadata      │  feature · urgency · pain · sentiment
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  ④ CLUSTER     │  sentence-transformers + KMeans
                    │  themes        │  Embeddings → N clusters → Claude naming
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  ⑤ SCORE       │  Weighted formula
                    │  impact 0–100  │  ARR(40%) × Freq(35%) × Urgency(25%)
                    └───────┬────────┘
                            │
                    ┌───────▼────────┐
                    │  ⑥ GENERATE    │  Claude API (roadmap + one-pagers)
                    │  roadmap       │  Quarterly plan · Feature justifications
                    └───────┬────────┘
                            │
          ┌─────────────────┼──────────────────┐
          ▼                 ▼                  ▼
  roadmap_report.md   impact_scores.csv  feature_onepagers/
  (Quarterly plan)    (Ranked themes)    (Stakeholder docs)
```

---

## ✨ Key Features

### 🔍 Multi-Source Feedback Ingestion
- Loads real app store reviews from [Kaggle dataset](https://www.kaggle.com/datasets/sanlian/app-store-reviews-for-a-mobile-app) (date, platform, country, star rating, issue flag)
- Auto-generates realistic synthetic feedback (200+ records) when CSV is unavailable — simulating Zendesk tickets, NPS responses, sales notes, and community posts
- Normalised schema across all sources for unified downstream processing

### 🏷️ AI-Powered Classification (Claude API)
- Classifies every feedback item into one of four product categories: `bug_report`, `feature_request`, `usability_issue`, `integration_request`
- Batch processing (10 items/call) to minimise API costs
- Confidence scoring on every classification with graceful fallback handling

### 🧬 Structured Metadata Extraction (Claude API)
For each item, Claude extracts:
- **Feature name** — short, actionable label (≤6 words)
- **Reason** — why the user needs it (1 sentence)
- **Urgency** — `low / medium / high`
- **User segment** — `Enterprise / Mid-Market / SMB / Free / Unknown`
- **Pain score** — 1–10 integer
- **Sentiment** — `positive / neutral / negative`

### 🔵 Semantic Theme Clustering
- Generates sentence embeddings using `all-MiniLM-L6-v2` (runs fully offline)
- L2-normalised vectors → KMeans clustering (configurable N clusters)
- Claude auto-names each cluster with a 5-word theme name and one-sentence description
- Tracks theme volume and composition for trend analysis

### 📊 Data-Driven Impact Scoring
Composite score (0–100) per theme using normalised, weighted formula:

```
Impact Score = (ARR_weight × ARR_norm) + (Freq_weight × Freq_norm) + (Urgency_weight × Urgency_norm)

Default weights:   ARR = 40%  |  Frequency = 35%  |  Urgency = 25%
```

ARR tiers (configurable): Enterprise $120K · Mid-Market $40K · SMB $8K · Free $0

### 📋 Quarterly Roadmap Generation (Claude API)
- Assigns top-N features to quarters based on complexity and impact
- Each feature includes: "Why We're Building This" narrative, expected business outcomes, and 2–3 success metrics
- Auto-generates **per-feature stakeholder one-pagers** in Markdown
- Full executive summary with coverage stats and top theme highlights

---

## 📁 Project Structure

```
product_feedback_intelligence/
│
├── main.py                          # Entry point — runs full 6-step pipeline
│
├── config/
│   └── settings.py                  # All config: weights, model, paths, thresholds
│
├── src/
│   ├── ingestion/
│   │   ├── csv_loader.py            # Kaggle CSV loader with flexible column mapping
│   │   └── synthetic_data.py        # Realistic synthetic feedback generator
│   │
│   ├── processing/
│   │   ├── classifier.py            # Claude: 4-category classification + confidence
│   │   └── extractor.py             # Claude: structured metadata extraction
│   │
│   ├── clustering/
│   │   └── theme_clusterer.py       # Embeddings + KMeans + Claude theme naming
│   │
│   ├── scoring/
│   │   └── impact_scorer.py         # ARR × Frequency × Urgency weighted scoring
│   │
│   ├── roadmap/
│   │   └── roadmap_generator.py     # Claude: quarterly roadmap + feature one-pagers
│   │
│   └── utils/
│       ├── logger.py                # Structured console logging
│       └── helpers.py               # JSON parsing, chunking utilities
│
├── data/
│   └── README.txt                   # Dataset download instructions
│
├── outputs/                         # All generated files land here
│   ├── classified_feedback.csv
│   ├── clustered_themes.csv
│   ├── impact_scores.csv
│   ├── roadmap_report.md
│   └── feature_onepagers/
│
├── notebooks/
│   └── exploration.ipynb            # Interactive EDA + visualisations
│
├── tests/
│   └── test_pipeline.py             # Unit tests (no API key required)
│
├── requirements.txt
├── pytest.ini
├── .env.example
└── .gitignore
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- An [Anthropic API key](https://console.anthropic.com/)

### 1. Clone the repository

```bash
git clone https://github.com/raju-AI-portfolio/AI-Powered-CRM-Feedback-Intelligence-Roadmap-Copilot.git
cd AI-Powered-CRM-Feedback-Intelligence-Roadmap-Copilot
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** `sentence-transformers` will download the `all-MiniLM-L6-v2` model (~80MB) on first run. This only happens once and is cached locally.

### 4. Configure your API key

```bash
cp .env.example .env
```

Edit `.env` and add your key:
```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Or export directly:
```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

### 5. (Optional) Add the Kaggle dataset

Download the app store reviews CSV from:
**[https://www.kaggle.com/datasets/sanlian/app-store-reviews-for-a-mobile-app](https://www.kaggle.com/datasets/sanlian/app-store-reviews-for-a-mobile-app)**

Place the file at: `data/app_store_reviews.csv`

> If the CSV is not found, the pipeline automatically generates 200 synthetic feedback records and continues without interruption.

### 6. Run the full pipeline

```bash
python main.py
```

**Expected output:**
```
============================================================
  Product Feedback Intelligence Engine — Starting
============================================================

[1/6] Ingesting feedback data…
[2/6] Classifying feedback…
        Batch 1/20 … Batch 20/20
[3/6] Extracting feature metadata…
[4/6] Clustering into themes…
        Cluster 0: 'CSV Export & Reporting'  (28 items)
        Cluster 1: 'Mobile Performance Issues'  (24 items)
        ...
[5/6] Scoring theme impact…
        # 1  CSV Export & Reporting         score=87.4
        # 2  SSO / Enterprise Auth          score=79.1
        ...
[6/6] Generating roadmap…

============================================================
  Pipeline complete! All outputs in the 'outputs/' folder.
============================================================
```

---

## ⚙️ Configuration Reference

All settings live in `config/settings.py`. Key parameters:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `CLAUDE_MODEL` | `claude-sonnet-4-20250514` | Claude model to use |
| `BATCH_SIZE` | `10` | Feedback items per API call |
| `N_CLUSTERS` | `8` | Number of theme clusters |
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | Sentence-transformers model |
| `ARR_WEIGHT` | `0.40` | Weight for ARR in impact score |
| `FREQUENCY_WEIGHT` | `0.35` | Weight for mention frequency |
| `URGENCY_WEIGHT` | `0.25` | Weight for urgency/pain |
| `TOP_N_FEATURES` | `5` | Features included in roadmap |
| `N_SYNTHETIC_RECORDS` | `200` | Fallback synthetic record count |

**Tuning the impact score weights:** The three weights must sum to `1.0`. Adjust based on your business context — e.g., increase `ARR_WEIGHT` if Enterprise retention is the top priority, or `URGENCY_WEIGHT` if NPS improvement is the goal.

---

## 📤 Outputs

After running the pipeline, the `outputs/` directory contains:

| File | Description |
|------|-------------|
| `classified_feedback.csv` | Every feedback item with `label` and `confidence` columns |
| `clustered_themes.csv` | Full dataset with `cluster`, `theme_name`, `theme_description` |
| `impact_scores.csv` | One row per theme: rank, score, ARR, mentions, sample quotes |
| `roadmap_report.md` | Full quarterly roadmap with executive summary and impact table |
| `feature_onepagers/*.md` | One stakeholder-ready one-pager per top-N feature |

### Sample `impact_scores.csv`

```
rank | theme_name                  | impact_score | mention_count | total_arr
-----|-----------------------------|--------------|----|----------
1    | CSV Export & Reporting      | 87.4         | 28 | $840,000
2    | SSO / Enterprise Auth       | 79.1         | 22 | $1,200,000
3    | Mobile Offline Mode         | 71.3         | 19 | $320,000
...
```

### Sample `roadmap_report.md` (excerpt)

```markdown
# Product Feedback Intelligence — Roadmap Report
Generated: 2025-07-15 09:32

## Executive Summary
- Total feedback items analysed: 200
- Distinct themes identified: 8
- Top impact feature: CSV Export & Reporting (score: 87.4)

## Q3 2025 — Foundation Sprint
### CSV Export & Reporting (Impact: 87.4)
**Why We're Building This:** 28 customers representing $840K ARR
have flagged the absence of bulk CSV export as a weekly operational
blocker. Enterprise users are manually copying data — a 2–3 hour
weekly overhead per team...
```

---

## 🧪 Running Tests

Unit tests cover core utilities and the impact scorer without requiring an API key:

```bash
pytest tests/ -v
```

```
tests/test_pipeline.py::TestHelpers::test_safe_json_parse_clean         PASSED
tests/test_pipeline.py::TestHelpers::test_safe_json_parse_with_fences   PASSED
tests/test_pipeline.py::TestHelpers::test_chunk_list                     PASSED
tests/test_pipeline.py::TestSyntheticData::test_generates_correct_count  PASSED
tests/test_pipeline.py::TestSyntheticData::test_no_empty_text            PASSED
tests/test_pipeline.py::TestImpactScorer::test_impact_score_range        PASSED
tests/test_pipeline.py::TestImpactScorer::test_ranked_descending         PASSED
...
```

---

## 📓 Exploratory Notebook

Launch the Jupyter notebook for interactive analysis and visualisations:

```bash
cd notebooks
jupyter notebook exploration.ipynb
```

The notebook includes:
- Label distribution bar charts
- Impact score scatter plot (mentions vs ARR, bubble size = score)
- Full roadmap Markdown rendering in-notebook
- Step-by-step pipeline execution with cell-level outputs

---

## 🔌 Extending the Pipeline

### Add a new feedback source

1. Create a new loader in `src/ingestion/` that returns a DataFrame with columns: `feedback_id`, `source`, `text`, `star_rating`, `platform`, `country`, `segment`
2. Call it in `main.py`'s `_load_data()` function alongside existing sources
3. Use `pd.concat()` to merge with the existing DataFrame

### Integrate with a real CRM

```python
# Example: pull from Salesforce via simple-salesforce
from simple_salesforce import Salesforce
sf = Salesforce(username=..., password=..., security_token=...)
cases = sf.query("SELECT Id, Description, Account.AnnualRevenue FROM Case")
df = pd.DataFrame(cases['records'])
```

### Swap the embedding model

Update `EMBEDDING_MODEL` in `config/settings.py` to any [sentence-transformers model](https://www.sbert.net/docs/pretrained_models.html):
```python
EMBEDDING_MODEL = "all-mpnet-base-v2"   # Higher accuracy, slower
EMBEDDING_MODEL = "all-MiniLM-L6-v2"    # Default — fast and accurate
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| LLM / AI | [Anthropic Claude API](https://docs.anthropic.com) (`claude-sonnet-4`) |
| Embeddings | [sentence-transformers](https://www.sbert.net/) `all-MiniLM-L6-v2` |
| Clustering | [scikit-learn](https://scikit-learn.org/) KMeans |
| Data Processing | [pandas](https://pandas.pydata.org/) · [NumPy](https://numpy.org/) |
| Testing | [pytest](https://pytest.org/) |
| Notebook | [Jupyter](https://jupyter.org/) |
| Dataset | [Kaggle — App Store Reviews](https://www.kaggle.com/datasets/sanlian/app-store-reviews-for-a-mobile-app) |

---

## 🗺️ Roadmap — Planned Enhancements

- [ ] **Streamlit Dashboard** — real-time impact score visualisation and roadmap explorer
- [ ] **Live CRM Connectors** — Zendesk, Intercom, Salesforce, Gong API integrations via N8N
- [ ] **Trend Tracking** — theme volume over time with week-on-week delta alerts
- [ ] **Auto-Notification** — Slack/email alert to customers when their requested feature ships
- [ ] **Adoption Feedback Loop** — track feature adoption vs original request volume post-launch
- [ ] **Multi-Language Support** — extend classification and extraction to non-English feedback
- [ ] **Pinecone Integration** — replace in-memory clustering with persistent vector store for large-scale datasets

---

## 🧑‍💼 About the Author

**Raju Kumar** — Pharmaceutical AI Transformation Leader | Principal PM (AI Products)

14 years of pharma and biosimilar domain expertise combined with 3 years of independently building and shipping enterprise-grade Generative & Agentic AI systems.

- 🔗 [LinkedIn](https://www.linkedin.com/in/programdirectorai)
- 🐙 [GitHub Portfolio](https://github.com/raju-AI-portfolio)
- 📧 rajucanon@yahoo.com

**Other projects in this portfolio:**
- [Regulatory Compliance Intelligence Copilot](https://github.com/raju-AI-portfolio/Regulatory-Compliance-Intelligence-Copilot-with-Human-Review-) — Production RAG system · GDPR/HIPAA/NIST · 95%+ accuracy
- [Airline Customer Support Multi-Agent System](https://github.com/raju-AI-portfolio/airline-customer-support-system) — LangGraph · Multi-agent orchestration
- [Customer Query Automation — N8N RAG Workflow](https://github.com/raju-AI-portfolio/Customer-Query-Response-Automation-using-N8N-RAG-Based-Workflow-) — N8N · No-code AI automation

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">
  <em>Built with ❤️ to give the customer's voice its rightful place in every product roadmap.</em>
</p>
