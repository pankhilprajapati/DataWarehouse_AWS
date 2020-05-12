import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    '''
    Argumets:
       - cur = cursor 
       - conn = variable connecting to cluster
    Return:
       - NONE
    Description:
       This function get the cursor and connecting to curser to 
       load the staging tables 
    '''
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    '''
    Argumets:
       - cur = cursor 
       - conn = variable connecting to cluster
    Return:
       - NONE
    Description:
       This function get the cursor and connecting to curser to 
       insert the values in to the tables
    '''
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()