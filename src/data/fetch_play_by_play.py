from nba_api.stats.endpoints import playbyplayv3
import time
import pandas as pd
from pathlib import Path
from json import JSONDecodeError

RAW_DIR = Path("../../data/raw/pbp")
RAW_DIR.mkdir(parents=True, exist_ok=True)

def save_raw_pbp(game_id: str):
    path = RAW_DIR / f"{game_id}.csv"

    if path.exists():
        return

    df = fetch_play_by_play(game_id)
    df.to_csv(path, index=False)

    # Evita rate limits / bloqueos.
    time.sleep(5)


def fetch_play_by_play(game_id: str, retries: int = 5):

    for attempt in range(1, retries + 1):
        try:
            pbp = playbyplayv3.PlayByPlayV3(game_id=game_id)  
            df = pbp.get_data_frames()[0]
            return df
        except JSONDecodeError as e:
            print(f"[WARN] JSON error for game {game_id}, attempt {attempt}/{retries}: {e}")
            time.sleep(5 * attempt)

        except Exception as e:
            print(f"[WARN] Failed game {game_id}, attempt {attempt}/{retries}: {e}")
            time.sleep(5 * attempt)

    print(f"[ERROR] Skipping game {game_id} after {retries} failed attempts")
    return pd.DataFrame()
            


     
    
    
