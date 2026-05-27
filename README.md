# 🎬🎮 MGR — Movie & Games Recommender Agent

> An AI agent that observes your preferences, thinks about the best matches, and recommends personalised movies and games.

---

## 📌 What problem does it solve?

Every day millions of people waste time scrolling through Netflix, Steam, or YouTube trying to decide what to watch or play. Current recommendation systems show you what is **popular**, not what is **right for you** at this moment.

**MGR solves this** by acting as a smart AI agent — you describe what you want in plain text, and it returns a curated list of 3–5 picks with clear reasons why each one matches you.

---

## 🧠 How it works — Observe → Think → Act

```
User Input (free text)
       │
       ▼
┌─────────────────────────────┐
│  OBSERVE: Input Parser      │  ← extracts genre, mood, platform
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│  THINK: Reasoning Engine    │  ← scores candidates using:
│                             │    Score(u,i) = sim(pref, item)
│  ┌──────────┐ ┌──────────┐  │             + w × review_signal
│  │Pref.     │ │ Item     │  │
│  │Encoder   │→│ Scorer   │→ Ranker
└─────────────────────────────┘
       │          ↑
       │    ┌─────┴──────┐
       │    │ Data Sources│
       │    │ TMDB  RAWG  │
       │    │ User History│
       │    └────────────┘
       ▼
┌─────────────────────────────┐
│  ACT: Output Formatter      │  ← top-k picks + score + reason
└─────────────────────────────┘
       │
       ▼
  Personalised Recommendations
```

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/mgr-agent.git
cd mgr-agent
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the agent
```bash
python main.py
```

### 4. Example interaction
```
You: I want a scary horror movie tonight on Netflix

🔍 [OBSERVE] Parsing user input...
   genre: horror | platform: netflix | mood: intense

🧠 [THINK] Running reasoning engine...
   Found 12 candidates after scoring.

⚡ [ACT] Formatting output...

══════════════════════════════
  Top 5 picks for you:
══════════════════════════════

  1. Hereditary  [MOVIE]
     Genre  : Horror
     Score  : 8.4 / 10
     Why    : Matches your horror preference — highly rated and genuinely scary.

  2. Get Out  [MOVIE]
     Genre  : Horror
     Score  : 8.1 / 10
     Why    : Matches your horror preference — highly rated and genuinely scary.
```

---

## 📁 Project Structure

```
mgr-agent/
│
├── main.py                  # Interactive CLI — run this
├── requirements.txt         # Python dependencies
├── .env.example             # API keys template
│
└── src/
    ├── agent.py             # Main agent loop (Observe→Think→Act)
    ├── input_parser.py      # OBSERVE — parse free-text input
    ├── reasoning_engine.py  # THINK   — score and rank candidates
    ├── data_fetcher.py      # Data    — sample data + TMDB/RAWG API
    └── output_formatter.py  # ACT     — format final output
```

---

## 🔑 Using Real APIs (Optional)

By default the agent uses built-in sample data — **no API key needed**.

To enable live data:

1. Get a free TMDB key at [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)
2. Get a free RAWG key at [rawg.io/apidocs](https://rawg.io/apidocs)
3. Copy `.env.example` to `.env` and fill in your keys
4. In `src/data_fetcher.py` set `USE_REAL_API = True`

---

## 🛠 Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| AI Backbone | Claude API (Anthropic) |
| Movie Data | TMDB API |
| Game Data | RAWG API |
| Interface | Command-line (CLI) |

---

## 📊 System Diagram

![MGR System Diagram](docs/system_diagram.png)

---

## 👤 Author

Built as part of an AI Agent course project.
Tool used: **Claude** by Anthropic.

---

## 📄 License

MIT License — free to use and modify.
