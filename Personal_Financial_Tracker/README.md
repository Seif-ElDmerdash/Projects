# Personal Finance Tracker

## Description
The Personal Finance Tracker is a software program that provides a simple and straightforward way to keep records of your personal finances. It creates one place for all the user’s financial records, allowing them to view all the earnings and transactions that have taken place, view how much they spend based on data entry, categorize the transactions by their spending habits, and present the data visually. 

It was collaboratively developed by **Badr Muhammad** (Team Leader & GUI Developer), **Karim ElBolok** (Co-GUI Developer & Visualisation Lead), and **Seif El Dmerdash & Youssef Maged** (BackEnd Developers). Built using CustomTkinter for a clean interface and Matplotlib for data visualization, the project's foundational development was supported by concepts from Harvard's CS50P introductory course for Python.

## Features
* **Accurate Data:** As soon as the user enters information into the program, it provides them with calculated accurate net balances in real-time.
* **User-friendly Design:** The program is built to be as user-friendly as possible with a clean and simple interface with very little clutter.
* **Visual Representation of Spending:** The pie chart feature provides users with a simple, concise and visual way to see how much they spend by category, at a glance.

## Prerequisites
* Python 3.x
* `customtkinter`
* `matplotlib`

## Usage
How to use the software:
1. **Launch:** Run the script. You will see your initial balances (set to your budget by default) displayed on top.
2. **Set Budgets:** Input the limits for each category in set category budgets.
3. **Add Transaction:** 
   * Select from the drop-down menu.
   * Input the Amount in the entry box.
   * Depending on the user’s choice, it will automatically assign the transaction as an Expense or an Income. 
   * Click "Add Transaction.". The balance will be updated immediately.
4. **Navigate Views:**
   * The "View History" button will allow you to see the chronological order of all movements.
   * Click "Detailed Summary" for quick calculation of total money in vs. money out.
   * Click on "View Pie Chart" to view the graphical categorization of your expenditure.

## Project Structure
* `Personal_Financial_Tracker.py`: The main script that runs the application, containing the GUI framework built with CustomTkinter and the backend functions.
* `finance.csv`: A database file initialized by the program to store all transaction records, including headers for date, description, amount, type, Total_balance, and Net_balance.
* `Summary.csv`: A separate database file created to store summarized spending data across categories against their respective limits.