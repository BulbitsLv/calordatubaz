import sqlite3

def run():
    # Pārliecināmies, ka datubāze un tabulas eksistē
    import database
    
    conn = sqlite3.connect("calorie_tracker.db")
    conn.execute("PRAGMA foreign_keys = ON;")
    c = conn.cursor()
    
    while True:
        print("\n================ CALORIE TRACKER ================")
        print("1. Skatīt lietotājus (users)")
        print("2. Pievienot lietotāju")
        print("3. Skatīt ēdienu kategorijas (food_categories)")
        print("4. Pievienot ēdienu kategoriju")
        print("5. Skatīt vingrojumus (exercises)")
        print("6. Pievienot vingrojumu")
        print("7. Skatīt produktus (foods)")
        print("8. Pievienot produktu")
        print("9. Skatīt produktu porcijas (food_servings)")
        print("10. Skatīt lietotāju mērķus (user_goals)")
        print("11. Skatīt svara žurnālu (weight_logs)")
        print("12. Pievienot svara ierakstu")
        print("13. Skatīt aktivitāšu žurnālu (exercise_logs)")
        print("14. Skatīt maltītes (meals)")
        print("15. Skatīt maltīšu produktus (meal_items)")
        print("0. Iziet")
        
        choice = input("\nIzvēlies opciju (0-15): ")
        
        if choice == "1":
            for row in c.execute("SELECT * FROM users"): print(row)
        elif choice == "2":
            email = input("E-pasts: ")
            name = input("Vārds: ")
            goal = int(input("Kaloriju mērķis: "))
            c.execute("INSERT INTO users (email, display_name, daily_calorie_goal, created_at) VALUES (?, ?, ?, datetime('now'))", (email, name, goal))
            conn.commit()
            print("Lietotājs pievienots!")
        elif choice == "3":
            for row in c.execute("SELECT * FROM food_categories"): print(row)
        elif choice == "4":
            name = input("Kategorijas nosaukums: ")
            desc = input("Apraksts: ")
            c.execute("INSERT INTO food_categories (name, description) VALUES (?, ?)", (name, desc))
            conn.commit()
            print("Kategorija pievienota!")
        elif choice == "5":
            for row in c.execute("SELECT * FROM exercises"): print(row)
        elif choice == "6":
            name = input("Vingrojuma nosaukums: ")
            cat = input("Kategorija: ")
            cpm = float(input("Kalorijas minūtē: "))
            c.execute("INSERT INTO exercises (name, category, calories_per_minute) VALUES (?, ?, ?)", (name, cat, cpm))
            conn.commit()
            print("Vingrojums pievienots!")
        elif choice == "7":
            for row in c.execute("SELECT * FROM foods"): print(row)
        elif choice == "8":
            name = input("Produkta nosaukums: ")
            cal = float(input("Kalorijas: "))
            c.execute("INSERT INTO foods (name, serving_size, serving_unit, calories, protein_g, carbs_g, fat_g, is_verified) VALUES (?, 100, 'g', ?, 0, 0, 0, 1)", (name, cal))
            conn.commit()
            print("Produkts pievienots!")
        elif choice == "9":
            for row in c.execute("SELECT * FROM food_servings"): print(row)
        elif choice == "10":
            for row in c.execute("SELECT * FROM user_goals"): print(row)
        elif choice == "11":
            for row in c.execute("SELECT * FROM weight_logs"): print(row)
        elif choice == "12":
            uid = int(input("Lietotāja ID: "))
            weight = float(input("Svars (kg): "))
            c.execute("INSERT INTO weight_logs (user_id, weight_kg, logged_at) VALUES (?, ?, datetime('now'))", (uid, weight))
            conn.commit()
            print("Svars reģistrēts!")
        elif choice == "13":
            for row in c.execute("SELECT * FROM exercise_logs"): print(row)
        elif choice == "14":
            for row in c.execute("SELECT * FROM meals"): print(row)
        elif choice == "15":
            for row in c.execute("SELECT * FROM meal_items"): print(row)
        elif choice == "0":
            print("Uz redzēšanos!")
            break
        else:
            print("Nederīga izvēle!")

    conn.close()

if __name__ == "__main__":
    run()