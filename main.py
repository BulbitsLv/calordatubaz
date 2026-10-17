import sqlite3
import tkinter as tk
from tkinter import messagebox

def get_db():
    conn = sqlite3.connect("calorie_tracker.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

class App:
    def __init__(self, root):
        self.root = root
        root.title("Calorie Tracker - Grafiskā saskarne")
        root.geometry("420x550")

        tk.Label(root, text="Calorie Tracker Vadība", font=("Arial", 14, "bold")).pack(pady=10)

        # Galvenās pogas tabulu apskatei un datu pievienošanai
        btn_configs = [
            ("Skatīt lietotājus", lambda: self.show_table("users")),
            ("Pievienot lietotāju", self.add_user),
            ("Skatīt produktus", lambda: self.show_table("foods")),
            ("Pievienot produktu", self.add_food),
            ("Skatīt vingrojumus", lambda: self.show_table("exercises")),
            ("Skatīt svara žurnālu", lambda: self.show_table("weight_logs")),
            ("Reģistrēt svaru", self.add_weight),
            ("Skatīt maltītes", lambda: self.show_table("meals")),
            ("Skatīt visas citas tabulas", self.show_all_tables_menu),
        ]

        for text, cmd in btn_configs:
            tk.Button(root, text=text, width=32, command=cmd).pack(pady=4)

        tk.Button(root, text="Iziet", width=32, command=root.quit, fg="red").pack(pady=15)

    def show_table(self, table_name):
        w = tk.Toplevel(self.root)
        w.title(f"Tabula: {table_name}")
        w.geometry("500x350")
        
        t = tk.Text(w, wrap=tk.WORD)
        t.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        conn = get_db()
        try:
            for row in conn.execute(f"SELECT * FROM {table_name}"):
                t.insert(tk.END, str(row) + "\n")
        except Exception as e:
            t.insert(tk.END, f"Kļūda: {e}")
        conn.close()
        t.config(state=tk.DISABLED)

    def show_all_tables_menu(self):
        w = tk.Toplevel(self.root)
        w.title("Visas datubāzes tabulas")
        w.geometry("350x400")
        
        tables = [
            "users", "food_categories", "exercises", "foods", 
            "food_servings", "user_goals", "weight_logs", 
            "exercise_logs", "meals", "meal_items"
        ]
        
        tk.Label(w, text="Izvēlies tabulu, ko apskatīt:", font=("Arial", 10, "bold")).pack(pady=5)
        for tbl in tables:
            tk.Button(w, text=tbl, width=25, command=lambda t=tbl: self.show_table(t)).pack(pady=2)

    def add_user(self):
        w = tk.Toplevel(self.root)
        w.title("Pievienot lietotāju")
        tk.Label(w, text="E-pasts:").pack()
        e1 = tk.Entry(w, width=25); e1.pack()
        tk.Label(w, text="Vārds:").pack()
        e2 = tk.Entry(w, width=25); e2.pack()
        tk.Label(w, text="Kaloriju mērķis:").pack()
        e3 = tk.Entry(w, width=25); e3.pack()

        def save():
            conn = get_db()
            conn.execute("INSERT INTO users (email, display_name, daily_calorie_goal, created_at) VALUES (?, ?, ?, datetime('now'))", 
                         (e1.get(), e2.get(), int(e3.get())))
            conn.commit()
            conn.close()
            messagebox.showinfo("OK", "Lietotājs pievienots!")
            w.destroy()
        tk.Button(w, text="Saglabāt", command=save).pack(pady=10)

    def add_food(self):
        w = tk.Toplevel(self.root)
        w.title("Pievienot produktu")
        tk.Label(w, text="Nosaukums:").pack()
        e1 = tk.Entry(w, width=25); e1.pack()
        tk.Label(w, text="Kalorijas (100g):").pack()
        e2 = tk.Entry(w, width=25); e2.pack()

        def save():
            conn = get_db()
            conn.execute("INSERT INTO foods (name, serving_size, serving_unit, calories, protein_g, carbs_g, fat_g, is_verified) VALUES (?, 100, 'g', ?, 0, 0, 0, 1)", 
                         (e1.get(), float(e2.get())))
            conn.commit()
            conn.close()
            messagebox.showinfo("OK", "Produkts pievienots!")
            w.destroy()
        tk.Button(w, text="Saglabāt", command=save).pack(pady=10)

    def add_weight(self):
        w = tk.Toplevel(self.root)
        w.title("Reģistrēt svaru")
        tk.Label(w, text="Lietotāja ID:").pack()
        e1 = tk.Entry(w, width=25); e1.pack()
        tk.Label(w, text="Svars (kg):").pack()
        e2 = tk.Entry(w, width=25); e2.pack()

        def save():
            conn = get_db()
            conn.execute("INSERT INTO weight_logs (user_id, weight_kg, logged_at) VALUES (?, ?, datetime('now'))", 
                         (int(e1.get()), float(e2.get())))
            conn.commit()
            conn.close()
            messagebox.showinfo("OK", "Svars reģistrēts!")
            w.destroy()
        tk.Button(w, text="Saglabāt", command=save).pack(pady=10)

if __name__ == "__main__":
    import database
    root = tk.Tk()
    App(root)
    root.mainloop()