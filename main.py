import tkinter as tk
import time
import random


def get_random_sample_text():
    sample_texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is fun and challenging.",
        "Practice makes perfect.",
        "Python is a versatile programming language."
    ]
    return random.choice(sample_texts)


def start_typing_test():
    global sample_text, start_time
    sample_text = get_random_sample_text()
    text_display.config(text=sample_text)
    entry.delete(0, "end")
    result_label.config(text="")

    entry.bind("<Key>", handle_typing)
    start_time = time.time()
    start_button.config(state="disabled")


def handle_typing(event):
    global sample_text, start_time
    if not start_time:
        return

    current_text = entry.get()
    if current_text == sample_text:
        end_time = time.time()
        entry.unbind("<Key>")
        calculate_scores(sample_text, current_text, start_time, end_time)


def calculate_scores(original_text, typed_text, start_time, end_time):
    elapsed_time = end_time - start_time
    words_typed = len(original_text.split())
    characters_typed = len(typed_text)

    errors = count_errors(original_text, typed_text)
    corrected_characters = characters_typed - errors

    wpm = int((words_typed / elapsed_time) * 60)
    cpm = int((corrected_characters / elapsed_time) * 60)

    wpm_text = f"Typing Speed (WPM): {wpm}"
    cpm_text = f"Corrected Characters Per Minute (CPM): {cpm}"

    result_label.config(text=wpm_text + "\n" + cpm_text)


def count_errors(original_text, typed_text):
    errors = 0
    min_len = min(len(original_text), len(typed_text))
    for i in range(min_len):
        if original_text[i] != typed_text[i]:
            errors += 1
    return errors


window = tk.Tk()
window.title("Typing Speed Test")
window.minsize(width=500, height=500)

sample_text = ""
start_time = None

label = tk.Label(window, text="Type the following text:")
label.pack()

text_display = tk.Label(window, text=sample_text)
text_display.pack()

entry = tk.Entry(window)
entry.pack()

start_button = tk.Button(window, text="Start Typing Test", command=start_typing_test)
start_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
