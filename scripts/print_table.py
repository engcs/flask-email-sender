"""
ESTE SCRIPT SERVE APENAS PARA FINS DIDÁTICOS
"""
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///subs.db', echo=False)
table = pd.read_sql_table(table_name='subscribers', con=engine)

print(table)
