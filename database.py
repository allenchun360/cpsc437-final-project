import csv
import sqlite3
from contextlib import closing

DATABASE_URL = 'file:database.db'

with open('offense_players_cleaned.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    # print(reader[0])

    try:
        with sqlite3.connect(DATABASE_URL, isolation_level=None,
                                uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                count = 0
                for row in reader:
                    if count != 0:
                        query = "INSERT INTO players (player_id, player, pos, team, photo) VALUES (?, ?, ?, ?, ?)"
                        cursor.execute(query, [row[0], row[1], row[2], row[3], row[4]])
                    count += 1

    except sqlite3.OperationalError as ex:
        print(ex)
        exit(1)
    except sqlite3.DatabaseError:
        print("database error: could not be found or corrupted")
        exit(1)



with open('offense_cleaned.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    # print(reader[0])

    try:
        with sqlite3.connect(DATABASE_URL, isolation_level=None,
                                uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                count = 0
                for row in reader:
                    if count != 0:
                        query = "INSERT INTO offense_players_weeks (player_id, Team_abbrev, pass_cmp, pass_att, pass_yds, pass_td, pass_int, pass_sacked, pass_sacked_yds, pass_long, pass_rating, rush_att, rush_yds, rush_td, rush_long, targets, rec, rec_yds, rec_td, rec_long, fumbles_lost, rush_scrambles, designed_rush_att, comb_pass_rush_play, comb_pass_play, comb_rush_play, Opponent_abbrev, two_point_conv, total_ret_td, offensive_fumble_recovery_td, pass_target_yds, pass_poor_throws, pass_blitzed, pass_hurried, rush_yds_before_contact, rush_yac, rush_broken_tackles, rec_air_yds, rec_yac, rec_drops, vis_team, home_team, week) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                        cursor.execute(query, [row[0], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41], row[42], row[43], row[44]])
                    count += 1

    except sqlite3.OperationalError:
        print("table not found")
        exit(1)
    except sqlite3.DatabaseError:
        print("database error: could not be found or corrupted")
        exit(1)


with open('kicking_players_cleaned.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    # print(reader[0])

    try:
        with sqlite3.connect(DATABASE_URL, isolation_level=None,
                                uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                count = 0
                for row in reader:
                    if count != 0:
                        query = "INSERT INTO kickers (player, Off_abbrev, photo) VALUES (?, ?, ?)"
                        cursor.execute(query, [row[0], row[1], row[2]])
                    count += 1

    except sqlite3.OperationalError as ex:
        print(ex)
        exit(1)
    except sqlite3.DatabaseError:
        print("database error: could not be found or corrupted")
        exit(1)

with open('kicking_cleaned.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    # print(reader[0])

    try:
        with sqlite3.connect(DATABASE_URL, isolation_level=None,
                                uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                count = 0
                for row in reader:
                    if count != 0:
                        query = "INSERT INTO kickers_players_weeks ('Off_abbrev', 'Def_abbrev', 'fga', 'fgm', 'xpa', 'xpm', 'fga_0_39', 'fgm_0_39', 'fga_40_49', 'fgm_40_49', 'fga_50', 'fgm_50', 'player', 'vis_team', 'home_team', 'week') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
                        cursor.execute(query, [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]])
                    count += 1

    except sqlite3.OperationalError:
        print("table not found")
        exit(1)
    except sqlite3.DatabaseError:
        print("database error: could not be found or corrupted")
        exit(1)