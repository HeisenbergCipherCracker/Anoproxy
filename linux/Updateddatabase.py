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
        self.db_file = "test3.db"
    
    async def create_table_for_proxy_servers(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS proxy_servers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ip_address TEXT,
                        port INTEGER,
                        type TEXT
                        )''')
        conn.commit()
        conn.close()
        
    async def insert_some_value(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO proxy_servers (ip_address, port, type) VALUES ("89.207.132.170", 1080, "SOCKS5")''')
        conn.commit()
        conn.close()
        
    async def insert_value_by_user(self,userIP,userPORT,userTYPE):
        self.userIP = userIP
        self.userPORT = userPORT
        self.userTYPE = userTYPE
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        fet = cursor.fetchall()
        cursor.execute('''INSERT INTO proxy_servers (ip_address, port, type) VALUES (?, ?, ?)''', (userIP, userPORT, userTYPE))
        conn.commit()
        conn.close()
        
    async def display_the_info_of_proxy_servers_table(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM proxy_servers''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
        conn.commit()
        conn.close()
        
    async def create_table_for_saved_proxy_servers(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS saved_proxy_servers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ip_address TEXT,
                        port INTEGER,
                        type TEXT
                        )''')
        conn.commit()
        conn.close()
        
    async def insert_into_saved_proxy_servers(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO saved_proxy_servers (ip_address, port, type) VALUES ("89.207.132.170", 1080, "SOCKS5")''')
        conn.commit()
        conn.close()
        
    async def display_saved_proxy_servers(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM saved_proxy_servers''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
        conn.commit()
        conn.close()
        
    async def add_column_to_proxy_servers_table_for_fast_one(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''ALTER TABLE proxy_servers ADD COLUMN fast_proxy_server TEXT''')
        cursor.execute("UPDATE proxy_servers SET fast_proxy_server = 'Yes' WHERE id=23 ")
        conn.commit()
        conn.close()
        
    async def display_the_saved_proxy_servers(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM saved_proxy_servers''')
        rows = cursor.fetchall()
        for row in rows:
            # print(row) #* we will need that
            newls = list(row)
            print(newls)
            
        conn.commit()
        conn.close()
        
    async def delete_data_from_proxy_servers_table(self,usercmd):
        self.usercmd = usercmd
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM proxy_servers WHERE id=? ''',(int(self.usercmd),))
        conn.commit()
        conn.close()
    
    async def display_the_info_of_proxy_servers_table(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM proxy_servers''')
        rows = cursor.fetchall()
        for row in rows:
            # print(row) #* we will need that
            newls = list(row)
            print(newls)
            
        conn.commit()
        conn.close()
        
    async def display_proxy_servers_table(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM proxy_servers''')
        rows = cursor.fetchall()
        for row in rows:
            # print(row) #* we will need that
            newls = list(row)
            print(newls)
            
        conn.commit()
        conn.close()
    
    
    


        
database = Database()

        
        

async def main():
    # database = Database()
    global database
    database = Database()
    # await database.create_table_for_proxy_servers() #* we need that
    # await database.insert_some_value() #* we need that
    # await database.insert_value_by_user("89.207.132.170", 1080, "SOCKS5") #* can be enabled
    # await database.display_the_info_of_proxy_servers_table()
    # await database.create_table_for_saved_proxy_servers()
    # await database.insert_into_saved_proxy_servers()
    # await database.display_saved_proxy_servers() #* we need that 
    # await database.delete_data_from_proxy_servers_table(usercmd=6) #* ew need that
    # await database.display_saved_proxy_servers()
    # await database.display_the_info_of_proxy_servers_table() #* we need that
    await database.display_the_saved_proxy_servers()
    
    # await database.display_the_info_of_proxy_servers_table()
    # await database.add_column_to_proxy_servers_table_for_fast_one()
    # await database.create_table_for_main_proxy_servers()
    # await database.insert_into_saved_proxy_servers()
    # await database.delete_data_from_proxy_servers_table()
    # await database.insert_to_main_proxy_servers()
    # await database.display_main_proxy_servers()
    # await database.special_proxy_server_tables()
    # await database.special_main()
    
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
