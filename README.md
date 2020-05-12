# Project: Data Warehouse

Building an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables.
Database is hosted on Redshift and data is load from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.

# Instruction 

### Schema for Song Play Analysis
#### Fact Table
 - songplays - records in event data associated      with song plays i.e. records with page NextSong
  songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

#### Dimension Tables
 - users - users in the app user_id, first_name,    last_name, gender, level
 - songs - songs in music database song_id, title, artist_id, year, duration
 - artists - artists in music database artist_id, name, location, lattitude, longitude
 - time - timestamps of records in songplays broken down into specific units start_time, hour, day, week, month, year, weekday

# Files
 - create_table.py is where fact and dimension tables for the star schema in Redshift is created.

 - etl.py is where data is load from S3 into staging tables on Redshift and then process that data into analytics tables on Redshift.

 - sql_queries.py is where  SQL statements, which will be imported into the two other files above.
 
 - .cfg is where all the key,host , port and db_name , user_name other configuration info which can be access

 - setup_test.ipynb is the file where the redshift cluster is created with IAM role that is further use to write SQL queries in the above two file. and the both files are test inside this. After that deletion of the cluster

 # Ackowledgement 
  - Udacity
  - AWS