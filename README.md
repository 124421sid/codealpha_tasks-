# 📈 Stock Portfolio Tracker

A simple command-line **Stock Portfolio Tracker** built with Python. This application allows users to create a stock portfolio, calculate the total investment, display a portfolio summary, and save the report as a **TXT** or **CSV** file.

---

## 🚀 Features

* View a list of available stocks and their prices.
* Add multiple stocks with custom quantities.
* Prevents invalid stock names and quantities.
* Calculates total investment automatically.
* Displays a formatted portfolio summary.
* Save portfolio reports in:

  * TXT format
  * CSV format
* User-friendly menu and error handling.

---

## 🛠️ Technologies Used

* Python 3
* File Handling
* Dictionaries
* Functions
* Exception Handling

---

## 📂 Project Structure

```
Stock_Portfolio_Tracker/
│
├── stock_portfolio_tracker.py
├── README.md
├── portfolio_report.txt   (Generated)
└── portfolio_report.csv   (Generated)
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run the program:

```bash
python stock_portfolio_tracker.py
```

---

## 📊 Available Stocks

| Stock | Price (₹) |
| ----- | --------: |
| AAPL  |       180 |
| TSLA  |       250 |
| GOOGL |       140 |
| MSFT  |       380 |
| AMZN  |       170 |
| META  |       320 |
| NFLX  |       420 |

---

## 📷 Sample Output

```
==================================================
STOCK PORTFOLIO TRACKER
==================================================

AVAILABLE STOCKS AND PRICES

AAPL       : ₹180
TSLA       : ₹250
GOOGL      : ₹140
MSFT       : ₹380
AMZN       : ₹170
META       : ₹320
NFLX       : ₹420

Enter stock name: AAPL
Enter quantity: 5

Added 5 shares of AAPL

Portfolio Summary

Stock      Price    Quantity    Total Value
AAPL       ₹180          5          ₹900

TOTAL INVESTMENT: ₹900
```

---

## 📁 Output Files

The application can generate:

* `portfolio_report.txt`
* `portfolio_report.csv`

These files contain the complete portfolio summary and total investment.

---

## 🎯 Future Improvements

* Fetch real-time stock prices using an API.
* Portfolio profit/loss calculation.
* Graphical User Interface (GUI).
* Database integration.
* Portfolio history and analytics.

---

## 👨‍💻 Author

**Siddhant Chamoli**

Developed as part of the **CodeAlpha Python Programming Internship**.
