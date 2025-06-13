import tkinter as tk

# WhatsApp FAQ database
faq_data = {
    "How do I install WhatsApp?":
        "Go to the App Store or Google Play Store, search for WhatsApp, and tap Install.",
    "How do I backup my chats?":
        "Go to Settings > Chats > Chat backup > Tap 'Back Up'.",
    "How do I restore my chat history?":
        "Uninstall and reinstall WhatsApp. Verify your number and follow the prompt to restore from backup.",
    "How do I block a contact?":
        "Open the chat > Tap the contact's name > Scroll down and tap 'Block Contact'.",
    "How do I delete my WhatsApp account?":
        "Go to Settings > Account > Delete my account and follow the instructions.",
    "How can I use WhatsApp on my computer?":
        "Visit web.whatsapp.com and scan the QR code using WhatsApp on your phone.",
    "Why am I not receiving messages?":
        "Check your internet connection, notification settings, and make sure WhatsApp has background data access.",
    "How do I create a WhatsApp group?":
        "Go to Chats > New Chat > New Group > Add participants and name the group.",
    "What is WhatsApp end-to-end encryption?":
        "Messages and calls are secured so only you and the person you're communicating with can read or listen to them.",
    "How do I change my phone number on WhatsApp?":
        "Go to Settings > Account > Change number and follow the steps."
}

# GUI setup
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("600x450")

# Title label
title_label = tk.Label(root, text="💬 WhatsApp FAQ Chatbot", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Dropdown menu
question_var = tk.StringVar(root)
question_var.set("Select a question")

def show_dropdown_answer(*args):
    selected = question_var.get()
    if selected in faq_data:
        response_label.config(text="Bot: " + faq_data[selected])
    else:
        response_label.config(text="")

dropdown = tk.OptionMenu(root, question_var, *faq_data.keys())
dropdown.config(width=60, font=("Arial", 11))
dropdown.pack(pady=10)

question_var.trace("w", show_dropdown_answer)

# Response display label
response_label = tk.Label(root, text="", wraplength=550, font=("Arial", 12), fg="blue", justify="left")
response_label.pack(pady=10)

# Manual input
entry_label = tk.Label(root, text="Or ask your own question below:", font=("Arial", 12))
entry_label.pack(pady=5)

manual_entry = tk.Entry(root, font=("Arial", 12), width=60)
manual_entry.pack(pady=5)

# Ask button
def answer_manual_question():
    user_question = manual_entry.get().strip().lower()
    found = False
    for q, a in faq_data.items():
        if user_question in q.lower():
            response_label.config(text="Bot: " + a)
            found = True
            break
    if not found:
        response_label.config(text="Bot: Sorry, I don't have an answer for that.")

ask_btn = tk.Button(root, text="Ask", command=answer_manual_question, font=("Arial", 12))
ask_btn.pack(pady=10)

root.mainloop()
