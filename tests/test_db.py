from src.db import get_connection, init_db

def test_has_rows():
    init_db()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM athletes")
    count = cur.fetchone()[0]
    assert count > 0
