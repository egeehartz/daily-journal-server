import sqlite3
import json
from models import Entry

def get_all_entries():
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.entry,
            e.mood_id
        FROM entries e
        """)

        entries = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            entry = Entry(row['id'], row['date'], row['entry'], row['mood_id'])
            entries.append(entry.__dict__)

    return json.dumps(entries)

# Function with a single parameter
def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.date,
            e.entry,
            e.mood_id
        FROM entries e
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()
        entry = Entry(data['id'], data['date'], data['entry'], data['mood_id'])

        return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))