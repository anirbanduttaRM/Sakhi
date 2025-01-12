import tkinter as tk
from tkinter import messagebox, ttk  # ttk for the dropdown box


class ExpectingMotherBotFrontend:
    def __init__(self, backend):
        self.backend = backend
        self.window = tk.Tk()
        self.window.title("BloomBot: Pregnancy Companion")
        self.window.geometry("500x650")
        self.window.resizable(True, True)
        
        # Set a background color and font style
        self.window.config(bg="#eaf6ff")  # Light blue background
        self.title_font = ("Helvetica", 18, "bold")
        self.button_font = ("Helvetica", 12)
        self.text_font = ("Helvetica", 14, "bold")
        
        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(
            self.window,
            text="BloomBot: Your Pregnancy Companion",
            font=self.title_font,
            bg="#007acc",  # Blue for header
            fg="white",
            anchor="center"
        )
        title_label.pack(pady=10, padx=10, fill="x")

        # Tip Button
        tip_button = tk.Button(
            self.window,
            text="Get Daily Pregnancy Tip",
            font=self.button_font,
            bg="#007acc",  # Blue button
            fg="white",
            padx=10,
            command=self.show_pregnancy_tip
        )
        tip_button.pack(pady=10, fill="x", padx=20)

        # Nutrition Advice Dropdown and Button
        nutrition_frame = tk.Frame(self.window, bg="#eaf6ff")
        nutrition_label = tk.Label(
            nutrition_frame,
            text="Select Week for Nutrition Advice:",
            font=self.button_font,
            bg="#eaf6ff",
            fg="#007acc",
            anchor="w"
        )
        nutrition_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.week_dropdown = ttk.Combobox(
            nutrition_frame,
            values=[str(i) for i in range(1, 51)],
            font=self.button_font,
            width=5,
            state="readonly"
        )
        self.week_dropdown.grid(row=0, column=1, padx=5)
        self.week_dropdown.set("1")  # Default value

        nutrition_button = tk.Button(
            nutrition_frame,
            text="Get Advice",
            font=self.button_font,
            bg="#007acc",
            fg="white",
            padx=10,
            command=self.show_nutrition_advice
        )
        nutrition_button.grid(row=0, column=2, padx=5)

        nutrition_frame.pack(pady=10, padx=20, fill="x")

        # Emotional Support Button
        support_button = tk.Button(
            self.window,
            text="Emotional Support Resources",
            font=self.button_font,
            bg="#007acc",
            fg="white",
            padx=10,
            command=self.show_emotional_support
        )
        support_button.pack(pady=10, fill="x", padx=20)

        # Ask the Bot Section
        ask_frame = tk.Frame(self.window, bg="#eaf6ff")
        ask_label = tk.Label(
            ask_frame,
            text="Ask the Bot:",
            font=self.button_font,
            bg="#eaf6ff",
            fg="#007acc",
            anchor="w"
        )
        ask_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.ask_entry = tk.Entry(ask_frame, font=self.text_font, width=40)
        self.ask_entry.grid(row=1, column=0, padx=5, pady=5)

        submit_button = tk.Button(
            ask_frame,
            text="Submit",
            font=self.button_font,
            bg="#007acc",
            fg="white",
            padx=10,
            command=self.submit_to_bot
        )
        submit_button.grid(row=2, column=0, padx=5, pady=5)

        ask_frame.pack(pady=10, fill="x", padx=20)

        # Response Text Area with Scrollbar
        response_frame = tk.Frame(self.window, bg="#eaf6ff")
        scrollbar = tk.Scrollbar(response_frame)
        scrollbar.pack(side="right", fill="y")

        self.response_text = tk.Text(
            response_frame,
            wrap="word",
            height=10,
            width=50,
            font=self.text_font,
            state="disabled",
            bg="#f9f9f9",  # Off-white text area
            fg="#00457c",  # Dark blue text
            yscrollcommand=scrollbar.set
        )
        self.response_text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.response_text.yview)

        response_frame.pack(pady=20, padx=20, fill="both", expand=True)

    def show_pregnancy_tip(self):
        tip = self.backend.get_pregnancy_tip()
        self.display_response(tip)

    def show_nutrition_advice(self):
        week = self.week_dropdown.get()
        if not week.isdigit():
            messagebox.showerror("Input Error", "Please select a valid week number.")
            return
        advice = self.backend.get_nutrition_advice(int(week))
        self.display_response(advice)

    def show_emotional_support(self):
        support = self.backend.get_emotional_support()
        self.display_response(support)

    def submit_to_bot(self):
        user_input = self.ask_entry.get()
        if not user_input.strip():
            messagebox.showerror("Input Error", "Please type your question to submit.")
            return
        response = self.backend.chat_with_bot(user_input)
        self.display_response(response)
        self.ask_entry.delete(0, tk.END)

    def display_response(self, response):
        """Display the response in the text area."""
        self.response_text.config(state="normal")
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, response)
        self.response_text.config(state="disabled")
