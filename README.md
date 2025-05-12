📊 Project Overview

This project uses the Spotify Web API to extract recently played songs from my personal account. The data is then processed and loaded into a PostgreSQL database. Using SQL and Power BI, I built visual dashboards to answer questions like:
What artists do I listen to the most?
When am I most active on Spotify?
What genres do I favor?
How old is the music I listen to?

| Layer         | Tool/Library                 | Purpose                         |
| ------------- | ---------------------------- | ------------------------------- |
| ETL           | Python + Spotipy             | API data extraction             |
| Transform     | Pandas + SQLAlchemy          | Cleaning and processing         |
| Storage       | PostgreSQL                   | Structured relational database  |
| Analytics     | SQL                          | Querying and aggregations       |
| Dashboard     | Power BI Desktop             | Data visualization and insights |
| Orchestration | Python script (`run_all.py`) | Automates full pipeline         |

🚀 Features
✅ Spotify API integration via OAuth
✅ Normalized listening data (artist, genre, track, time)
✅ Track release year and song "age"
✅ Top genres, artists, and play frequency analytics
✅ Hourly and daily listening behavior breakdown
✅ Dashboard built in Power BI using exported and live data

🧱 Pipeline Architecture

Spotify API (Spotipy)
        ↓
   Python ETL Scripts
        ↓
 Cleaned DataFrames (Pandas)
        ↓
 PostgreSQL (listening_history table)
        ↓
SQL Queries / CSV Exports
        ↓
Power BI Dashboards

Automated via run_all.py

📸 Screenshots
🔝 Top Artists
⏰ Listening by Hour
🎶 Genre Distribution


🛠️ How to Run
Requirements:
Python 3.9+

PostgreSQL installed and running locally

Power BI Desktop

Spotify Developer Account

1. Clone the repo
```
git clone https://github.com/yourusername/spotify-trends.git
cd spotify-trends
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Set up your environment
Create a .env file with:

```
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
```
4. Run the full pipeline
```
python run_all.py
```
5. Open Power BI
Load listening_history.csv or connect to your local PostgreSQL

Use included visuals or build your own!

🎓 Lessons Learned
How to securely interact with the Spotify API using OAuth
Best practices for ETL pipeline organization and orchestration
Data modeling for music and time-series data
Creating reusable SQL queries for insights
Designing visual dashboards for storytelling

🔍 Sample data and screenshots are included.
![postgres_sample](https://github.com/user-attachments/assets/84e20752-009d-4d85-968a-02d7b50ce369)

![spotify_dashboard](https://github.com/user-attachments/assets/b8eacb8f-e284-44c4-ac07-0441e3db7d88)
