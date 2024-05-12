import sqlite3 as sq

db = sq.connect("tg.db")
cur = db.cursor()


async def db_start():
    cur.execute('''CREATE TABLE IF NOT EXISTS accounts(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id VARCHAR NOT NULL,
                admin_level INTEGER DEFAULT 0,
                banned_time INTEGER DEFAULT 0)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS reports(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_reporter INTEGER NOT NULL,
                id_moderator INTEGER NOT NULL,
                text TEXT NOT NULL,
                submission_time DATETIME NOT NULL,
                status SMALLINT NOT NULL)''')
    db.commit()


async def cmd_start_db(user_id):
    user = cur.execute(f"SELECT * FROM accounts WHERE tg_id = {user_id}")
    print(user.fetchone())
    if user is None:
        cur.execute(f"INSERT INTO accounts (tg_id, admin_level, banned_time) VALUES ({user_id}, 0, 0)")
        db.commit()

# async def get_admin_level(user_id):
#     user = cur.execute(f"SELECT admin_level FROM accounts WHERE id == {user_id}").fetchone()
#     if not user:
#         return None
#     db.commit()