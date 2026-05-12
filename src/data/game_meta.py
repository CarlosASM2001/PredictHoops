def build_game_meta(game_rows, season, season_type):
    
    game_id = game_rows["GAME_ID"].iloc[0]

    winner = game_rows.loc[game_rows["WL"] == "W", "TEAM_ABBREVIATION"].iloc[0]
    
    home_team = None
    away_team = None

    for _, row in game_rows.iterrows():
        matchup = row["MATCHUP"]
        team = row["TEAM_ABBREVIATION"]

        if "vs." in matchup:
            home_team = team
        elif "@" in matchup:
            away_team = team
        
        return{
            "game_id": game_id,
            "season": season,
            "season_type": season_type,
            "home_team": home_team,
            "away_team": away_team,
            "winner_team": winner
        }