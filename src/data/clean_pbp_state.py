import pandas as pd

import calculate_time as ct


def _clean_score(value, current_score):
    if pd.isna(value) or value == "":
        return current_score
    return int(float(value))



def get_event_type(event):
    action_type = event.get("actionType")

    if pd.notna(action_type) and str(action_type).strip():
        return str(action_type)

    description = get_event_description(event).lower()

    if "steal" in description:
        return "Steal"
    if "block" in description:
        return "Block"
    return None


def get_event_description(event):

    description = event.get("description")

    if pd.notna(description) and str(description).strip():
        return description

    action_type = event.get("actionType")
    sub_type = event.get("subType")
    player = event.get("playerName")

    parts = [
        str(player) if pd.notna(player) else None,
        str(action_type) if pd.notna(action_type) else None,
        str(sub_type) if pd.notna(sub_type) else None,
    ]

    return " ".join([p for p in parts if p])

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
            "event_type": get_event_type(event),
            "description": get_event_description(event),
            "winner_team": game_meta["winner_team"],
            "home_win": int(game_meta["winner_team"] == game_meta["home_team"]),
        }

        rows.append(row)

    return rows