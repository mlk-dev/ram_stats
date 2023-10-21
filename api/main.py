from fastapi import FastAPI, HTTPException
from db.database import cursor

app = FastAPI()


def get_last_n_records(n):
    """get last n records from database
    :param n
    """
    cursor.execute("SELECT * FROM ram_stats ORDER BY timestamp DESC LIMIT ?", (n,))
    records = cursor.fetchall()
    return records


@app.get("/ram_stats/")
async def read_ram_stats(n: int = 10):
    """read records from output of database"""
    if n < 1:
        raise HTTPException(status_code=400, detail="Invalid value for n")
    records = get_last_n_records(n)
    return records
