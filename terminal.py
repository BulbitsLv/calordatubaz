from datetime import datetime
import sqlite3


def registret_lietotaju():
  conn = sqlite3.connect("calorie_tracker.db")
  cursor = conn.cursor()
  cursor.execute("PRAGMA foreign_keys = ON;")

  print("\n--- Jauna lietotāja reģistrācija ---")
  vards = input("Ievadi savu vārdu: ")
  epasts = input("Ievadi e-pastu: ")
  mērķis = int(input("Ievadi dienas kaloriju mērķi (piem., 2000): "))
  tagad = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  cursor.execute(
      """
        INSERT INTO users (email, display_name, daily_calorie_goal, created_at)
        VALUES (?, ?, ?, ?)
    """,
      (epasts, vards, mērķis, tagad),
  )

  conn.commit()
  conn.close()
  print("Lietotājs veiksmīgi reģistrēts!")


def pievienot_aktivitati():
  conn = sqlite3.connect("calorie_tracker.db")
  cursor = conn.cursor()
  cursor.execute("PRAGMA foreign_keys = ON;")

  # Parādām lietotājus
  cursor.execute("SELECT id, display_name FROM users")
  lietotaji = cursor.fetchall()
  if not lietotaji:
    print("Vispirms reģistrē vismaz vienu lietotāju!")
    conn.close()
    return

  print("\n--- Reģistrētie lietotāji ---")
  for l in lietotaji:
    print(f"ID: {l[0]} | Vārds: {l[1]}")

  user_id = int(input("Izvēlies lietotāja ID: "))

  # Parādām vingrinājumus
  cursor.execute("SELECT id, name, calories_per_minute FROM exercises")
  vingrinajumi = cursor.fetchall()

  if not vingrinajumi:
    cursor.execute(
        "INSERT INTO exercises (name, calories_per_minute) VALUES (?, ?)",
        ("Skriešana", 10.0),
    )
    conn.commit()
    cursor.execute("SELECT id, name, calories_per_minute FROM exercises")
    vingrinajumi = cursor.fetchall()

  print("\n--- Pieejamie vingrinājumi ---")
  for v in vingrinajumi:
    print(f"ID: {v[0]} | Nosaukums: {v[1]} | kcal/min: {v[2]}")

  exercise_id = int(input("Izvēlies vingrinājuma ID: "))
  ilgums = float(input("Ievadi ilgumu minūtēs: "))

  cursor.execute(
      "SELECT calories_per_minute FROM exercises WHERE id = ?", (exercise_id,)
  )
  rez = cursor.fetchone()
  kalorijas_minutē = rez[0]
  kopējās_kalorijas = ilgums * kalorijas_minutē

  tagad = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  cursor.execute(
      """
        INSERT INTO exercise_logs (user_id, exercise_id, duration_minutes, calories_burned, performed_at)
        VALUES (?, ?, ?, ?, ?)
    """,
      (user_id, exercise_id, ilgums, kopējās_kalorijas, tagad),
  )

  conn.commit()
  conn.close()
  print(
      f"Aktivitāte saglabāta! Sadedzinātas aptuveni {kopējās_kalorijas} kcal."
  )

  if __name__ == "__main__":
    while True:
        print("\n=== CALORIE TRACKER IZVĒLNE ===")
        print("1. Reģistrēt jaunu lietotāju")
        print("2. Pievienot aktivitāti (treniņu)")
        print("3. Iziet")

        izvele = input("Izvēlies darbību (1-3): ")

        if izvele == "1":
            registret_lietotaju()
        elif izvele == "2":
            pievienot_aktivitati()
        elif izvele == "3":
            print("Uz redzēšanos!")
            break
        else:
            print("Nekorekta izvēle, mēģini vēlreiz.")