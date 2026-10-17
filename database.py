import sqlite3

database = sqlite3.connect("calorie_tracker.db")
cursor = database.cursor()

# Ieslēdzam ārējo atslēgu atbalstu
database.execute("PRAGMA foreign_keys = ON;")

# 1. users
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        email VARCHAR NOT NULL,
        display_name VARCHAR NOT NULL,
        daily_calorie_goal INTEGER NOT NULL,
        created_at TIMESTAMP NOT NULL
    )
""")

# 2. food_categories
cursor.execute("""
    CREATE TABLE IF NOT EXISTS food_categories (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        description TEXT
    )
""")

# 3. exercises
cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        category VARCHAR,
        met_value REAL,
        calories_per_minute REAL NOT NULL
    )
""")

# 4. foods
cursor.execute("""
    CREATE TABLE IF NOT EXISTS foods (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        brand VARCHAR,
        serving_size REAL NOT NULL,
        serving_unit VARCHAR NOT NULL,
        calories REAL NOT NULL,
        protein_g REAL NOT NULL,
        carbs_g REAL NOT NULL,
        fat_g REAL NOT NULL,
        category_id INTEGER,
        is_verified BOOLEAN,
        FOREIGN KEY (category_id) REFERENCES food_categories(id)
    )
""")

# 5. food_servings
cursor.execute("""
    CREATE TABLE IF NOT EXISTS food_servings (
        id INTEGER PRIMARY KEY,
        food_id INTEGER NOT NULL,
        label VARCHAR NOT NULL,
        amount REAL NOT NULL,
        unit VARCHAR NOT NULL,
        grams REAL,
        FOREIGN KEY (food_id) REFERENCES foods(id)
    )
""")

# 6. user_goals
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_goals (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        effective_from DATE NOT NULL,
        calorie_goal INTEGER NOT NULL,
        protein_goal_g REAL,
        carbs_goal_g REAL,
        fat_goal_g REAL,
        created_at TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")

# 7. weight_logs
cursor.execute("""
    CREATE TABLE IF NOT EXISTS weight_logs (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        weight_kg REAL NOT NULL,
        body_fat_pct REAL,
        logged_at TIMESTAMP NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")

# 8. exercise_logs
cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercise_logs (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        exercise_id INTEGER NOT NULL,
        duration_minutes REAL NOT NULL,
        calories_burned REAL,
        performed_at TIMESTAMP NOT NULL,
        notes TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (exercise_id) REFERENCES exercises(id)
    )
""")

# 9. meals
cursor.execute("""
    CREATE TABLE IF NOT EXISTS meals (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        meal_type VARCHAR NOT NULL,
        eaten_at TIMESTAMP NOT NULL,
        notes TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")

# 10. meal_items
cursor.execute("""
    CREATE TABLE IF NOT EXISTS meal_items (
        id INTEGER PRIMARY KEY,
        meal_id INTEGER NOT NULL,
        food_id INTEGER NOT NULL,
        quantity REAL NOT NULL,
        serving_id INTEGER,
        FOREIGN KEY (meal_id) REFERENCES meals(id),
        FOREIGN KEY (food_id) REFERENCES foods(id),
        FOREIGN KEY (serving_id) REFERENCES food_servings(id)
    )
""")

database.commit()
database.close()