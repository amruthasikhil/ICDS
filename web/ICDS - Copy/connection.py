import pymysql
from flask import jsonify

class Db:
    def __init__(self):
        self.insert = None
        self.con = pymysql.connect(host="localhost", user="root", password="", db="icds", port=3306)
        self.cu = self.con.cursor()


    def nonreturn(self,a):
        self.cu.execute(a)
        id=self.cu.lastrowid
        self.con.commit()
        return id


    def selectone(self,a):
        self.cu.execute(a)
        self.res = self.cu.fetchone()
        return (self.res)

    def selectall(self,a):
        self.cu.execute(a)
        self.res=self.cu.fetchall()
        return(self.res)


    def mid(self,a):
        self.cu.execute(a)
        f=self.cu.fetchone()
        if f[0] is None:
            id=1
        else:
            id=f[0] + 1
        return (id)
    def jsonsel(self,a):
        self.cu.execute(a)
        self.res = self.cu.fetchall()
        row_headers = [x[0] for x in self.cu.description]
        json_data = []
        for result in self.res:
            json_data.append(dict(zip(row_headers, result)));
            # print(self.res, json_data)
        return json_data
