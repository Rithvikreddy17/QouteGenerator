import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

class MotivationalQuoteGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Motivational Quote Generator")
        self.root.geometry("400x300")

        self.quote_label = tk.Label(root, text="", wraplength=350, font=("Helvetica", 12), pady=20)
        self.quote_label.pack()

        self.next_button = tk.Button(root, text="Next Quote", command=self.show_next_quote)
        self.next_button.pack()

        # Database initialization
        self.connection = sqlite3.connect("quotes.db")
        self.cursor = self.connection.cursor()

        # Create quotes table if not exists
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS quotes (id INTEGER PRIMARY KEY, quote TEXT)''')
        self.connection.commit()

        # Insert some sample quotes into the database
        self.insert_sample_quotes()

        # Load and display an initial quote
        self.show_next_quote()

    def insert_sample_quotes(self):
        quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Believe you can and you're halfway there. - Theodore Roosevelt",
            "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "Strive not to be a success, but rather to be of value. - Albert Einstein"
        ]

        for quote in quotes:
            self.cursor.execute("INSERT INTO quotes (quote) VALUES (?)", (quote,))
            self.connection.commit()

    def show_next_quote(self):
        # Retrieve all quotes from the database
        self.cursor.execute("SELECT quote FROM quotes")
        quotes = self.cursor.fetchall()

        if quotes:
            # Choose a random quote from the list
            random_quote = random.choice(quotes)
            self.quote_label.config(text=random_quote[0])
        else:
            messagebox.showinfo("No Quotes", "No quotes found in the database.")

    def __del__(self):
        # Close the database connection when the program ends
        self.connection.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = MotivationalQuoteGenerator(root)
    root.mainloop()
