from nba_api.stats.endpoints import leaguegamelog

def fetch_games(season=str, season_type=str):

    logs = leaguegamelog.LeagueGameLog(
        season=season, 
        season_type_all_star=season_type, 
        player_or_team_abbreviation="T"
        ).get_data_frames()[0]

    games = logs[["GAME_ID", "GAME_DATE", "TEAM_ID", "TEAM_ABBREVIATION", "WL", "MATCHUP"]]

    return games