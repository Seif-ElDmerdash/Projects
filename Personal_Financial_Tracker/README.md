# Personal Finance Tracker

## Overview

A desktop-based personal finance management application built with Python. The Personal Finance Tracker provides users with a centralized platform to record transactions, monitor spending habits, set budget limits, and visualize financial data through interactive charts and detailed reports.

## What This Project Does

This application empowers users to gain control over their personal finances by:

- **Recording Transactions** – Log all income and expenses with timestamps and category classification
- **Real-Time Balance Tracking** – Instant calculation and display of current net balance
- **Budget Management** – Set spending limits for each category and monitor adherence
- **Spending Analytics** – View comprehensive spending patterns with visual pie charts
- **Transaction History** – Access chronological records of all financial movements
- **Detailed Summaries** – Generate quick reports showing total income vs. total expenses

## Key Features

- **Accurate Real-Time Data** – Automatic calculation of net balances immediately upon transaction entry
- **User-Friendly Interface** – Clean, intuitive design with minimal clutter built using CustomTkinter
- **Visual Spending Breakdown** – Pie chart visualization for easy understanding of spending distribution by category
- **Category-Based Organization** – Automatic categorization of transactions based on user selection
- **Transaction Categorization** – Flexible category system supporting both income and expense tracking
- **Budget Alerts** – Track spending against defined category limits

## Prerequisites & Installation

### Requirements
- Python 3.x
- `customtkinter` – Modern GUI framework
- `matplotlib` – Data visualization and charting

### Setup

```bash
pip install customtkinter matplotlib
```

## Usage Guide

### Launching the Application

```bash
python Personal_Financial_Tracker.py
```

### Step-by-Step Guide

1. **Initial Setup**
   - Upon launch, view your current balance (default set to your defined budget)
   - Set spending limits for each category under "Set Category Budgets"

2. **Adding Transactions**
   - Select a category from the dropdown menu
   - Enter the transaction amount
   - System automatically classifies as Income or Expense based on selection
   - Click "Add Transaction" to record (balance updates immediately)

3. **Viewing Financial Data**
   - **View History** – See all transactions in chronological order with full details
   - **Detailed Summary** – Quick overview of total income vs. total expenses
   - **View Pie Chart** – Visual breakdown of spending by category

4. **Budget Monitoring**
   - Compare actual spending against set category limits
   - Track progress toward financial goals

## Project Architecture

| Component | Description |
|-----------|-------------|
| `Personal_Financial_Tracker.py` | Main application script containing GUI framework (CustomTkinter) and backend logic |
| `finance.csv` | Transaction database storing date, description, amount, type, and balances |
| `Summary.csv` | Summary database for categorized spending totals vs. budget limits |

### Data Storage
- **finance.csv** – Record: Date, Description, Amount, Type (Income/Expense), Total Balance, Net Balance
- **Summary.csv** – Record: Category, Total Spending, Budget Limit, Remaining Budget

## Technology Stack

- **GUI Framework** – CustomTkinter for modern, responsive interface
- **Data Visualization** – Matplotlib for charts and graphs
- **Data Storage** – CSV files for persistent transaction records
- **Language** – Python 3.x

## Contributors

- **Badr Muhammad** – Team Leader & GUI Developer
- **Karim ElBolok** – Co-GUI Developer & Visualization Lead
- **Seif El Dmerdash** – Backend Developer
- **Youssef Maged** – Backend Developer

*Project built with foundational concepts from Harvard's CS50P introductory Python course.*