import psycopg2
class data:
    def __init__(self):
        self.con=psycopg2.connect("dbname='yokesh' user='postgres' password='yokesh3339' host='localhost' port='5432' ")
        self.cur=self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS vtg(id SERIAL,location varchar,weather varchar,time varchar,status BOOLEAN,PRIMARY KEY(id))")
        self.con.commit()
    

    def insert(self,location="",weather="",time="",status=""):
        self.cur.execute("INSERT INTO vtg(location,weather,time,status) VALUES(%s,%s,%s,%s)",(location,weather,time,status))
        self.con.commit()
        

    def update(self,id,location="",weather="",time="",status=""):
        self.cur.execute("UPDATE vtg SET location=%s,weather=%s,time=%s,status=%s where id=%s",(location,weather,time,status,id))
        self.con.commit()
    

    def delete(self,id):
        self.cur.execute("DELETE FROM vtg where id=%s",(id,))
        self.con.commit()
    

    def view(self):
        self.cur.execute("SELECT * FROM vtg ORDER BY id")
        rows=self.cur.fetchall()
        self.con.commit()
        return rows
    def search(self,location="",weather="",time=""):
        self.cur.execute("SELECT * FROM vtg where location=%s OR weather=%s OR time=%s",(location,weather,time))
        rows=self.cur.fetchall()
        self.con.commit()
        return rows
    
    def __del__(self):
        self.con.close()
    



