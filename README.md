## 🛎️ 1. OLX Car Cover Scraper

This Python script scrapes car cover listings from OLX and saves them into a CSV file with a timestamped filename.

### 🔧 Requirements

- Python 3.x
- Install required packages:

```bash
pip3 install -r requirements.txt
```

### ▶️ Run the script

```bash
python3 script.py
```

### 📁 Output

A file named like `olx_data_2025-05-10_1530.csv` will be created with search result details.

---

## 📉 2. AMFI NAV Extractor (Shell Script)

This script fetches mutual fund NAV data from [AMFI India](https://www.amfiindia.com/spages/NAVAll.txt) and extracts scheme names with their asset values into a tab-separated file.

### 🛠 Requirements

- `wget`
- `awk`
- Linux/macOS shell

### 🔧 Installation

### ▶️ Run the shell script

```bash
chmod +x extract.sh
./extract.sh
```

### 📁 Output

A file named `scheme_nav_data.tsv` will be created with the extracted NAV data.

---

-Jay
