# CodeAlpha-Stock-portfolio-tracker
# 📈 Stock Portfolio Tracker

A simple Python program to track stock investments using hardcoded prices.  
This project is designed as a beginner‑friendly exercise in **dictionaries, input/output, arithmetic, and file handling**.

---

## 🚀 Features
- User inputs stock symbols and quantities.
- Hardcoded dictionary defines stock prices (e.g., `{"AAPL": 180, "META": 250}`).
- Calculates **total investment value**.
- Displays portfolio summary in the terminal.
- Saves results to a `.csv` file for easy viewing in Excel or Google Sheets.
- Optional timestamped filenames to keep history of runs.

---

## 🛠️ Requirements
- Python 3.x  
- No external libraries required (uses only built‑in modules).

---

## 📄 Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/teja-sri21/CodeAlpha-Stock-portfolio-tracker.git
   cd stock-portfolio-tracker

2. Run the program:
   `bash
   python portfolio_tracker.py
   `

3. Enter stock symbols and quantities when prompted.  
   Example:
   `
   Enter stock symbol (or 'done' to finish): AAPL
   Enter quantity of AAPL: 10
   Enter stock symbol (or 'done' to finish): META
   Enter quantity of META: 5
   Enter stock symbol (or 'done' to finish): done
   `

4. View results in the terminal and check the generated file:
   - portfolio_tracker.csv (or timestamped version if enabled).

---

📊 Example Output
`
Your Portfolio:
AAPL: 10 shares → $1800
META: 5 shares → $1250

Total Investment Value: $3050
Portfolio saved to portfolio_tracker.csv
`

---

📂 File Structure
`
stock-portfolio-tracker/
│
├── portfolio_tracker.py   # Main program
├── README.md              # Project documentation
└── portfolio_tracker.csv  # Generated output file (created after run)
`

---

✨ Future Improvements
- Fetch live stock prices using an API.
- Add support for multiple currencies.
- Track portfolio performance over time.

---

📜 License
This project is licensed under the MIT License — feel free to use, modify, and share.
`

---

This README will make your GitHub repo look polished and professional.  

👉 Do you want me to also create a GitHub‑ready folder structure with .gitignore and MIT License file so you can upload everything in one go?
