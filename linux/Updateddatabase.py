import sqlite3
import asyncio



############################################################################333

datalistIP = []
datalistPORT = []
datalistTYPE = []

########################################################################################

class Singleton(type):
    """Create a singleton class for metaclass preparation """
    _instances = {} #* Create a insinstance null
    
    def __call__(cls, *args, **kwargs): #* using call to when we called the class
        #!only one instance allowed
        if cls not in cls._instances: #* see if there is an instance of class or not 
            instance = super().__call__(*args, **kwargs) #* if it is not the instance it use the super method to give it attributes
            cls._instances[cls] = instance 
        return cls._instances[cls] #* returns the value

###########################################################################################################################################

class Database(metaclass=Singleton):
    """A class for database methods that is metaclass """
    
    def __init__(self):
        """Connects to the database file  """
        self.db_file = "test3.db"
        
        
####################################################################################################################################################################################################################3
    
    async def create_table_for_proxy_servers(self):
        """That will create a table for proxyservers if it is not exists """
        conn = sqlite3.connect(self.db_file) #* make connection
        cursor = conn.cursor() #* compose cursor
        cursor.execute('''CREATE TABLE IF NOT EXISTS proxy_servers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ip_address TEXT,
                        port INTEGER,
                        type TEXT
                        )''') #* table creation command
        conn.commit() #* commit and sace the changes
        conn.close() #* close the connection when we were done
        
#############################################################################################################################################################################################################        
        
    async def insert_some_value(self):
        """I inserted some initial values into the database here """
        conn = sqlite3.connect(self.db_file) #* make connection 
        cursor = conn.cursor() #* create cursor
        cursor.execute('''INSERT INTO proxy_servers (ip_address, port, type) VALUES ("89.207.132.170", 1080, "SOCKS5")''') #* insert some values
        conn.commit() #* commit and save the changes
        conn.close() #* close the connection
        
###########################################################################################################################################################################################3        
        
    async def insert_value_by_user(self,userIP,userPORT,userTYPE):
        """This is for when we want the user to insert some values to its database """
        self.userIP = userIP #* create some values
        self.userPORT = userPORT
        self.userTYPE = userTYPE
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor() #* create connection and cursor
        fet = cursor.fetchall()
        cursor.execute('''INSERT INTO proxy_servers (ip_address, port, type) VALUES (?, ?, ?)''', (userIP, userPORT, userTYPE)) #* insert the user values to the database
        conn.commit() #* commit and save the changes
        conn.close() #* close the connection
        
########################################################################################################################################################################################################        
        
    async def display_the_info_of_proxy_servers_table(self):
        """We will display the proxy database info from here when the user wants to make a choice """
        conn = sqlite3.connect(self.db_file) #* create connection
        cursor = conn.cursor() #* create cursor
        cursor.execute('''SELECT * FROM proxy_servers''') #* select all the columns and values from the proxy servers table
        rows = cursor.fetchall() #* create fetch all 
        for row in rows: #* print the rows
            rowlist = list(row) #* create a list for rows
            print(row)
            
        conn.commit() #* commit the changes 
        conn.close() #* close the connection
        
################################################################################################################################################################################################        
    async def create_table_for_saved_proxy_servers(self):
        """This will create a table for when we want to store and save some proxies for sometime """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS saved_proxy_servers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ip_address TEXT,
                        port INTEGER,
                        type TEXT
                        )''') #* creating the saved proxy tables
        conn.commit()
        conn.close() #* close and commit
   
#############################################################################################################################################################        
    async def insert_into_saved_proxy_servers(self):
        """I inserted some values to the database """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO saved_proxy_servers (ip_address, port, type) VALUES ("89.207.132.170", 1080, "SOCKS5")''')
        conn.commit()
        conn.close()
        
############################################################################################################################################3        
        
    async def display_saved_proxy_servers(self):
        """This will display the saved proxy servers into the database """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM saved_proxy_servers''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
        conn.commit()
        conn.close()

#############################################################################################################################        
        
    async def add_column_to_proxy_servers_table_for_fast_one(self):
        """Adding a column for see if the proxy is fast or not """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''ALTER TABLE proxy_servers ADD COLUMN fast_proxy_server TEXT''')
        cursor.execute("UPDATE proxy_servers SET fast_proxy_server = 'Yes' WHERE id=23 ")
        conn.commit()
        conn.close()

##################################################################################################################        
        
    async def display_the_saved_proxy_servers(self):
        """ Display the saved proxy servers """
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

########################################################################################################################
        
    async def delete_data_from_proxy_servers_table(self,usercmd):
        """User can delete its desired data """
        self.usercmd = usercmd
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM proxy_servers WHERE id=? ''',(int(self.usercmd),))
        conn.commit()
        conn.close()
    
####################################################################################################################################    
    async def display_the_info_of_proxy_servers_table(self):
        """Display the proxyservers table """
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


##################################################################################################################################        
    async def display_proxy_servers_table(self):
        """Display the proxyservers table """
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM proxy_servers''')
        rows = cursor.fetchall()
        for row in rows:
            # print(row) #* we will need that
            newls = list(row)
            print(newls)
            for _ in newls:
                global datalistIP,datalistPORT,datalistTYPE
                info = (f"Ip address of proxyserver:{newls[1]}\n Port:{newls[2]}\ntype:{newls[3]}")
                print(info)
                ip = newls[1]
                port = newls[2]
                Type = newls[3]
                datalistIP.append(ip)
                datalistPORT.append(port)
                datalistTYPE.append(Type)
            
            print(datalistIP)
            print(datalistPORT)
            print(datalistTYPE)
            
            
        conn.commit()
        conn.close()
    
##########################################################################################################################    
    


        
database = Database()

# print(datalistIP)
        
        

async def main():
    # database = Database()
    global database
    database = Database()
    # insert_proxies_to_config(datalistIP,datalistPORT,datalistTYPE)
    # await database.display_proxy_servers_table()
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
    # await database.display_the_saved_proxy_servers()
    
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
