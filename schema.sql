-- drop table if exists users;
--     create table team (
--     id integer primary key autoincrement,
--     team_name text not null,
--     coach text not null,
-- );

-- insert into users (first_name, last_name, username, password) 
-- VALUES 
--     ('dummy-Andy', 'Wu', 'dummy-andywu', 'andywu'),
--     ('dummy-Allen', 'Chun', 'dummy-allenchun', 'allenchun'),
--     ('dummy-Annette', 'Lee', 'dummy-annettelee', 'annettelee'),
--     ('dummy-Kishan', 'Patel', 'dummy-kishanpatel', 'kishanpatel');

    create table players (
    player_id text primary key,
    pos text not null,
    player text not null,
    team text not null
);

    create table offense_players_weeks (
    player_id text not null,
    pass_cmp integer not null,
    pass_att integer not null,
    pass_yds integer not null,
    pass_td integer not null,
    pass_int integer not null,
    pass_sacked real not null,
    pass_sacked_yds integer not null,
    pass_long integer not null,
    pass_rating integer not null,
    rush_att integer not null,
    rush_yds integer not null,
    rush_td integer not null,
    rush_long integer not null,
    targets integer not null,
    rec integer not null,
    rec_yds integer not null,
    rec_td integer not null,
    rec_long integer not null,
    fumbles_lost integer not null,
    rush_scrambles integer not null,
    designed_rush_att integer not null,
    comb_pass_rush_play integer not null,
    comb_pass_play integer not null,
    comb_rush_play integer not null,
    -- Team_abbrev text not null,
    Opponent_abbrev text not null,
    two_point_conv integer not null,
    total_ret_td integer not null,
    offensive_fumble_recovery_td integer not null,
    pass_target_yds integer not null,
    pass_poor_throws integer not null,
    pass_blitzed integer not null,
    pass_hurried integer not null,
    rush_yds_before_contact integer not null,
    rush_yac integer not null,
    rush_broken_tackles integer not null,
    rec_air_yds integer not null,
    rec_yac integer not null,
    rec_drops integer not null,
    vis_team text not null,
    home_team text not null,
    week integer not null,

    FOREIGN KEY (player_id) references players(player_id)
);

    create table kickers (
    player text primary key,
    Off_abbrev text not null,
    photo image not null
);

    create table kickers_players_weeks (
    player text not null,
    Off_abbrev text not null,
    Def_abbrev text not null,
    fga integer not null,
    fgm integer not null,
    xpa integer not null,
    xpm integer not null,
    fga_0_39 integer not null,
    fgm_0_39 integer not null,
    fga_40_49 integer not null,
    fgm_40_49 integer not null,
    fga_50 integer not null,
    fgm_50 integer not null,
    vis_team text not null,
    home_team text not null,
    week integer not null,
    FOREIGN KEY (player) references kickers(player)
);