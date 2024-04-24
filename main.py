import os
from summarizer import summarize
from sendOutput import send_to_discord
from contentScraper import scrape_page
from linkScraper import get_urls_from_futuretools
import tkinter as tk
from tkinter import messagebox

def run_summary(url):
    content = scrape_page(url)
    summary = summarize(content, url)
    send_to_discord(summary)

def run_futuretools_summary(number):
    urls = get_urls_from_futuretools()
    for i in range(number):
        url = urls[i]
        content = scrape_page(url)
        summary = summarize(content, url)
        send_to_discord(summary)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Article Summarizer")
        self.master.geometry("400x200")
        self.master.iconbitmap("app_icon.ico")

        self.url_label = tk.Label(self, text="Enter URL:", font=("Helvetica", 10))
        self.url_label.pack(pady=10)

        self.url_entry = tk.Entry(self, width=40, font=("Helvetica", 12))
        self.url_entry.pack(pady=5)

        self.summarize_url_button = tk.Button(self)
        self.summarize_url_button["text"] = "Summarize URL"
        self.summarize_url_button["command"] = lambda: self.run_summary(self.url_entry.get())
        self.summarize_url_button.pack(pady=10)

        self.futuretools_label = tk.Label(self, text="Enter number of articles to summarize:", font=("Helvetica", 10))
        self.futuretools_label.pack(pady=10)

        self.futuretools_entry = tk.Spinbox(self, from_=1, to=100, width=5, font=("Helvetica", 12))
        self.futuretools_entry.pack(pady=5)

        self.summarize_futuretools_button = tk.Button(self)
        self.summarize_futuretools_button["text"] = "Summarize Futuretools"
        self.summarize_futuretools_button["command"] = lambda: self.run_futuretools_summary(int(self.futuretools_entry.get()))
        self.summarize_futuretools_button.pack(pady=10)

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy, font=("Helvetica", 10))
        self.quit.pack(side="bottom", pady=10)

        # Add some padding around the widgets
        for child in self.winfo_children():
            child.pack(padx=10, pady=5)

    def run_summary(self, url):
        try:
            run_summary(url)
            messagebox.showinfo("Success", "Summary sent to Discord")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run_futuretools_summary(self, number):
        try:
            run_futuretools_summary(number)
            messagebox.showinfo("Success", "Summary sent to Discord")
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
app = Application(master=root)
app.mainloop()
