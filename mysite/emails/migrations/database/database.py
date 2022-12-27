import sqlite3

class MyDatabase:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS email (id INTEGER PRIMARY KEY, email text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT DISTINCT email FROM email")
        rows = self.cur.fetchall()
        return rows
    def check(self, email):
        self.cur.execute("SELECT * FROM email WHERE email=?", (email,))
        rows = self.cur.fetchall()
        return rows

    def insert(self, email):
        # insert into table and remove duplicates
        self.cur.execute("INSERT OR IGNORE INTO email(email) VALUES(?)", (email,))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM email WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    # The schema for the database is as follows:
    # id | email
    # 1  |
    # 2  |
    # and is created in the __init__ method

    #     async def initiate_newsletter(db):
    # print("running")
    # Mail = m.Mail
    # time = datetime.now(timezone.utc)
    # #convert time to local time
    # time = time.astimezone()
    # hour, minute = time.hour-4, time.minute
    # print(hour, minute)
    # # db = database.MyDatabase('emails.db')
    # #send the news letter every day at 8:00am
    # if hour == 12 and minute == 43:
    #         print("=================Newsletter test====================")
    # if time.hour == 8:
    #     #send the newsletter
    #     print("Sending newsletter")
    #     content = sendNewsletter.send_newsletter()
    #     emails = db.check()
    #     for email in emails:
    #         mail = Mail(email, content, html=True)
    #         mail.subscription_send_email()
    # return HttpResponse("Newsletter sent")
