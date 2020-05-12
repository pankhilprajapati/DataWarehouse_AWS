import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    '''
     Argumets:
       - cur = cursor 
       - conn = variable connecting to cluster
    Return:
       - NONE
    Description:
       This function get the cursor and connecting to curser to 
       Drop the tables
    '''
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    '''
        Argumets:
       - cur = cursor 
       - conn = variable connecting to cluster
    Return:
       - NONE
    Description:
       This function get the cursor and connecting to curser to 
       create the tables
    '''
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()