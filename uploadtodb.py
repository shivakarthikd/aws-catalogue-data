from postgresconnector import cursor,cnxn
#from test import ser_cat,s_code
schema='synergyapp'

def uploadtodb(ser_cat,s_code,diffkeys):
    coloumns=''
    for i in ser_cat.keys():
        coloumns=coloumns+' \"'+str(i)+'\" varchar(255),'
    #
    # coloumns=','.join(rds_cat.keys())
    # print(coloumns)
    # for i in rds_cat.values():
    #     values=values+' '+str(i)+','

    columns = ', '.join( "\""+str(x)+"\"".replace('/', '_') for x in ser_cat.keys())
    values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in ser_cat.values())
    #values=','.join(rds_cat.values())
    #print(values)
    coloumns=coloumns[0:len(coloumns)-1]

    #print(coloumns)
    # cursor.execute('drop table if exists '+ s_code)
    query=" create table if not exists "+schema+"."+s_code+"_table("+coloumns+")"
    print(query)
    cursor.execute(query)
    if diffkeys != {}:
        for col in diffkeys:
            alt_query='ALTER TABLE '+schema+"."+s_code+'_table ADD COLUMN IF NOT EXISTS \"'+str(col) +'\" varchar(255)'
            cursor.execute(alt_query)
    #insterquery='INSERT INTO '+s_code+'( Name ) VALUES('+ values+')'
    sql = 'INSERT INTO %s ( %s ) VALUES ( %s )' % (schema+"."+s_code+'_table', columns, values)
    #cursor.execute('''INSERT INTO '''+ s_code +'''()('''+ values +'')''')
    cursor.execute(sql)
    cnxn.commit()
    # cursor.execute('SELECT * FROM AWSDatabaseMigrationSvc_table')
    # rows = cursor.fetchall()
    # for i in rows:
    #     print(i)