import io
import duckdb
import pandas as pd


con=duckdb.connect(database="data/bd_tables.duckdb",read_only=False)

csv= """
beverage,prices
orange_juice, 2.5
expresso, 3
Tea, 3.5
"""

tab1=pd.read_csv(io.StringIO(csv))
query=con.execute("""
CREATE TABLE IF NOT EXISTS tab1 AS SELECT * FROM tab1
""")