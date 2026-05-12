import pandas as pd
from pathlib import Path
import fetch_games as games
import game_meta as gm
import fetch_play_by_play as pbp
import clean_pbp_state as clean_pbp
import time

PROCESSED_DIR = Path("../../data/processed")
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def main():
    all_state_rows = []

    seasons = ["2022-23"]
    season_types = ["Regular Season", "Playoffs"]

    for season in seasons:
        for season_type in season_types:
            games_df = games.fetch_games(season, season_type)

            for game_id, game_rows in games_df.groupby("GAME_ID"):
                print(f"Processing {season} {season_type} {game_id}")

                game_meta = gm.build_game_meta(game_rows, season, season_type)

                raw_path = pbp.RAW_DIR / f"{game_id}.csv"

                if raw_path.exists():
                    pbp_df = pd.read_csv(raw_path)
                else:
                    pbp_df = pbp.fetch_play_by_play(game_id)
                    pbp_df.to_csv(raw_path, index=False)
                    time.sleep(3)

                state_rows = clean_pbp.clean_pbp_state(pbp_df, game_meta)
                all_state_rows.extend(state_rows)

    final_df = pd.DataFrame(all_state_rows)

    final_df = final_df.sort_values(
        ["season", "game_id", "elapsed_seconds", "event_num"]
    )

    final_df.to_csv(PROCESSED_DIR / "game_states.csv", index=False)

if __name__ == "__main__":
    main()