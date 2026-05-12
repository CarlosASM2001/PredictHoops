import calculate_time as ct


def clean_pbp_state(pbp_df, game_meta):

    rows = []

    current_home_score = 0
    current_away_score = 0

    for _, event in pbp_df.iterrows():
        score = event.get("SCORE")

        if isinstance(score, str) and "-" in score:
            left, right = score.split("-")
            left = int(left.strip())
            right = int(right.strip())

            current_away_score = left
            current_home_score = right

        row = {
            "game_id": game_meta["game_id"],
            "season": game_meta["season"],
            "season_type": game_meta["season_type"],
            "event_num": event.get("EVENTNUM"),
            "period": event.get("PERIOD"),
            "clock": event.get("PCTIMESTRING"),
            "elapsed_seconds": ct.elapsed_seconds(
                event.get("PERIOD"),
                event.get("PCTIMESTRING")
            ),
            "home_team": game_meta["home_team"],
            "away_team": game_meta["away_team"],
            "home_score": current_home_score,
            "away_score": current_away_score,
            "score_diff_home": current_home_score - current_away_score,
            "event_type": event.get("EVENTMSGTYPE"),
            "description": (
                event.get("HOMEDESCRIPTION")
                or event.get("VISITORDESCRIPTION")
                or event.get("NEUTRALDESCRIPTION")
            ),
            "winner_team": game_meta["winner_team"],
            "home_win": int(game_meta["winner_team"] == game_meta["home_team"]),
        }

        rows.append(row)

    return rows