import tkinter as tk
import re
import random
import datetime
import tkinter.scrolledtext as scrolledtext


class DodgeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Dodge")
        master.configure(bg="#1E1E1E")

        # Create the text input box
        self.text_box = tk.scrolledtext.ScrolledText(master, height=10, width=50, wrap="word", bg="#2E2E2E", fg="#F8F8F8", insertbackground="#F8F8F8", highlightbackground="#2E2E2E", highlightcolor="#F8F8F8", font=("Helvetica", 12))
        self.text_box.pack(fill="both", expand=True)

        # Create the "Check" button
        self.check_button = tk.Button(master, text="Check", command=self.check_text, bg="#F8F8F8", fg="#1E1E1E", activebackground="#1E1E1E", activeforeground="#F8F8F8", font=("Helvetica", 12, "bold"))
        self.check_button.pack(pady=10)

        # Create the output text box
        self.output_text_box = tk.scrolledtext.ScrolledText(master, height=10, width=50, wrap="word", bg="#2E2E2E", fg="#F8F8F8", insertbackground="#F8F8F8", highlightbackground="#2E2E2E", highlightcolor="#F8F8F8", font=("Helvetica", 12))
        self.output_text_box.pack(fill="both", expand=True)

        # Create the "Copy" button
        self.copy_button = tk.Button(master, text="Copy", command=self.copy_text, bg="#F8F8F8", fg="#1E1E1E", activebackground="#1E1E1E", activeforeground="#F8F8F8", font=("Helvetica", 12, "bold"))
        self.copy_button.pack(pady=10)

        # Create the list of ChatGPT detectors
        self.detectors = {
            "GPTZero": lambda text: random.choice([True, False]),  # Replace with your actual detection logic
            "contentatscale.ai": lambda text: random.choice([True, False])   # Replace with your actual detection logic
        }

        # Create the detector list label
        self.detector_list_label = tk.Label(master, text=self.get_detector_list_text(), bg="#1E1E1E", fg="#F8F8F8", font=("Helvetica", 10))
        self.detector_list_label.pack(pady=5)


    def check_text(self):
        # Get the text from the input box
        text = self.text_box.get("1.0", "end-1c")

        # Check if the text was written by ChatGPT
        is_chatgpt = any(detector(text) for detector in self.detectors.values())  # Use the detectors list to check if the text was written by ChatGPT

        if is_chatgpt:
            # Generate a fake text to trick GPTZero
            fake_text = self.generate_fake_text(text)
            self.output_text_box.config(state="normal")
            self.output_text_box.delete("1.0", "end")
            self.output_text_box.insert("end", f"The input text was written by ChatGPT with a probability of 80%. \n\nHere's a modified version of the text that looks more like it was written by a human:\n{'-'*90}\n{fake_text}")
            self.output_text_box.config(state="disabled")
        else:
            self.output_text_box.config(state="normal")
            self.output_text_box.delete("1.0", "end")
            self.output_text_box.insert("end", "The input text was not written by ChatGPT.")
            self.output_text_box.config(state="disabled")

        # Update the detector list label
        self.detector_list_label.config(text=self.get_detector_list_text())
    def generate_fake_text(self, text):
        # Replace this with your actual text modification logic
        return text.replace(".", ". ").replace(",", ", ")

    def copy_text(self):
        # Copy the modified text to the clipboard
        modified_text = self.output_text_box.get("1.0", "end-1c")
        self.master.clipboard_clear()
        self.master.clipboard_append(modified_text)

    def get_detector_list_text(self):
        # Generate a list of detectors and their status
        detector_list = ["detectors:"]
        for name, detector in self.detectors.items():
            status = "working" if detector("test text") is not None else "not working"
            detector_list.append(f"{name}: {status}")

        # Combine the list into a string with line breaks
        detector_list_text = "\n".join(detector_list)

        # Add the date and time the detector list was last updated
        current_time = "03/03/2023"
        detector_list_text += f"\n\nLast updated: {current_time}"

        return detector_list_text

root = tk.Tk()
my_gui = DodgeGUI(root)
root.mainloop()
