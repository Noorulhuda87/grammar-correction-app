import tkinter as tk
from tkinter import ttk
import openai

# Set your OpenAI API Key
with open("openai_key.txt") as f:
    openai.api_key = f.read().strip()

def correct_grammar():
    user_input = input_text.get("1.0", tk.END).strip()
    if not user_input:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter some text.")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that corrects grammar."},
                {"role": "user", "content": f"Correct the grammar: {user_input}"}
            ],
            temperature=0.2,
            max_tokens=200
        )
        corrected = response['choices'][0]['message']['content'].strip()
        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", "" + corrected + "\n")
        output_text.tag_add("margins", "1.0", "end")
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", f"\nError: {str(e)}\n")
        output_text.tag_add("margins", "1.0", "end")

def apply_input_text_margins(event=None):
    input_text.tag_add("margins", "1.0", "end")

# Create main window
window = tk.Tk()
window.title("Grammar Correction By Noorulhuda")
window.geometry("700x600")
window.configure(bg="#d3d3d3")
window.resizable(False, False)

padding = 15

# Title Label
title_label = tk.Label(window, text="Grammar Correction By Noorulhuda",
                       font=("Helvetica", 20, "bold"), bg="#d3d3d3")
title_label.pack(pady=(10, 20))

# Input Label
input_label = tk.Label(window, text="Insert Text:",
                       font=("Helvetica", 14, "bold"), bg="#d3d3d3")
input_label.pack(anchor="w", padx=padding)

# Frame for input text
input_frame = tk.Frame(window, bg="#d3d3d3")
input_frame.pack(fill=tk.BOTH, padx=padding, pady=(0, 10), expand=True)

# Input Text widget
input_text = tk.Text(input_frame, height=8, wrap=tk.WORD, font=("Helvetica", 13))
input_text.pack(fill=tk.BOTH, expand=True)

# Apply margins to input box

input_text.tag_configure("margins", lmargin1=5, lmargin2=5, rmargin=5, spacing1=3, spacing3=3)
input_text.tag_add("margins", "1.0", "end")
input_text.bind("<KeyRelease>", apply_input_text_margins)  # ensure margins persist

# Correct Button
correct_button = tk.Button(
    window, text="Correct Grammar", font=("Helvetica", 14, "bold"),
    bg="#444444", fg="white", padx=25, pady=12, command=correct_grammar
)
correct_button.pack(pady=(0, 20))

# Output Label
output_label = tk.Label(window, text="Corrected Text:",
                        font=("Helvetica", 14, "bold"), bg="#d3d3d3")
output_label.pack(anchor="w", padx=padding)

# Frame for output text
output_frame = tk.Frame(window, bg="#d3d3d3")
output_frame.pack(fill=tk.BOTH, padx=padding, pady=(0, 10), expand=True)

# Output Text widget
output_text = tk.Text(output_frame, height=8, wrap=tk.WORD, font=("Helvetica", 13))
output_text.pack(fill=tk.BOTH, expand=True)
output_text.tag_configure("margins", lmargin1=3, lmargin2=5, rmargin=3, spacing1=3, spacing3=3)
output_text.insert("1.0", "\n")
output_text.tag_add("margins", "1.0", "end")

# Run app
window.mainloop()
