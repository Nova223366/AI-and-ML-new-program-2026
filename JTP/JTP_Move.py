import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from textblob import TextBlob

# Load dataset
try:
    df = pd.read_csv(r"C:\AI and ML new program 2026\Class Work files\Move recommndation system\imdb_top_1000.csv")
except FileNotFoundError:
    messagebox.showerror("Error", "File 'imdb_top_1000.csv' not found!")
    raise SystemExit

# Extract genres
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

# Sentiment label
def senti(p):
    if p > 0:
        return "Positive 😊"
    elif p < 0:
        return "Negative 😞"
    return "Neutral 😐"

# Recommendation function
def recommend(genre=None, mood=None, rating=None, n=5):
    d = df
    if genre:
        d = d[d["Genre"].str.contains(genre, case=False, na=False)]
    if rating is not None:
        d = d[d["IMDB_Rating"] >= rating]

    if d.empty:
        return "No suitable movie recommendations found."

    d = d.sample(frac=1).reset_index(drop=True)
    out = []

    for _, r in d.iterrows():
        ov = r.get("Overview")
        if pd.isna(ov):
            continue

        pol = TextBlob(ov).sentiment.polarity
        out.append((r["Series_Title"], pol))

        if len(out) == n:
            break

    return out if out else "No suitable movie recommendations found."

# Button action
def get_recommendations():
    genre = genre_var.get()
    mood = mood_entry.get()
    rating_input = rating_entry.get()

    # Validate rating
    rating = None
    if rating_input:
        try:
            rating = float(rating_input)
            if not (7.6 <= rating <= 9.3):
                messagebox.showerror("Error", "Rating must be between 7.6 and 9.3")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid rating value")
            return

    recs = recommend(genre, mood, rating)

    result_box.delete(1.0, tk.END)

    if isinstance(recs, str):
        result_box.insert(tk.END, recs)
    else:
        mp = TextBlob(mood).sentiment.polarity
        mood_text = senti(mp)

        result_box.insert(tk.END, f"Your Mood: {mood_text} (Polarity: {mp:.2f})\n\n")
        result_box.insert(tk.END, "Recommended Movies:\n\n")

        for i, (title, pol) in enumerate(recs, 1):
            result_box.insert(
                tk.END,
                f"{i}. {title} (Polarity: {pol:.2f}, {senti(pol)})\n"
            )

# GUI setup
root = tk.Tk()
root.title("🎬 Movie Recommendation System")
root.geometry("600x500")

# Name
tk.Label(root, text="Your Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Genre dropdown
tk.Label(root, text="Select Genre:").pack()
genre_var = tk.StringVar()
genre_dropdown = ttk.Combobox(root, textvariable=genre_var, values=genres)
genre_dropdown.pack()

# Mood input
tk.Label(root, text="Your Mood:").pack()
mood_entry = tk.Entry(root)
mood_entry.pack()

# Rating input
tk.Label(root, text="Minimum IMDB Rating (7.6 - 9.3):").pack()
rating_entry = tk.Entry(root)
rating_entry.pack()

# Button
tk.Button(root, text="Recommend Movies", command=get_recommendations).pack(pady=10)

# Output box
result_box = tk.Text(root, height=15, width=70)
result_box.pack()

# Run app
root.mainloop()