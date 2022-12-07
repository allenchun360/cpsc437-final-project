import sqlite3
from contextlib import closing
from players import Player, Kicker
from get_weeks_models import get_weeks, get_kickers_weeks

DATABASE_URL = 'file:database.db?mode=ro'

def average_standard_score(player_id):
    weeks = get_weeks(player_id)
    sum = 0
    for week in weeks:
        sum += week.week_standard_score()
    return round(sum / 11, 2)

def kickers_average_standard_score(player):
    weeks = get_kickers_weeks(player)
    sum = 0
    for week in weeks:
        sum += week.week_standard_score()
    return round(sum / 11, 2)

def get_all_players():
    try:
        with sqlite3.connect(DATABASE_URL, isolation_level=None,
                                uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                query = "SELECT player_id, player, team, pos FROM players"
                cursor.execute(query)
                row = cursor.fetchone()
                # player_table = []
                qb = []
                rb =[]
                wr = []
                te = []

                while row is not None:
                    average_score = average_standard_score(str(row[0]))
                    player = Player(player_id=str(row[0]), player=str(row[1]), team=str(row[2]),
                                        pos=str(row[3]), average_standard_score=average_score)
                    if str(row[3]) == 'QB':
                        qb.append(player)
                    elif str(row[3]) == 'RB' or str(row[3]) == 'FB':
                        rb.append(player)
                    elif str(row[3]) == 'WR':
                        wr.append(player)
                    elif str(row[3]) == 'TE':
                        te.append(player)
                    # player_table.append(player)
                    row = cursor.fetchone()
                    # print(player.get_player_id())

                # print(player_table)
                qb = sorted(qb, key=lambda x: x.get_average_standard_score(), reverse=True)
                rb = sorted(rb, key=lambda x: x.get_average_standard_score(), reverse=True)
                wr = sorted(wr, key=lambda x: x.get_average_standard_score(), reverse=True)
                te = sorted(te, key=lambda x: x.get_average_standard_score(), reverse=True)
                return qb, rb, wr, te
                
    except sqlite3.OperationalError as ex:
        print(ex)
        exit(1)
    except sqlite3.DatabaseError:
        print("database error: could not be found or corrupted")
        exit(1)


def get_kickers():
    try:
        with sqlite3.connect(DATABASE_URL, isolation_level=None,
                                uri=True) as connection:
            with closing(connection.cursor()) as cursor:
                query = "SELECT player, Off_abbrev, photo FROM kickers"
                cursor.execute(query)
                row = cursor.fetchone()
                player_table = []

                while row is not None:
                    average_score = kickers_average_standard_score(str(row[0]))
                    player = Kicker(player=str(row[0]), Off_abbrev=str(row[1]), photo=row[2], average_standard_score=average_score)
                    player_table.append(player)
                    row = cursor.fetchone()
                    # print(player.get_player_id())
                
                player_table = sorted(player_table, key=lambda x: x.get_average_standard_score(), reverse=True)

                return player_table
                
    except sqlite3.OperationalError as ex:
        print(ex)
        exit(1)
    except sqlite3.DatabaseError:
        print("database error: could not be found or corrupted")
        exit(1)