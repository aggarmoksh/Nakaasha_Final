# ===========
#   Imports
# ===========
import sqlite3 as sql

# ========================
#  Connecting to database
# ========================
conn = sql.connect("test.db")
cur = conn.cursor()

# =================
#  Query execution
# =================
query = ('''CREATE TABLE NEW
    (FIRSTNAME TEXT NOT NULL,
     LASTNAME TEXT NOT NULL,
     USERNAME TEXT NOT NULL,
     PASSWORD TEXT NOT NULL,
     CITY TEXT NOT NULL,
     STATE TEXT NOT NULL,
     PINCODE  INT);''')
cur.execute(query)

# ================================
#  Closing connection to database
# ================================
conn.close()