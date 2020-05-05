# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                                        songplay_id SERIAL PRIMARY KEY, 
                                        start_time timestamp NOT NULL, 
                                        user_id INT , 
                                        level varchar, 
                                        song_id varchar , 
                                        artist_id varchar, 
                                        session_id INT, 
                                        location varchar, 
                                        user_agent varchar); """)

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                                       user_id int PRIMARY KEY, 
                                       first_name varchar, 
                                       last_name varchar, 
                                       gender varchar, 
                                       level varchar); """)

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(
                                        song_id varchar PRIMARY KEY, 
                                        title varchar, 
                                        artist_id varchar, 
                                        year INT, 
                                        duration float8); """)

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(
                                        artist_id varchar, 
                                        name varchar, 
                                        location varchar, 
                                        latitude FLOAT8, 
                                        longitude FLOAT8); """)

time_table_create = ("""CREATE TABLE IF NOT EXISTS time(
                                        start_time timestamp, 
                                        hour INT NOT NULL, 
                                        day INT NOT NULL, 
                                        week INT NOT NULL, 
                                        month TEXT NOT NULL, 
                                        year INT NOT NULL, 
                                        weekday int NOT NULL); """)

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays ( 
                                        start_time, 
                                        user_id, 
                                        level, 
                                        song_id, 
                                        artist_id, 
                                        session_id, 
                                        location, 
                                        user_agent) 
                                    VALUES (%s, %s, %s, %s, %s,%s, %s, %s); 
                                """)

user_table_insert = ("""INSERT INTO users (
                                       user_id,
                                       first_name, 
                                       last_name, 
                                       gender, 
                                       level) 
                                    VALUES (%s, %s, %s, %s, %s) 
                                    ON CONFLICT(user_id) DO UPDATE
                                        SET first_name = excluded.first_name,
                                            last_name = excluded.last_name,
                                            gender = excluded.gender,
                                            level = excluded.level;
                                        """)

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration)
                                VALUES (%s, %s, %s, %s, %s);
                                """)

artist_table_insert = ("""INSERT INTO artists (
                                       artist_id, 
                                        name , 
                                        location, 
                                        latitude, 
                                        longitude) 
                                    VALUES (%s, %s, %s, %s, %s) 
                                    """)


time_table_insert = ("""INSERT INTO time (
                                        start_time, 
                                        hour, 
                                        day, 
                                        week, 
                                        month, 
                                        year, 
                                        weekday) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s) 

                                """)

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id
                  FROM artists a 
                  JOIN songs s
                  ON a.artist_id = s.artist_id
                  WHERE s.title = %s  AND a.name = %s AND s.duration = %s ;
                  """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]