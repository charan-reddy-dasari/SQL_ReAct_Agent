import sqlite3

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    experience INTEGER
)
""")

employees = [
    (1, "Ravi", "IT", 80000, 4),
    (2, "Rahul", "HR", 50000, 2),
    (3, "Kiran", "IT", 90000, 5),
    (4, "Amit", "Finance", 60000, 3),
    (5, "Suresh", "IT", 100000, 7),
    (6, "Priya", "HR", 55000, 3),
    (7, "Neha", "Finance", 75000, 6),
    (8, "Arjun", "Marketing", 65000, 4),
    (9, "Sneha", "Marketing", 70000, 5),
    (10, "Vijay", "Finance", 85000, 8)
]

cursor.executemany("""
INSERT OR IGNORE INTO employees
VALUES (?, ?, ?, ?, ?)
""", employees)

conn.commit()
conn.close()

print("Database created successfully!")