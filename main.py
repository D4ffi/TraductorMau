
import google.generativeai as genai
from tkinter import *

API_KEY = "AIzaSyBjEYLrBSBODY-NPmac7yeZmZdp3nSSmmY"

genai.configure(
    api_key=API_KEY

)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

BG_GRAY = "#007A78"
BG_DARK = "#005453"
TEXT_COLOR = "#FFC745"

FONT = ("Calibri", 12)
FONT_BOLD = ("Calibri", 12, "bold")


class Geminipy:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Mauricio-Chat.py")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=400, height=550, bg=BG_DARK)

        # Head label
        head_label = Label(self.window, bg=BG_DARK, fg=TEXT_COLOR, text="Chatea con Gemini.py!", font=FONT_BOLD,
                           pady=10)
        head_label.place(relwidth=1)

        # Divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # Text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_DARK, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scrollbar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # Bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # Message entry box
        self.msg_entry = Entry(bottom_label, bg=BG_DARK, fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=1.0, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

    def _on_enter_pressed(self, e):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        self.window.after(500, self._send_message_to_ai, msg)

    def _send_message_to_ai(self, msg):
        response = chat.send_message(msg)
        self._insert_bot_message(response.text, "Gemini")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

    def _insert_bot_message(self, text, sender):
        msg2 = f"{sender}: {text}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)


if __name__ == "__main__":
    app = Geminipy()
    app.run()
