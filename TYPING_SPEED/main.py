import tkinter as tk

from tkinter import messagebox

import time

import random



# Sample sentences to type

SENTENCES = [

    "The quick brown fox jumps over the lazy dog.",

    "A journey of a thousand miles begins with a single step.",

    "To be or not to be, that is the question.",

    "All that glitters is not gold.",

    "Practice makes perfect.",

    "Better late than never.",

    "Actions speak louder than words."

]



class TypingSpeedTestApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Typing Speed Test")

        self.root.geometry("600x400")



        self.start_time = None

        self.sentence = random.choice(SENTENCES)



        # UI Elements

        self.label = tk.Label(root, text="Type the following sentence:", font=("Arial", 14))

        self.label.pack(pady=10)



        self.sentence_label = tk.Label(root, text=self.sentence, font=("Arial", 12), wraplength=500)

        self.sentence_label.pack(pady=10)



        self.input_text = tk.Text(root, height=5, width=60, font=("Arial", 12))

        self.input_text.pack(pady=10)



        self.start_button = tk.Button(root, text="Start", command=self.start_test, font=("Arial", 12))

        self.start_button.pack(pady=10)



        self.finish_button = tk.Button(root, text="Finish", command=self.finish_test, font=("Arial", 12), state=tk.DISABLED)

        self.finish_button.pack(pady=10)



        self.result_label = tk.Label(root, text="", font=("Arial", 14))

        self.result_label.pack(pady=10)



    def start_test(self):

        self.start_time = time.time()

        self.input_text.delete(1.0, tk.END)

        self.input_text.focus()

        self.finish_button.config(state=tk.NORMAL)

        self.result_label.config(text="")



    def finish_test(self):

        if not self.start_time:

            messagebox.showwarning("Warning", "Click Start before finishing!")

            return



        end_time = time.time()

        elapsed_time = end_time - self.start_time

        self.start_time = None



        typed_text = self.input_text.get(1.0, tk.END).strip()



        # Calculate typing speed

        word_count = len(typed_text.split())

        wpm = (word_count / elapsed_time) * 60



        # Calculate accuracy

        original_words = self.sentence.split()

        typed_words = typed_text.split()

        correct_words = sum(1 for ow, tw in zip(original_words, typed_words) if ow == tw)

        accuracy = (correct_words / len(original_words)) * 100



        self.result_label.config(text=f"Speed: {wpm:.2f} WPM | Accuracy: {accuracy:.2f}%")



        self.finish_button.config(state=tk.DISABLED)

        self.input_text.delete(1.0, tk.END)

        self.sentence = random.choice(SENTENCES)

        self.sentence_label.config(text=self.sentence)



if __name__ == "__main__":

    root = tk.Tk()

    app = TypingSpeedTestApp(root)

    root.mainloop()