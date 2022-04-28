"""
ESTE SCRIPT SERVE APENAS PARA FINS DIDÁTICOS
"""
from sqlalchemy import create_engine
# engine = create_engine('sqlite:///subs.db', echo=False)

import sqlite3 as lite
from rich.console import Console
from rich.table import Table

conn = lite.connect('subs.db')
cur = conn.cursor()


def get_posts():
    with conn:
        cur.execute("SELECT * FROM Subscribers")
        return cur.fetchall()


data = get_posts()
table = Table(title="Subscribers")

table.add_column("Id", justify="left", style="cyan", no_wrap=True)
table.add_column("Name", justify="left", style="magenta", no_wrap=True)
table.add_column("Date Created", justify="left", style="green", no_wrap=True)


for row in data:
    table.add_row(*[str(cell) for cell in row])


console = Console()
console.print(table)
