import pandas_datareader
import matplotlib.pyplot as plt
import tkinter as tk
import yfinance
import os

dark_blue = "#2a2a72"
light_blue = "#388697"
grey = "#63768d"


def get_data(ticker, start_date, end_date):
    data = pandas_datareader.data.get_data_yahoo(ticker, start_date, end_date)
    with open("StockInfo.txt", "w") as file:
        file.writelines(yfinance.Ticker(ticker).info["longBusinessSummary"])
    os.startfile("StockInfo.txt")

    data['Adj Close'].plot(figsize=(10, 7))
    plt.title("Adjusted Close Price of {}".format(ticker), fontsize=16)
    plt.ylabel('Price', fontsize=16)
    plt.xlabel('Year', fontsize=16)
    plt.grid(which="major", color='k', linestyle='dashdot', linewidth=0.75)
    plt.show()


root = tk.Tk()
root.title("Stock Tracker")
root.config(bg=dark_blue)
root.iconbitmap("stock.ico")
root.geometry("425x325")
root.resizable(0, 0)

title_frame = tk.Frame(root, bg=dark_blue)
title_frame.pack()
ticker_frame = tk.Frame(root, bg=dark_blue)
ticker_frame.pack(pady=10)
main_frame = tk.Frame(root, bg=dark_blue)
main_frame.pack()
button_frame = tk.Frame(root, bg=dark_blue)
button_frame.pack(pady=15)

tk.Label(title_frame, text="Stock Tracker", font=("Segoe", 35), bg=grey, width=15).pack(padx=2, pady=2)

ticker_label = tk.Label(ticker_frame, text="Ticker:", font=("Segoe", 13), bg=grey, width=12)
ticker_label.grid(row=0, column=0, padx=2, pady=5)
ticker_entry = tk.Entry(ticker_frame, font=("Segoe", 13), bg=grey)
ticker_entry.grid(row=1, column=0, padx=2, pady=5)

start_year_label = tk.Label(main_frame, text="Start Year:", font=("Segoe", 13), bg=grey, width=12)
start_year_label.grid(row=0, column=0, padx=15, pady=5)
start_year_entry = tk.Entry(main_frame, font=("Segoe", 13), bg=grey)
start_year_entry.grid(row=1, column=0, padx=15, pady=5)

end_year_label = tk.Label(main_frame, text="End Year:", font=("Segoe", 13), bg=grey, width=12)
end_year_label.grid(row=0, column=1, padx=15, pady=5)
end_year_entry = tk.Entry(main_frame, font=("Segoe", 13), bg=grey)
end_year_entry.grid(row=1, column=1, padx=15, pady=5)

get_info_button = tk.Button(button_frame, text="Get Info", font=("Segoe", 25), bg=grey, width=15, command=lambda:get_data(ticker_entry.get(), start_year_entry.get(), end_year_entry.get()))
get_info_button.pack(padx=5, pady=5)

root.mainloop()
