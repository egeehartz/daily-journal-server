import sqlite3
import json
from models import Mood

def get_all_moods():
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.mood
        FROM moods e
        """)

        entries = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            mood = Mood(row['id'], row['mood'])
            entries.append(mood.__dict__)

    return json.dumps(entries)