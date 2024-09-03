import tkinter as tk
import answer_finder

def submit_question():
    # Get the text from the Text widget
    question = question_entry.get(1.0, tk.END).strip()
    answer = answer_finder.get_answer(question)  # Call the get_answer function
    answer_text.config(state=tk.NORMAL)
    answer_text.delete(1.0, tk.END)
    answer_text.insert(tk.END, f"Answer to \"{question}\":\n{answer}")
    answer_text.config(state=tk.DISABLED)

def clear_text():
  # Check if question_entry is an Entry widget
  if isinstance(question_entry, tk.Entry):
      question_entry.delete(0, tk.END)
  else:  # Assuming question_entry is a Text widget
      question_entry.delete(1.0, tk.END)
  # Check if answer_text is an Entry widget
  if isinstance(answer_text, tk.Entry):
      answer_text.delete(0, tk.END)
  else: # Assuming answer_text is a Text widget
      answer_text.delete(1.0, tk.END)  
      

# Create the main window
window = tk.Tk()
window.title("AI Language Model V1 Interpret")
window.configure(bg="#03c2fc")  # Light blue background

# Make the window resizable
window.resizable(True, True)

# Create a frame to hold the widgets
frame = tk.Frame(window, padx=10, pady=10)
frame.configure(bg="#03c2fc")
frame.pack(fill=None, expand=True)

# Create labels
question_label = tk.Label(frame, text="Enter your question:", bg="#03c2fc")
question_label.grid(row=0, column=0, sticky="w")

# Create a Text widget for the question with word wrap
question_entry = tk.Text(frame, wrap=tk.WORD, height=5)
question_entry.grid(row=1, column=0, sticky="nsew")

# Add a scrollbar to the question text box
question_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=question_entry.yview)
question_scrollbar.grid(row=1, column=1, sticky="ns")
question_entry['yscrollcommand'] = question_scrollbar.set

# Create an answer label
answer_label = tk.Label(frame, text="Answer:", bg="#03c2fc")
answer_label.grid(row=3, column=0, sticky="w")

# Create a Text widget for the answer with word wrap
answer_text = tk.Text(frame, state=tk.DISABLED, wrap=tk.WORD, height=10)
answer_text.grid(row=4, column=0, sticky="nsew")

# Add a scrollbar to the answer text box
answer_scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=answer_text.yview)
answer_scrollbar.grid(row=4, column=1, sticky="ns")
answer_text['yscrollcommand'] = answer_scrollbar.set

# Configure the grid to make the text boxes resizable
frame.columnconfigure(0, weight=1)
frame.rowconfigure(4, weight=1)

# Create a button to submit the question (matching clear button style)
submit_button = tk.Button(frame, text="Submit", fg="white", bg="green", command=submit_question)
submit_button.grid(row=7, column=0, pady=10, sticky="ew")

# Create the clear button (matching submit button style)
clear_button = tk.Button(frame, text="Clear", fg="white", bg="red", command=clear_text)
clear_button.grid(row=8, column=0, pady=10, sticky="ew")

# Start the main loop
window.mainloop()
