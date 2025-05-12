import subprocess
import logging
import sys
from datetime import datetime
import os

#logging
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/spotify_pipeline.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

#task runner
def run_script(script_path):
    logging.info(f"🔄 Running: {script_path}")
    try:
        subprocess.run(["python", script_path], check=True)
        logging.info(f"✅ Finished: {script_path}")
    except subprocess.CalledProcessError as e:
        logging.error(f"❌ Failed: {script_path} with error: {e}")
        sys.exit(1)

#pipeline steps
if __name__ == "__main__":
    logging.info("🚀 Spotify Listening Pipeline Started")

    run_script("scripts/spotify_data_scraper.py")
    run_script("scripts/load_to_postgres.py")
    run_script("scripts/listening_queries.py")

    logging.info("🎉 All pipeline steps completed successfully.")
