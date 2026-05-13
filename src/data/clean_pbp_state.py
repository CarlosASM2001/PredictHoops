import pandas as pd

import calculate_time as ct


def _clean_score(value, current_score):
    if pd.isna(value) or value == "":
        return current_score
    return int(float(value))


def _clean_text(value):
    if pd.isna(value):
        return ""
    return str(value)


def clean_pbp_state(pbp_df, game_meta):
    rows = []
    current_home_score = 0
    current_away_score = 0

    for _, event in pbp_df.iterrows():
        current_home_score = _clean_score(event.get("scoreHome"), current_home_score)
        current_away_score = _clean_score(event.get("scoreAway"), current_away_score)

        row = {
            "game_id": game_meta["game_id"],
            "season": game_meta["season"],
            "season_type": game_meta["season_type"],
            "event_num": event.get("actionNumber"),
            "period": event.get("period"),
            "clock": event.get("clock"),
            "elapsed_seconds": ct.elapsed_seconds(
                event.get("period"),
                event.get("clock"),
            ),
            "home_team": game_meta["home_team"],
            "away_team": game_meta["away_team"],
            "home_score": current_home_score,
            "away_score": current_away_score,
            "score_diff_home": current_home_score - current_away_score,
            "event_type": event.get("actionType"),
            "description": _clean_text(event.get("description")),
            "winner_team": game_meta["winner_team"],
            "home_win": int(game_meta["winner_team"] == game_meta["home_team"]),
        }

        rows.append(row)

    return rows