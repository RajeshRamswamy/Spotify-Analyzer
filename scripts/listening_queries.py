import pandas as pd
from db_connection import get_engine
from sqlalchemy import text

engine = get_engine()

#query for top artists
top_artist_query = """
    SELECT artist_name, COUNT(*) AS play_count
    FROM listening_history
    GROUP BY artist_name
    ORDER BY play_count DESC
    LIMIT 10;
"""
top_artist_df = pd.DataFrame(engine.connect().execute(text(top_artist_query)))

#query for top genres
genre_query = """
    SELECT
    TRIM(genre) AS genre,
    COUNT(*) AS play_count
    FROM (
    SELECT UNNEST(string_to_array(genres, ',')) AS genre
    FROM listening_history
    WHERE genres IS NOT NULL AND genres != ''
    ) AS genre_list
    GROUP BY genre
    ORDER BY play_count DESC
    LIMIT 10;
"""
genre_df = pd.DataFrame(engine.connect().execute(text(genre_query)))

#queries for newest song by release date
newest_songs_query = """
    SELECT track_name, artist_name, MIN(played_at) AS first_play, album, release_date
    FROM listening_history
    GROUP BY track_name, artist_name, album, release_date
    ORDER BY release_date DESC
    LIMIT 10;
"""
newest_songs_df = pd.DataFrame(engine.connect().execute(text(newest_songs_query)))

#save queried data
top_artist_df.to_csv("queried_data/top_artists.csv", index=False)
genre_df.to_csv("queried_data/genre.csv", index=False)
newest_songs_df.to_csv("queried_data/newest_songs.csv", index=False)