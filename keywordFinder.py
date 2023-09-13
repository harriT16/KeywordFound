import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

def search_keyword_on_website():
    url = url_entry.get()
    keyword = keyword_entry.get()
    output_text.delete(1.0, tk.END) 
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            output_text.insert(tk.END, f"Failed to get URL. Exit: {response.status_code}\n")
            return
        
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.stripped_strings 
        
        found = False
        for i, string in enumerate(texts):
            if keyword.lower() in string.lower():
                output_text.insert(tk.END, f"Keyword '{keyword}' found: {string}\n")
                found = True
        
        if not found:
            output_text.insert(tk.END, f"Keyword '{keyword}' not found on the website.\n")
            
    except Exception as e:
        output_text.insert(tk.END, f"An error occurred: {e}\n")

root = tk.Tk()
root.title('Keyword Searcher')

url_label = ttk.Label(root, text="Enter URL:")
url_label.pack(side="left")
url_entry = ttk.Entry(root, width=50)
url_entry.pack(side="left")

keyword_label = ttk.Label(root, text="Enter Keyword:")
keyword_label.pack(side="left")
keyword_entry = ttk.Entry(root, width=20)
keyword_entry.pack(side="left")

# Add Search button
search_button = ttk.Button(root, text="Search", command=search_keyword_on_website)
search_button.pack(side="left")

# Add Output Text Box
output_text = tk.Text(root, wrap='word', width=80, height=20)
output_text.pack(side="bottom", fill="both", expand=True)

root.mainloop()
