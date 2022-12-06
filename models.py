import sqlite3
from contextlib import closing
from players import Player, Weeks

DATABASE_URL = 'file:database.db?mode=ro'

def get_all_players():
    try:
        with sqlite3.connect(DATABASE_URL, isolation_level=None,
                                uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                query = "SELECT player_id, player, team, pos FROM players"
                cursor.execute(query)
                row = cursor.fetchone()
                player_table = []

                while row is not None:
                    player = Player(player_id=str(row[0]), player=str(row[1]), team=str(row[2]),
                                    pos=str(row[3]))
                    player_table.append(player)
                    row = cursor.fetchone()
                    # print(player.get_player_id())

                return player_table
                
    except sqlite3.OperationalError as ex:
        print(ex)
        exit(1)
    except sqlite3.DatabaseError:
        print("database error: could not be found or corrupted")
        exit(1)

def get_weeks(player_id):
    try:
        with sqlite3.connect(DATABASE_URL, isolation_level=None,
                                uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                query = "SELECT player_id, pass_cmp, pass_att, pass_yds, pass_td, pass_int, pass_sacked, pass_sacked_yds, pass_long, pass_rating, rush_att, rush_yds, rush_td, rush_long, targets, rec, rec_yds, rec_td, rec_long, fumbles_lost, rush_scrambles, designed_rush_att, comb_pass_rush_play, comb_pass_play, comb_rush_play, Opponent_abbrev, two_point_conv, total_ret_td, offensive_fumble_recovery_td, pass_target_yds, pass_poor_throws, pass_blitzed, pass_hurried, rush_yds_before_contact, rush_yac, rush_broken_tackles, rec_air_yds, rec_yac, rec_drops, vis_team, home_team, week FROM offense_players_weeks WHERE player_id = ? ORDER BY week"
                cursor.execute(query, [player_id])
                row = cursor.fetchone()
                weeks_table = []
                # print(player_id)

                while row is not None:
                    week = Weeks(player_id=str(row[0]),
                                    pass_cmp=str(row[1]),
                                    pass_att=str(row[2]),
                                    pass_yds=str(row[3]),
                                    pass_td=str(row[4]),
                                    pass_int=str(row[5]),
                                    pass_sacked=str(row[6]),
                                    pass_sacked_yds=str(row[7]),
                                    pass_long=str(row[8]),
                                    pass_rating=str(row[9]),
                                    rush_att=str(row[10]),
                                    rush_yds=str(row[11]),
                                    rush_td=str(row[12]),
                                    rush_long=str(row[13]),
                                    targets=str(row[14]),
                                    rec=str(row[15]),
                                    rec_yds=str(row[16]),
                                    rec_td=str(row[17]),
                                    rec_long=str(row[18]),
                                    fumbles_lost=str(row[19]),
                                    rush_scrambles=str(row[20]),
                                    designed_rush_att=str(row[21]),
                                    comb_pass_rush_play=str(row[22]),
                                    comb_pass_play=str(row[23]),
                                    comb_rush_play=str(row[24]),
                                    # Team_abbrev=str(row[25]),
                                    Opponent_abbrev=str(row[25]),
                                    two_point_conv=str(row[26]),
                                    total_ret_td=str(row[27]),
                                    offensive_fumble_recovery_td=str(row[28]),
                                    pass_target_yds=str(row[29]),
                                    pass_poor_throws=str(row[30]),
                                    pass_blitzed=str(row[31]),
                                    pass_hurried=str(row[32]),
                                    rush_yds_before_contact=str(row[33]),
                                    rush_yac=str(row[34]),
                                    rush_broken_tackles=str(row[35]),
                                    rec_air_yds=str(row[36]),
                                    rec_yac=str(row[37]),
                                    rec_drops=str(row[38]),
                                    vis_team=str(row[39]),
                                    home_team=str(row[40]),
                                    week=str(row[41]))
                    weeks_table.append(week)
                    row = cursor.fetchone()

                # print(weeks_table)

                return weeks_table
                
    except sqlite3.OperationalError as ex:
        print(ex)
        exit(1)
    except sqlite3.DatabaseError:
        print("database error: could not be found or corrupted")
        exit(1)