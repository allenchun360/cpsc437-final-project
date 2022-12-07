class Weeks:
    """players class"""

    def __init__(self,
                player_id,
                pass_cmp,
                pass_att,
                pass_yds,
                pass_td,
                pass_int,
                pass_sacked,
                pass_sacked_yds,
                pass_long,
                pass_rating,
                rush_att,
                rush_yds,
                rush_td,
                rush_long,
                targets,
                rec,
                rec_yds,
                rec_td,
                rec_long,
                fumbles_lost,
                rush_scrambles,
                designed_rush_att,
                comb_pass_rush_play,
                comb_pass_play,
                comb_rush_play,
                Opponent_abbrev,
                two_point_conv,
                total_ret_td,
                offensive_fumble_recovery_td,
                pass_target_yds,
                pass_poor_throws,
                pass_blitzed,
                pass_hurried,
                rush_yds_before_contact,
                rush_yac,
                rush_broken_tackles,
                rec_air_yds,
                rec_yac,
                rec_drops,
                vis_team,
                home_team,
                week):
        self._player_id = player_id
        self._pass_cmp = pass_cmp
        self._pass_att = pass_att
        self._pass_yds = pass_yds
        self._pass_td = pass_td
        self._pass_int = pass_int
        self._pass_sacked = pass_sacked
        self._pass_sacked_yds = pass_sacked_yds
        self._pass_long = pass_long
        self._pass_rating = pass_rating
        self._rush_att = rush_att
        self._rush_yds = rush_yds
        self._rush_td = rush_td
        self._rush_long = rush_long
        self._targets = targets
        self._rec = rec
        self._rec_yds = rec_yds
        self._rec_td = rec_td
        self._rec_long = rec_long
        self._fumbles_lost = fumbles_lost
        self._rush_scrambles = rush_scrambles
        self._designed_rush_att = designed_rush_att
        self._comb_pass_rush_play = comb_pass_rush_play
        self._comb_pass_play = comb_pass_play
        self._comb_rush_play = comb_rush_play
        self._Opponent_abbrev = Opponent_abbrev
        self._two_point_conv = two_point_conv
        self._total_ret_td = total_ret_td
        self._offensive_fumble_recovery_td = offensive_fumble_recovery_td
        self._pass_target_yds = pass_target_yds
        self._pass_poor_throws = pass_poor_throws
        self._pass_blitzed = pass_blitzed
        self._pass_hurried = pass_hurried
        self._rush_yds_before_contact = rush_yds_before_contact
        self._rush_yac = rush_yac
        self._rush_broken_tackles = rush_broken_tackles
        self._rec_air_yds = rec_air_yds
        self._rec_yac = rec_yac
        self._rec_drops = rec_drops
        self._vis_team = vis_team
        self._home_team = home_team
        self._week = week

    def get_player_id(self):
        """get player id"""
        return self._player_id

    def get_pass_cmp(self):
        return self._pass_cmp
 
    def get_pass_att(self):
        return self._pass_att

    def get_pass_yds(self): 
        return self._pass_yds

    def get_pass_td(self): 
        return self._pass_td

    def get_pass_int(self): 
        return self._pass_int 

    def get_pass_sacked(self):
        return self._pass_sacked 

    def get_pass_sacked_yds(self):
        return self._pass_sacked_yds 

    def get_pass_long(self):
        return self._pass_long 

    def get_pass_rating(self):
        return self._pass_rating 

    def get_rush_att(self):
        return self._rush_att 

    def get_rush_yds(self):
        return self._rush_yds 

    def get_rush_td(self):
        return self._rush_td 

    def get_rush_long(self):
        return self._rush_long

    def get_targets(self):
        return self._targets

    def get_rec(self):
        return self._rec

    def get_rec_yds(self):
        return self._rec_yds

    def get_rec_td(self):
        return self._rec_td

    def get_rec_long(self):
        return self._rec_long

    def get_fumbles_lost(self):
        return self._fumbles_lost

    def get_rush_scrambles(self):
        return self._rush_scrambles

    def get_designed_rush_att(self):
        return self._designed_rush_att

    def get_comb_pass_rush_play(self):
        return self._comb_pass_rush_play

    def get_comb_pass_play(self):
        return self._comb_pass_play

    def get_comb_rush_play(self):
        return self._comb_rush_play

    def get_Opponent_abbrev(self):
        return self._Opponent_abbrev

    def get_two_point_conv(self):
        return self._two_point_conv

    def get_total_ret_td(self):
        return self._total_ret_td

    def get_offensive_fumble_recovery_td(self):
        return self._offensive_fumble_recovery_td

    def get_pass_target_yds(self):
        return self._pass_target_yds

    def get_pass_poor_throws(self):
        return self._pass_poor_throws

    def get_pass_blitzed(self):
        return self._pass_blitzed

    def get_pass_hurried(self):
        return self._pass_hurried

    def get_rush_yds_before_contact(self):
        return self._rush_yds_before_contact

    def get_rush_yac(self):
        return self._rush_yac 

    def get_rush_broken_tackles(self):
        return self._rush_broken_tackles

    def get_rec_air_yds(self):
        return self._rec_air_yds

    def get_rec_yac(self):
        return self._rec_yac

    def get_rec_drops(self):
        return self._rec_drops

    def get_vis_team(self):
        return self._vis_team

    def get_home_team(self):
        return self._home_team

    def get_week(self):
        return self._week

    def week_standard_score(self):
        return round(self.get_pass_yds()/25 + self.get_rush_yds()/10 + self.get_rec_yds()/10 + 6*self.get_rec_td() + 6 * self.get_rush_td() + 4 * self.get_pass_td() - 2 * self.get_pass_int() - self.get_fumbles_lost() + 2 * self.get_two_point_conv(), 2)

class KickersWeeks:
    """players class"""

    def __init__(self,
                 Off_abbrev,
                 Def_abbrev,
                 fga,
                 fgm,
                 xpa,
                 xpm,
                 fga_0_39,
                 fgm_0_39,
                 fga_40_49,
                 fgm_40_49,
                 fga_50,
                 fgm_50,
                 player,
                 vis_team,
                 home_team,
                 week):
        self._Off_abbrev = Off_abbrev
        self._Def_abbrev = Def_abbrev
        self._fga = fga
        self._fgm = fgm
        self._xpa = xpa
        self._xpm = xpm
        self._fga_0_39 = fga_0_39
        self._fgm_0_39 = fgm_0_39
        self._fga_40_49 = fga_40_49
        self._fgm_40_49 = fgm_40_49
        self._fga_50 = fga_50
        self._fgm_50 = fgm_50
        self._player = player
        self._vis_team = vis_team
        self._home_team = home_team
        self._week = week

    def get_Off_abbrev(self):
        return self._Off_abbrev

    def get_Def_abbrev(self):
        return self._Def_abbrev

    def get_fga(self):
        return self._fga

    def get_fgm(self):
        return self._fgm

    def get_xpa(self):
        return self._xpa

    def get_xpm(self):
        return self._xpm

    def get_fga_0_39(self):
        return self._fga_0_39

    def get_fgm_0_39(self):
        return self._fgm_0_39

    def get_fga_40_49(self):
        return self._fga_40_49

    def get_fgm_40_49(self):
        return self._fgm_40_49

    def get_fga_50(self):
        return self._fga_50

    def get_fgm_50(self):
        return self._fgm_50

    def get_player(self):
        return self._player

    def get_vis_team(self):
        return self._vis_team

    def get_home_team(self):
        return self._home_team

    def get_week(self):
        return self._week

    def week_standard_score(self):
        return 5 * self.get_fgm_50() + 5 * self.get_fgm_40_49() + 5 * self.get_fgm_0_39() + self.get_xpm() - 2 * self.get_fga_0_39() - self.get_fga_40_49()