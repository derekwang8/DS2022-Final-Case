from src.db import get_connection, init_db

def test_has_rows():
    # Initialize the database (creates tables and loads CSV)
    init_db()

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM athletes")
    count = cur.fetchone()[0]

    # Should have at least 1 row (WWC17 dataset has 216)
    assert count > 0
