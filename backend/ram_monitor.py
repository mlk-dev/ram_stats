import psutil
import time
from db.database import connection, cursor


def get_ram_stats():
    """get RAM statistics from system"""
    ram = psutil.virtual_memory()
    total = ram.total >> 20
    free = ram.free >> 20
    used = ram.used >> 20
    cursor.execute("INSERT INTO ram_stats (total, free, used) VALUES (?, ?, ?)", (total, free, used))
    connection.commit()


def collect_ram_stats_periodically(interval=10):
    while True:
        get_ram_stats()
        time.sleep(interval)
