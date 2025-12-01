import csv
import sqlite3
from db import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS athletes;")

    cur.execute("""
        CREATE TABLE athletes (
            Name TEXT,
            Country TEXT,
            Overall_Score REAL,
            Rank INTEGER,
            A_Score REAL,
            B_Score REAL,
            C_Score REAL,
            Time REAL,
            PlaceCat TEXT,
            Region TEXT,
            Event TEXT,
            Gender TEXT,
            B_Score_Cat TEXT,
            A_Ded_Cnt INTEGER,
            Nandu_Miss INTEGER,
            Nandu_Total INTEGER,
            Nandu_Completed TEXT
        );
    """)

    with open("assets/WWC17.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [tuple(row.values()) for row in reader]

    placeholders = ",".join(["?"] * 17)

    cur.executemany(
        f"INSERT INTO athletes VALUES ({placeholders})",
        rows
    )

    conn.commit()
    conn.close()
    print("Database initialized with WWC17 dataset.")

if __name__ == "__main__":
    init_db()
