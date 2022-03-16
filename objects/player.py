class Player:
    def __init__(self, data) -> None:
        self.team = data[1]
        self.role = data[2]
        self.player = data[3]
        self.player_kills = data[4]
        self.player_deaths = data[5]
        self.player_assists = data[6]
        self.player_kda = data[7]
        self.average_cs = data[8]
        self.total_cs = data[9]
        self.average_jg_prox = data[10]
        self.total_iso_deaths = data[11]
        self.average_iso_deaths = data[12]
        self.average_vision_score = data[13]
        self.average_percent_mid_lane = data[14]
        self.average_damage_to_champs = data[15]
        self.total_first_bloods = data[16]
        self.first_blood_rate = data[17]
        self.total_solo_kils = data[18]
        self.solo_kill_rate = data[19]
        self.total_player_gold = data[20]
        self.total_team_gold = data[21]
        self.gold_share = data[22]
        self.average_gold_diff_15 = data[23]
        self.total_player_damage_to_champs = data[24]
        self.total_team_damage_to_champs = data[25]
        self.damage_share = data[26]