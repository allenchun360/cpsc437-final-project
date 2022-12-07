import sqlite3
from contextlib import closing
from weeks import Weeks, KickersWeeks

DATABASE_URL = 'file:database.db?mode=ro'

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
                                    pass_cmp=row[1],
                                    pass_att=row[2],
                                    pass_yds=row[3],
                                    pass_td=row[4],
                                    pass_int=row[5],
                                    pass_sacked=row[6],
                                    pass_sacked_yds=row[7],
                                    pass_long=row[8],
                                    pass_rating=row[9],
                                    rush_att=row[10],
                                    rush_yds=row[11],
                                    rush_td=row[12],
                                    rush_long=row[13],
                                    targets=row[14],
                                    rec=row[15],
                                    rec_yds=row[16],
                                    rec_td=row[17],
                                    rec_long=row[18],
                                    fumbles_lost=row[19],
                                    rush_scrambles=row[20],
                                    designed_rush_att=row[21],
                                    comb_pass_rush_play=row[22],
                                    comb_pass_play=row[23],
                                    comb_rush_play=row[24],
                                    # Team_abbrev=row[25],
                                    Opponent_abbrev=row[25],
                                    two_point_conv=row[26],
                                    total_ret_td=row[27],
                                    offensive_fumble_recovery_td=row[28],
                                    pass_target_yds=row[29],
                                    pass_poor_throws=row[30],
                                    pass_blitzed=row[31],
                                    pass_hurried=row[32],
                                    rush_yds_before_contact=row[33],
                                    rush_yac=row[34],
                                    rush_broken_tackles=row[35],
                                    rec_air_yds=row[36],
                                    rec_yac=row[37],
                                    rec_drops=row[38],
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


def get_kickers_weeks(player):
    try:
        with sqlite3.connect(DATABASE_URL, isolation_level=None,
                                uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                query = "SELECT Off_abbrev, Def_abbrev, fga, fgm, xpa, xpm, fga_0_39, fgm_0_39, fga_40_49, fgm_40_49, fga_50, fgm_50, player, vis_team, home_team, week FROM kickers_players_weeks WHERE player = ? ORDER BY week"
                cursor.execute(query, [player])
                row = cursor.fetchone()
                kickers_weeks_table = []
                # print(player_id)
                # print(row)

                while row is not None:
                    # print(row)
                    kickers_week = KickersWeeks(Off_abbrev=str(row[0]),
                                    Def_abbrev=str(row[1]),
                                    fga=row[2],
                                    fgm=row[3],
                                    xpa=row[4],
                                    xpm=row[5],
                                    fga_0_39=row[6],
                                    fgm_0_39=row[7],
                                    fga_40_49=row[8],
                                    fgm_40_49=row[9],
                                    fga_50=row[10],
                                    fgm_50=row[11],
                                    player=str(row[12]),
                                    vis_team=str(row[13]),
                                    home_team=str(row[14]),
                                    week=str(row[15]))
                    kickers_weeks_table.append(kickers_week)
                    row = cursor.fetchone()

                # print(kickers_weeks_table)

                return kickers_weeks_table
                
    except sqlite3.OperationalError as ex:
        print(ex)
        exit(1)
    except sqlite3.DatabaseError:
        print("database error: could not be found or corrupted")
        exit(1)