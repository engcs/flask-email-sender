"""
ESTE SCRIPT SERVE APENAS PARA FINS DIDÁTICOS
"""
# import sqlite3 as lite
# conn = lite.connect('subs.db')
# cur = conn.cursor()
# def get_posts():
#     with conn:
#         cur.execute("SELECT * FROM Subscribers")
#         return cur.fetchall()

from rich.console import Console
from rich.table import Table
from sqlalchemy import create_engine, MetaData, Table as sqlTable, select

engine = create_engine('sqlite:///subs.db', echo=False)
connection = engine.connect()
metadata = MetaData()
show = sqlTable('Subscribers', metadata, autoload=True, autoload_with = engine)
query = select([show])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
data = result_set

table = Table(title="Subscribers")

table.add_column("Id", justify="left", style="cyan", no_wrap=True)
table.add_column("Name", justify="left", style="magenta", no_wrap=True)
table.add_column("Date Created", justify="left", style="green", no_wrap=True)

for row in data:
    table.add_row(*[str(cell) for cell in row])

console = Console()
console.print(table)
