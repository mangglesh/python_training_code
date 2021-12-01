#The specification calls for the use of a connection object to manage the connection to the database 
# cursor objects to manage the interaction with the database, for fetching data from
# the database and updating its contents

# The other advantage is that it’s fairly easy to prototype an application using a lightweight database and then switch the application over
# to a production database after the basic design of the application has been finalized

import psycopg2 as pos_con
import sqlalchemy.pool as pool


pos_con = pool.manage(pos_con)



#add database connections
hostname = "localhost"
username = "postgres"
password_db = ""
database_db = "postgres"
db_port = "5432"

try:
    posgress_con = None
    posgress_con = pos_con.connect(host=hostname,user=username,password=password_db,database=database_db,port=db_port,connect_timeout = 60)
    cur = posgress_con.cursor()
    #un comment below line to fetch data from view

except Exception as error:
    print(error)
finally:
    if posgress_con is not None:
        try:
            posgress_con.close()
        except Exception:
            pass




cur.execute("select * from us_states")
print(cur.fetchall())

posgress_con.close()
