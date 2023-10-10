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
        pass
    #TODO: complete here
    
    #? can use assert 

# asyncio.run(Database().data_base_updated_for_proxyservers_holding())