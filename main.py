import tkinter as tk
from tkinter import messagebox
from model import predict_stress
from suggestions import get_suggestions

def analyze():
    try:
        sleep = float(entry_sleep.get())
        activity = float(entry_activity.get())
        screen = float(entry_screen.get())
        mood = int(entry_mood.get())

        result = predict_stress(sleep, activity, screen, mood)
        suggestion = get_suggestions(result)

        result_label.config(text=f"Stress Level: {result}")
        suggestion_label.config(text=suggestion)

        # Alert system
        if result == "High Stress":
            messagebox.showwarning("ALERT 🚨", "High Stress Detected! Take immediate action!")

    except:
        messagebox.showerror("Error", "Enter valid inputs")

root = tk.Tk()
root.title("Smart Stress Monitor")
root.geometry("420x450")

tk.Label(root, text="Sleep Hours").pack()
entry_sleep = tk.Entry(root)
entry_sleep.pack()

tk.Label(root, text="Activity (hrs)").pack()
entry_activity = tk.Entry(root)
entry_activity.pack()

tk.Label(root, text="Screen Time (hrs)").pack()
entry_screen = tk.Entry(root)
entry_screen.pack()

tk.Label(root, text="Mood (1-10)").pack()
entry_mood = tk.Entry(root)
entry_mood.pack()

tk.Button(root, text="Monitor Stress", command=analyze).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

suggestion_label = tk.Label(root, text="", wraplength=300)
suggestion_label.pack()

root.mainloop()