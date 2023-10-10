import sqlite3
import asyncio

class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=Singleton):
    
    def __init__(self):
        self.db_file = "proxyservers.db"
    
    async def data_base_updated_for_proxyservers_holding(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS proxyserver (ip TEXT, port TEXT, type TEXT, col4 TEXT)")
        values = [("ip1", "port1", "type1", "4", "col5"), ("ip2", "port2", "type2", "t", "col5")]
        cur.executemany("INSERT INTO proxyserver VALUES (?,?,?,?,?)", values)

        con.commit()
        con.close()
        
    async def Insert_new_values_into_data_base(self):
        connection = sqlite3.connect(self.db_file)
        cur = connection.cursor()
        values = [("ip1", "port1", "type1", "4", "col5"), ("ip2", "port2", "type2", "t", "col5")]
        cur.executemany("INSERT INTO proxyserver VALUES (?,?,?,?,?)", values)

        connection.commit()
        connection.close()

    async def display_data_base_info(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("SELECT * FROM proxyserver")
        rows = cur.fetchall()
        print(rows)
        con.close()
        
    async def delete_data_from_the_data_base(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("DELETE FROM proxyserver")
        con.commit()
        con.close()
        
    async def special_proxy_servers(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("ALTER TABLE proxyserver ADD COLUMN special TEXT")
        con.commit()
        con.close()
        
    async def insert_special_proxy_into_data_base(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("UPDATE proxyserver SET specialproxy = ? WHERE ip = ?", ("192.168.1.1", "145.239.85.58"))
        con.commit()
        con.close()
        
    async def create_saved_proxy_table(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS savedproxy (ip TEXT, port TEXT, type TEXT)")
        con.commit()
        con.close()
        
    async def insert_saved_proxy_into_data_base(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("INSERT INTO savedproxy VALUES (?,?,?)",("145.239.85.58","9300","SOCKS5"))
        con.commit()
        con.close()
        
    async def create_table_for_fast_proxy_servers(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS fastproxy (ip TEXT, port TEXT, type TEXT)")
        con.commit()
        con.close()
        
    async def insert_to_fast_proxy_servers(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("INSERT INTO fastproxy VALUES (?,?,?)",("145.239.85.58","9300","SOCKS5"))
        con.commit()
        con.close()
        
    async def display_fast_proxy_servers(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("SELECT * FROM fastproxy")
        rows = cur.fetchall()
        print(rows)
        con.close()
        
    async def died_fast_proxy_servers(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("DELETE FROM fastproxy")
        con.commit()
        con.close()
        
    async def suspended_fast_proxy_servers(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("UPDATE fastproxy SET type = ? WHERE ip = ?", ("SOCKS5", "145.239.85.58"))
        con.commit()
        con.close()
        
    async def column_for_stored_fast_proxy_servers(self):
        con = sqlite3.connect(self.db_file)
        cur = con.cursor()
        cur.execute("ALTER TABLE fastproxy ADD COLUMN types TEXT")
        con.commit()
        con.close()

async def main():
    database = Database()
    # await database.data_base_updated_for_proxyservers_holding()
    # await database.Insert_new_values_into_data_base()
    # await database.display_data_base_info()
    # await database.delete_data_from_the_data_base()
    # await database.special_proxy_servers()
    # await database.insert_special_proxy_into_data_base()
    # await database.create_saved_proxy_table()
    # await database.insert_saved_proxy_into_data_base()
    # await database.create_table_for_fast_proxy_servers()
    # await database.insert_to_fast_proxy_servers()
    # await database.display_fast_proxy_servers()
    # await database.died_fast_proxy_servers()
    # await database.suspended_fast_proxy_servers()
    # await database.column_for_stored_fast_proxy_servers()

if __name__ == "__main__":
    asyncio.run(main())
