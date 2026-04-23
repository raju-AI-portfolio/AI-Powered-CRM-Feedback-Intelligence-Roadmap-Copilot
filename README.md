# 🤖 AI-Powered CRM Feedback Intelligence & Roadmap Copilot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenAI_API-412991?style=for-the-badge&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/TextBlob-NLP-4CAF50?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Shipped-28A745?style=for-the-badge"/>
</p>

<p align="center">
  <strong>An end-to-end AI pipeline that transforms raw, unstructured customer feedback into structured product insights, sentiment analysis, issue detection, and LLM-generated business recommendations — all through an interactive Streamlit dashboard.</strong>
</p>

---

## 📌 Problem Statement

Product and operations teams face a constant challenge: customer feedback arrives in high volume, across multiple channels, and in completely unstructured form. Making sense of it requires:

- Manual reading and tagging of hundreds or thousands of reviews
- Subjective prioritisation with no consistent scoring methodology
- No repeatable process to convert raw voice-of-customer into roadmap decisions

> **This project automates that entire workflow** — from raw CSV upload through AI-generated, business-ready product recommendations — in a single, interactive web application.

---

## 🎯 Business Impact

| Manual Process | With This System |
|----------------|-----------------|
| Hours of manual review tagging | **Automated classification in seconds** |
| Subjective sentiment assessment | **Quantified sentiment scores via NLP** |
| Ad hoc issue identification | **Hybrid rule-based + AI issue detection** |
| No structured recommendations | **LLM-generated insights with business context** |
| Static reports in spreadsheets | **Interactive, filterable live dashboard** |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────┐
│         INPUT LAYER                 │
│   Customer Feedback CSV Upload      │
│   (App store · NPS · Support)       │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│     DATA CLEANING & PREPROCESSING   │
│  • Null / duplicate removal         │
│  • Type normalisation               │
│  • Text stripping & validation      │
│  • Token-length capping             │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│       FEATURE ENGINEERING           │
│  • Sentiment scoring (TextBlob)     │
│  • Polarity & subjectivity          │
│  • Issue flag detection             │
│  • Rule-based hybrid logic          │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│     AI INSIGHT GENERATION           │
│  • LLM prompt engineering           │
│  • Top issues extraction            │
│  • Business impact analysis         │
│  • Product improvement suggestions  │
└─────────────────┬───────────────────┘
                  │
                  ▼
┌─────────────────────────────────────┐
│     STREAMLIT DASHBOARD             │
│  • Data preview & stats             │
│  • Sentiment distribution charts    │
│  • AI insights rendered live        │
│  • Filterable, interactive UI       │
└─────────────────────────────────────┘
```

---

## ✨ Key Features

### 📥 Flexible CSV Ingestion
- Upload any customer feedback CSV directly through the browser
- Auto-detects the review/text column — works across different dataset formats
- Handles real-world Kaggle datasets (app store reviews, NPS exports, support tickets)

### 🧹 Robust Data Cleaning Pipeline
The system automatically handles common real-world data quality issues:

| Issue | Method |
|-------|--------|
| Missing / null reviews | `dropna()` — removes invalid rows |
| Duplicate submissions | `drop_duplicates()` — prevents repeated signals |
| Mixed data types | Type coercion to consistent string format |
| Whitespace & empty strings | `.str.strip()` + empty string filter |
| Token overflow in LLM | Input length capping — controls cost and latency |
| Inconsistent column names | Flexible column detection with fallback logic |

### 🧠 NLP-Based Feature Engineering
Using **TextBlob**, each feedback item is enriched with:
- **Polarity score** — measures positive/negative sentiment (−1.0 to +1.0)
- **Subjectivity score** — distinguishes factual reports from opinions (0.0 to 1.0)
- **Sentiment label** — `Positive / Neutral / Negative` classification
- **Issue flag** — hybrid rule-based detection of bug and usability signals

### 🤖 LLM-Powered Insight Generation (OpenAI API)
Structured prompt engineering extracts three distinct insight types from the cleaned, enriched data:
- **Top recurring issues** — what customers are most frequently complaining about
- **Business impact analysis** — the commercial risk and opportunity represented by the feedback
- **Product improvement suggestions** — prioritised, actionable recommendations for the product team

### 📊 Interactive Streamlit Dashboard
- Live data preview with row counts and column summary
- Sentiment distribution visualisation
- AI insights rendered with clean formatting
- No-code interface — accessible to PMs, analysts, and non-technical stakeholders

---

## 📁 Project Structure

```
AI-Powered-Customer-Review/
│
├── app.py                    # Streamlit app — main entry point
├── requirements.txt          # Python dependencies
├── .env.example              # API key template
├── .gitignore
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- An [OpenAI API key](https://platform.openai.com/api-keys)

### 1. Clone the repository

```bash
git clone https://github.com/raju-AI-portfolio/AI-Powered-Customer-Review.git
cd AI-Powered-Customer-Review
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Mac / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API key

```bash
# Option A — environment variable (recommended)
export OPENAI_API_KEY="sk-your-key-here"

# Option B — copy the example file and edit it
cp .env.example .env
# Then open .env and set OPENAI_API_KEY=sk-your-key-here
```

### 5. Launch the dashboard

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## 💡 How to Use

1. **Upload your CSV** — click "Browse files" and select any customer feedback dataset
2. **Preview the data** — the app detects the review column and shows a cleaned preview
3. **Review sentiment scores** — see polarity distribution across all feedback items
4. **Read AI insights** — scroll down for LLM-generated issues, impact analysis, and recommendations
5. **Iterate** — upload a different dataset or date range and re-run instantly

### Compatible dataset formats
The app works with any CSV containing a text/review column. Tested with:
- [App Store Reviews — Kaggle](https://www.kaggle.com/datasets/sanlian/app-store-reviews-for-a-mobile-app)
- NPS survey exports
- Zendesk / Intercom ticket exports
- Google Play Store review CSVs

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Language | Python 3.11+ | Core runtime |
| Data Processing | Pandas | Cleaning, transformation, aggregation |
| NLP | TextBlob | Sentiment scoring, polarity, subjectivity |
| LLM Integration | OpenAI API | Insight generation, prompt engineering |
| Frontend / UI | Streamlit | Interactive web dashboard |

---

## 📊 Example Output

**Sentiment Distribution**
```
Positive  ████████████████████  52%
Neutral   ██████████            27%
Negative  ████████              21%
```

**Sample AI-Generated Insights**

> **Top Issues Identified:**
> 1. App crashes frequently on export — reported by 34% of negative reviewers
> 2. Login failures and session timeouts — second most cited frustration
> 3. Missing bulk operations — requested by power users across segments
>
> **Business Impact:**
> The crash-on-export issue carries significant churn risk for high-frequency users.
> Login reliability problems are disproportionately represented in 1-star reviews,
> suggesting they are deal-breakers rather than minor friction points.
>
> **Product Recommendations:**
> 1. Prioritise export stability fix for next sprint — highest user-visible impact
> 2. Investigate session management — possible token expiry misconfiguration
> 3. Add bulk select + action as a Q3 feature based on request volume

---

## 🧠 Key Technical Decisions

**Why TextBlob for sentiment?**
TextBlob provides fast, dependency-free sentiment scoring without requiring a GPU or API call — keeping the feature engineering layer offline, low-latency, and cost-free. For production scale, this layer can be swapped for a fine-tuned transformer model.

**Why hybrid rule-based + AI?**
Rule-based issue detection (keyword matching, star rating thresholds) runs instantly on the full dataset and provides structured signals. The LLM layer then synthesises those signals into narrative insights — combining the reliability of deterministic logic with the expressiveness of generative AI.

**Why prompt structure matters**
The OpenAI prompts are engineered to request three specific, distinct output sections (issues · impact · recommendations) rather than a generic summary. This ensures the output is consistently structured and directly actionable for product decision-making.

---

## 🔮 Planned Enhancements

- [ ] **Advanced embeddings** — replace TextBlob with `sentence-transformers` for semantic clustering
- [ ] **Theme clustering** — group similar feedback into named themes using KMeans
- [ ] **ARR-weighted scoring** — link feedback to customer segment and revenue impact
- [ ] **Multi-source ingestion** — connect to Zendesk, Intercom, and Salesforce APIs directly
- [ ] **Real-time processing** — webhook-triggered pipeline for live feedback streams
- [ ] **Roadmap generation** — auto-produce quarterly roadmap proposals from scored themes
- [ ] **Cloud deployment** — one-click deploy to Streamlit Cloud or AWS

---

## 🧑‍💼 About the Author

**Raju Kumar** — Pharmaceutical AI Transformation Leader | Principal PM (AI Products)

14 years of pharma and biosimilar domain expertise combined with 3 years of independently building and shipping enterprise-grade Generative & Agentic AI systems.

- 🔗 [LinkedIn](https://www.linkedin.com/in/programdirectorai)
- 🐙 [GitHub Portfolio](https://github.com/raju-AI-portfolio)
- 📧 rajucanon@yahoo.com

**Other projects in this portfolio:**

| Project | Description |
|---------|-------------|
| [Regulatory Compliance Copilot](https://github.com/raju-AI-portfolio/Regulatory-Compliance-Intelligence-Copilot-with-Human-Review-) | Production RAG · GDPR/HIPAA/NIST · 95%+ accuracy · Human-in-the-loop |
| [Airline Customer Support Agent](https://github.com/raju-AI-portfolio/airline-customer-support-system) | Multi-agent system · LangGraph · Intent classification · Safety guardrails |
| [N8N RAG Workflow Automation](https://github.com/raju-AI-portfolio/Customer-Query-Response-Automation-using-N8N-RAG-Based-Workflow-) | No-code AI automation · Pinecone · Multi-channel delivery |
| [Feedback Intelligence & Roadmap Copilot](https://github.com/raju-AI-portfolio/AI-Powered-CRM-Feedback-Intelligence-Roadmap-Copilot) | Full pipeline · Clustering · Impact scoring · Roadmap generation |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<p align="center">
  <em>Turning the raw voice of the customer into the clearest signal on your product roadmap.</em>
</p>



