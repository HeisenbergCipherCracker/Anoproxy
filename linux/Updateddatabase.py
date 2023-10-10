import sqlite3
import asyncio
from extractdata import ipS, portS, typeS

class Singleton(type):
    _instances = None
    
    def __call__(self, *args, **kwargs):
        if self._instances is None:
            self._instances = super().__call__(*args, **kwargs)
        return self._instances

class Database(metaclass=Singleton):
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    async def data_base_updated_for_proxyservers_holding(self):
        global ipS, portS, typeS
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS proxyserver (ip TEXT, port TEXT, type TEXT)")
        values = [(ipS, portS, typeS)]
        cur.executemany("INSERT INTO proxyserver VALUES (?,?,?)", values)
        con.commit()
        con.close()
        
    async def Insert_new_values_into_data_base():
        global ipS, portS, typeS
        connection = sqlite3.connect("proxyservers.db")
        cur = connection.cursor()
        cur.execute("INSERT INTO proxyserver VALUES (?,?,?)",("145.239.85.58","9300","SOCKS5"))
        cur.execute("INSERT INTO proxyserver VALUES (?,?,?)",("145.239.85.58","9300","SOCKS5")) #!complete
        cur.execute("INSERT INTO proxyserver VALUES (?,?,?)",("145.239.85.58","9300","SOCKS5")) #!complete
        cur.execute("INSERT INTO proxyserver VALUES (?,?,?)",("145.239.85.58","9300","SOCKS5")) #! complete
        cur.execute("INSERT INTO proxyserver VALUES (?,?,?)",("145.239.85.58","9300","SOCKS5")) #!complete
        cur.execute("INSERT INTO proxyserver VALUES (?,?,?)",("145.239.85.58","9300","SOCKS5")) #!complete
        connection.commit()
        connection.close()
    #TODO: complete here
    
    async def display_data_base_info(self):
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM proxyserver")
        rows = cur.fetchall()
        print(rows)
        
    async def delete_data_from_the_data_base(self):
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("DELETE FROM proxyserver")
        con.commit()
        con.close()
        
    async def special_proxy_servers(self):
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("ALERT TABLE proxyserver ADD COLUMN specialproxy")
        con.commit()
        con.close()
        
    async def insert_special_proxy_into_data_base(self):
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("UPDATE proxyserver SET specialproxy = ? WHERE condition",("192.168.1.1","8080","http"))
        con.commit()
        con.close()
        
    async def create_saved_proxy_table(self):
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS savedproxy (ip TEXT, port TEXT, type TEXT)")
        con.commit()
        con.close()
        
    async def insert_saved_proxy_into_data_base(self):
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("INSERT INTO savedproxy VALUES (?,?,?)",("145.239.85.58","9300","SOCKS5"))
        con.commit()
        con.close()
        
    async def create_table_for_fast_proxy_servers(self):
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS fastproxy (ip TEXT, port TEXT, type TEXT)")
        con.commit()
        con.close()
        
    async def insert_to_fast_proxy_servers(self):
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("INSERT INTO fastproxy VALUES (?,?,?)",("145.239.85.58","9300","SOCKS5"))
        con.commit()
        con.close()
        
    async def display_fast_proxy_servers(self):
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM fastproxy")
        rows = cur.fetchall()
        print(rows)
        
    async def died_fast_proxy_servers(self):
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("DELETE FROM fastproxy")
        con.commit()
        con.close()
        
    async def suspended_fast_proxy_servers(self):
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("UPDATE fastproxy SET type = ? WHERE condition",("SOCKS5","http"))
        con.commit()
        con.close()
        
    async def column_for_stored_fast_proxy_servers(self):
        con = sqlite3.connect("proxyservers.db")
        cur = con.cursor()
        cur.execute("ALTER TABLE fastproxy ADD COLUMN type TEXT")
        con.commit()
        con.close()
    
    #? can use assert 

# asyncio.run(Database().data_base_updated_for_proxyservers_holding())