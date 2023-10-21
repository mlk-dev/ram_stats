from backend.ram_monitor import get_ram_stats, collect_ram_stats_periodically
from db.database import cursor
import time


def test_get_ram_stats():
    get_ram_stats()
    cursor.execute("SELECT * FROM ram_stats ORDER BY timestamp DESC LIMIT 1")
    record = cursor.fetchone()
    assert record is not None


def test_collect_ram_stats_periodically():
    initial_count = cursor.execute("SELECT COUNT(*) FROM ram_stats").fetchone()[0]
    collect_ram_stats_periodically(interval=1)
    time.sleep(2)
    final_count = cursor.execute("SELECT COUNT(*) FROM ram_stats").fetchone()[0]
    assert final_count > initial_count
