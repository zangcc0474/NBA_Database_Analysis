DROP Database IF EXISTS NBA_Database;
CREATE Database NBA_Database;
USE Auction_Painting;


SET FOREIGN_KEY_CHECKS = 0; 
DROP TABLE IF EXISTS Game;
DROP TABLE IF EXISTS Player;
DROP TABLE IF EXISTS Player_Stats;
DROP TABLE IF EXISTS Team_Stats;
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Player_Position;
SET FOREIGN_KEY_CHECKS = 1; 


CREATE TABLE Game (
  game_date date NOT NULL,
  host varchar NOT NULL,
  guest varchar  NULL,
  host_score int  NULL,
  guest_score int  NULL,
  PRIMARY KEY (date)
)

CREATE TABLE Player (
  player_id varchar NOT NULL,
  player_name varchar(50)  NULL,
  PRIMARY KEY (player_id)
)

 CREATE TABLE Player_Stats (
  player_id varchar NOT NULL,
  assistant int NULL,
  block int NULL,
  fieldg int  NULL,
  fieldg3 int  NULL,
  fieldg3_pct decimal(4,3)  NULL,
  freet_attemp int  NULL,
  minute_played time  NULL,
  offrebound int  NULL,
  personal_foul int  NULL,
  points int  NULL,
  steal int  NULL,
  turnover int  NULL,
  total_reb int  NULL,
  fieldg_attempt int  NULL,
  freethrow int  NULL,
  fieldg3_attempt int  NULL,
  fieldg_pct decimal(4,3)  NULL,
  freethrow_pct decimal(4,3)  NULL,
  game_date date NOT NULL,
  derebound int  NULL,
  PRIMARY KEY (player_id,game_date),
  CONSTRAINT fk_game FOREIGN KEY (game_date) REFERENCES game (game_date),
  CONSTRAINT fk_player FOREIGN KEY (player_id) REFERENCES player (player_id)
)

CREATE TABLE Team_Stats (
  game date NOT NULL,
  team_abbrev varchar NOT NULL,
  tassistant int  NULL,
  tblock int  NULL,
  tfieldg int  NULL,
  tfieldg3 int  NULL,
  tfieldg3_pct decimal(4,3)  NULL,
  tfreethrow_attempt int  NULL,
  toffebound int  NULL,
  tpersonal_foul int  NULL,
  tpoints int  NULL,
  tsteal int  NULL,
  tturnover int  NULL,
  ttotal_reb int  NULL,
  tfieldg_attempt int  NULL,
  tfreethrow int  NULL,
  tfieldg3_attempt int  NULL,
  tfreethrow_pct decimal(4,3)  NULL,
  tfieldg_pct decimal(4,3)  NULL,
  PRIMARY KEY (game,team_name),
  CONSTRAINT fk_team_stats_game FOREIGN KEY (game) REFERENCES game (game_date),
  CONSTRAINT fk_team_stats_team FOREIGN KEY (team) REFERENCES team (team_abbrev)
) 

CREATE TABLE Team (
  team_name varchar(50)  NULL,
  team_abbrev varchar(20) NOT NULL,
  PRIMARY KEY (abbrev)
)

CREATE TABLE Player_Position (
  id int NOT NULL AUTO_INCREMENT,
  player_id varchar  NULL,
  position varchar  NULL,
  PRIMARY KEY (id),
  CONSTRAINT player_position_ibfk_1 FOREIGN KEY (player_id) REFERENCES player (player_id)
)