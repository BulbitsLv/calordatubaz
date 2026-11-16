

import sqlite3
import tkinter as tk
import tkinter.ttk
from tkinter import messagebox

def get_db():
    conn = sqlite3.connect("calorie_tracker.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


class App:
    def __init__(self, root):
        self.root = root
        root.title("Calorie Tracker")
        root.geometry("450x650")
        root.configure(bg="#EAF2E9")

        # Virsraksts
        tk.Label(
            root,
            text="Calorie Tracker",
            font=("Arial", 24, "bold"),
            bg="#EAF2E9",
            fg="#28583A"
        ).pack(pady=(20, 5))

        tk.Label(
            root,
            text="Kaloriju uzskaites programma",
            font=("Arial", 11),
            bg="#EAF2E9",
            fg="#526B57"
        ).pack(pady=(0, 20))

        # Pogas
        btn_configs = [
            ("Skatīt lietotājus", lambda: self.show_table("users")),
            ("Pievienot lietotāju", self.add_user),
            ("Skatīt produktus", lambda: self.show_table("foods")),
            ("Pievienot produktu", self.add_food),
            ("Skatīt vingrojumus", lambda: self.show_table("exercises")),
            ("Skatīt svara žurnālu", lambda: self.show_table("weight_logs")),
            ("Reģistrēt svaru", self.add_weight),
            ("Skatīt maltītes", lambda: self.show_table("meals")),
            ("Skatīt citas tabulas", self.show_all_tables_menu),
        ]

        for text, cmd in btn_configs:
            tk.Button(
                root,
                text=text,
                font=("Arial", 11),
                width=30,
                height=2,
                bg="#FFFFFF",
                fg="#28583A",
                activebackground="#CDE3CF",
                relief="flat",
                cursor="hand2",
                command=cmd
            ).pack(pady=4)

        # Iziet poga
        tk.Button(
            root,
            text="Iziet",
            font=("Arial", 11, "bold"),
            width=30,
            height=2,
            bg="#B95B55",
            fg="white",
            activebackground="#963F3A",
            relief="flat",
            cursor="hand2",
            command=root.quit
        ).pack(pady=15)

    # Tabulu apskate
        
    def show_table(self, table_name):
        w = tk.Toplevel(self.root)
        w.title("Tabula: " + table_name)
        w.geometry("750x400")
        w.configure(bg="#EAF2E9")

        tk.Label(
            w,
            text=table_name,
            font=("Arial", 18, "bold"),
            bg="#EAF2E9",
            fg="#28583A"
        ).pack(pady=10)

        conn = get_db()

        try:
            cursor = conn.execute(f"SELECT * FROM {table_name}")
            columns = [description[0] for description in cursor.description]

            frame = tk.Frame(w)
            frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

            tree = tk.ttk.Treeview(
                frame,
                columns=columns,
                show="headings"
            )

            for column in columns:
                tree.heading(column, text=column)
                tree.column(column, width=130, minwidth=80)

            scrollbar_y = tk.ttk.Scrollbar(
                frame, orient=tk.VERTICAL, command=tree.yview
            )
            scrollbar_x = tk.ttk.Scrollbar(
                frame, orient=tk.HORIZONTAL, command=tree.xview
            )

            tree.configure(
                yscrollcommand=scrollbar_y.set,
                xscrollcommand=scrollbar_x.set
            )

            tree.grid(row=0, column=0, sticky="nsew")
            scrollbar_y.grid(row=0, column=1, sticky="ns")
            scrollbar_x.grid(row=1, column=0, sticky="ew")

            frame.grid_rowconfigure(0, weight=1)
            frame.grid_columnconfigure(0, weight=1)

            for row in cursor.fetchall():
                tree.insert("", tk.END, values=row)

        except Exception as e:
            messagebox.showerror("Kļūda", str(e))

        finally:
            conn.close()

    # Visu tabulu izvēlne
    def show_all_tables_menu(self):
        w = tk.Toplevel(self.root)
        w.title("Visas tabulas")
        w.geometry("350x500")
        w.configure(bg="#EAF2E9")

        tk.Label(
            w,
            text="Izvēlies tabulu:",
            font=("Arial", 16, "bold"),
            bg="#EAF2E9",
            fg="#28583A"
        ).pack(pady=15)

        tables = [
            "users", "food_categories", "exercises",
            "foods", "food_servings", "user_goals",
            "weight_logs", "exercise_logs", "meals",
            "meal_items"
        ]

        for tbl in tables:
            tk.Button(
                w,
                text=tbl,
                width=25,
                bg="white",
                fg="#28583A",
                relief="flat",
                command=lambda t=tbl: self.show_table(t)
            ).pack(pady=4)

    # Pievienot lietotāju
    def add_user(self):
        w = tk.Toplevel(self.root)
        w.title("Pievienot lietotāju")
        w.geometry("350x350")
        w.configure(bg="#EAF2E9")

        tk.Label(
            w, text="Pievienot lietotāju",
            font=("Arial", 17, "bold"),
            bg="#EAF2E9", fg="#28583A"
        ).pack(pady=15)

        tk.Label(w, text="E-pasts:", bg="#EAF2E9").pack()
        e1 = tk.Entry(w, width=30)
        e1.pack(pady=5)

        tk.Label(w, text="Vārds:", bg="#EAF2E9").pack()
        e2 = tk.Entry(w, width=30)
        e2.pack(pady=5)

        tk.Label(w, text="Kaloriju mērķis:", bg="#EAF2E9").pack()
        e3 = tk.Entry(w, width=30)
        e3.pack(pady=5)

        def save():
            try:
                conn = get_db()
                conn.execute(
                    """INSERT INTO users
                    (email, display_name, daily_calorie_goal, created_at)
                    VALUES (?, ?, ?, datetime('now'))""",
                    (e1.get(), e2.get(), int(e3.get()))
                )
                conn.commit()
                conn.close()

                messagebox.showinfo("OK", "Lietotājs pievienots!")
                w.destroy()

            except (ValueError, sqlite3.Error) as e:
                messagebox.showerror("Kļūda", str(e))

        tk.Button(
            w, text="Saglabāt",
            bg="#28583A", fg="white",
            width=20, command=save
        ).pack(pady=20)

    # Pievienot produktu
    def add_food(self):
        w = tk.Toplevel(self.root)
        w.title("Pievienot produktu")
        w.geometry("350x300")
        w.configure(bg="#EAF2E9")

        tk.Label(
            w, text="Pievienot produktu",
            font=("Arial", 17, "bold"),
            bg="#EAF2E9", fg="#28583A"
        ).pack(pady=15)

        tk.Label(w, text="Nosaukums:", bg="#EAF2E9").pack()
        e1 = tk.Entry(w, width=30)
        e1.pack(pady=5)

        tk.Label(w, text="Kalorijas (100g):", bg="#EAF2E9").pack()
        e2 = tk.Entry(w, width=30)
        e2.pack(pady=5)

        def save():
            try:
                conn = get_db()
                conn.execute(
                    """INSERT INTO foods
                    (name, serving_size, serving_unit, calories,
                    protein_g, carbs_g, fat_g, is_verified)
                    VALUES (?, 100, 'g', ?, 0, 0, 0, 1)""",
                    (e1.get(), float(e2.get()))
                )
                conn.commit()
                conn.close()

                messagebox.showinfo("OK", "Produkts pievienots!")
                w.destroy()

            except (ValueError, sqlite3.Error) as e:
                messagebox.showerror("Kļūda", str(e))

        tk.Button(
            w, text="Saglabāt",
            bg="#28583A", fg="white",
            width=20, command=save
        ).pack(pady=20)

    # Reģistrēt svaru
    def add_weight(self):
        w = tk.Toplevel(self.root)
        w.title("Reģistrēt svaru")
        w.geometry("350x300")
        w.configure(bg="#EAF2E9")

        tk.Label(
            w, text="Reģistrēt svaru",
            font=("Arial", 17, "bold"),
            bg="#EAF2E9", fg="#28583A"
        ).pack(pady=15)

        tk.Label(w, text="Lietotāja ID:", bg="#EAF2E9").pack()
        e1 = tk.Entry(w, width=30)
        e1.pack(pady=5)

        tk.Label(w, text="Svars (kg):", bg="#EAF2E9").pack()
        e2 = tk.Entry(w, width=30)
        e2.pack(pady=5)

        def save():
            try:
                conn = get_db()
                conn.execute(
                    """INSERT INTO weight_logs
                    (user_id, weight_kg, logged_at)
                    VALUES (?, ?, datetime('now'))""",
                    (int(e1.get()), float(e2.get()))
                )
                conn.commit()
                conn.close()

                messagebox.showinfo("OK", "Svars reģistrēts!")
                w.destroy()

            except (ValueError, sqlite3.Error) as e:
                messagebox.showerror("Kļūda", str(e))

        tk.Button(
            w, text="Saglabāt",
            bg="#28583A", fg="white",
            width=20, command=save
        ).pack(pady=20)


if __name__ == "__main__":
    import database

    root = tk.Tk()
    app = App(root)
    root.mainloop()
