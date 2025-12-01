from src.db import get_connection

def test_has_rows():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM athletes")
    (count,) = cur.fetchone()
    assert count > 0
