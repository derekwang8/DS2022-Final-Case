import sqlite3
import csv
import os

DB_PATH = "wushu.db"
CSV_PATH = os.path.join("assets", "WWC17.csv")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Create the athletes table and load CSV data if not already present."""
    conn = get_connection()
    cur = conn.cursor()

    # Create table if missing
    cur.execute("""
        CREATE TABLE IF NOT EXISTS athletes (
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
        )
    """)

    # Check if table already populated
    cur.execute("SELECT COUNT(*) FROM athletes")
    count = cur.fetchone()[0]

    if count == 0:
        # Load CSV
        with open(CSV_PATH, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            rows = [
                (
                    row["Name"],
                    row["Country"],
                    float(row["Overall_Score"]),
                    int(row["Rank"]),
                    float(row["A_Score"]),
                    float(row["B_Score"]),
                    float(row["C_Score"]),
                    float(row["Time"]),
                    row["PlaceCat"],
                    row["Region"],
                    row["Event"],
                    row["Gender"],
                    row["B_Score_Cat"],
                    int(row["A_Ded_Cnt"]),
                    int(row["Nandu_Miss"]),
                    int(row["Nandu_Total"]),
                    row["Nandu_Completed"]
                )
                for row in reader
            ]

            cur.executemany("""
                INSERT INTO athletes VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, rows)

    conn.commit()
    conn.close()
