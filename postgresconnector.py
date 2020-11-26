import psycopg2
from config import config
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
# server = '10.0.0.69'
# database = 'synergy'
# username = 'synergy'
# password = 'Karthik@123'
# Port = '5432'
# schema= 'synergy'
# server = 'vm01-eus-synergydb.eastus.cloudapp.azure.com'
# database = 'synergydb'
# username = 'syndbadmin'
# password = 'Syn3rGyAppU53R#AzUr3'
# Port = '5443'
# schema= 'synergyapp'


try:
    params=config()

    #cnxn = psycopg2.connect('host='+server+' dbname='+database+' user='+username+' password='+ password+' port='+Port + 'schema='+schema)
    cnxn=psycopg2.connect(**params)
    cursor = cnxn.cursor()

except psycopg2.Error as ex:
    sqlstate = ex.args[0]
    print(sqlstate)

#print(cursor)
# conn = pyodbc.connect('DRIVER={FreeTDS};SERVER=server.domain.local;PORT=1433;UID=DOMAIN\user;PWD=mypassword;DATABASE=mydatabasename;UseNTLMv2=yes;TDS_Version=8.0;Trusted_Domain=domain.local;')
# cursor = conn.cursor()
#print(s_code)
#s_code="mytable"
# string = "CREATE TABLE  "+s_code+"(Name varchar(15), Age integer, City varchar(50))"
# cursor.execute(string)
# # cursor.execute("SELECT * FROM TestTable")
# # #cursor.execute('SELECT * FROM TestDB.dbo.Person')
# #
# cursor.execute('''
#                 INSERT INTO mytable (Name, Age, City)
#                 VALUES
#                 ('Bob',55,'Montreal'),
#                 ('Jenny',66,'Boston')
#                 ''')
# cnxn.commit()
#cursor.execute('SELECT * FROM mytable')

#rows = cursor.fetchall()
#for i in r:
