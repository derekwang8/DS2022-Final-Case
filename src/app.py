from flask import Flask, jsonify, request
from db import get_connection
from load_data import init_db

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/athletes")
def athletes():
    limit = int(request.args.get("limit", 5))
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM athletes LIMIT ?", (limit,))
    rows = [dict(row) for row in cur.fetchall()]

    return jsonify(rows)

@app.route("/summary")
def summary():
    conn = get_connection()
    cur = conn.cursor()

    # Total athletes
    cur.execute("SELECT COUNT(*) AS count FROM athletes")
    total = cur.fetchone()["count"]

    # Average scores
    cur.execute("""
        SELECT 
            AVG(Overall_Score) AS avg_overall,
            AVG(A_Score) AS avg_A,
            AVG(B_Score) AS avg_B,
            AVG(C_Score) AS avg_C
        FROM athletes
    """)
    stats = cur.fetchone()

    # Top 5 countries by number of athletes
    cur.execute("""
        SELECT Country, COUNT(*) AS count
        FROM athletes
        GROUP BY Country
        ORDER BY count DESC
        LIMIT 5
    """)
    top_countries = [dict(row) for row in cur.fetchall()]

    return {
        "total_athletes": total,
        "average_scores": {
            "overall": round(stats["avg_overall"], 3),
            "A": round(stats["avg_A"], 3),
            "B": round(stats["avg_B"], 3),
            "C": round(stats["avg_C"], 3)
        },
        "top_countries": top_countries
    }

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=8080)
