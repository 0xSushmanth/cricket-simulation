import random


class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.stats = {
            "bowling": bowling,
            "batting": batting,
            "fielding": fielding,
            "running": running,
            "experience": experience,
        }


class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = players.copy()
        self.bowlers = []

    def select_captain(self, captain):
        self.captain = captain

    def sending_next_player(self):
        if len(self.batting_order) > 0:
            return self.batting_order.pop(0)
        return None

    def choose_bowler(self):
        return random.choice(self.bowlers)


class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.properties = {
            "size": size,
            "fan_ratio": fan_ratio,
            "pitch_conditions": pitch_conditions,
            "home_advantage": home_advantage,
        }


class Umpire:
    def __init__(self, field):
        self.field = field
        self.scores = 0
        self.wickets = 0
        self.overs = 0

    def update_score(self, runs):
        self.scores += runs

    def update_wickets(self):
        self.wickets += 1

    def update_overs(self):
        self.overs += 1

    def predict_outcome(self, batsman, bowler):
        batting_prob = (
            batsman.stats["batting"]
            * self.field.properties["pitch_conditions"]
            * random.random()
        )
        bowling_prob = (
            bowler.stats["bowling"]
            * self.field.properties["pitch_conditions"]
            * random.random()
        )
        if batting_prob > bowling_prob:
            return True
        return False


class Commentator:
    def __init__(self, umpire):
        self.umpire = umpire

    def describe_ball(self, batsman, bowler):
        outcome = "OUT" if self.umpire.predict_outcome(batsman, bowler) else "NOT OUT"
        if outcome == "OUT":
            description = f"{batsman.name} is OUT!"
        else:
            description = f"{batsman.name} plays the shot."
        return description

    def describe_game(self, captain1, captain2, country1, country2, total_overs):
        print("\n--------- Game Information ---------\n")
        print(f"{country1} Vs {country2}")
        print(f"Captain 1: {captain1}, Captain 2: {captain2}")
        print(f"Total Overs: {total_overs}\n")
        print("---------------------------------------------\n")

    def describe_start(self, team):
        print("\n------------- GAME STARTED ------------------\n")
        print(f"Team {team} playing:\n")

    def describe_end(self):
        print(
            f"\nFinal Run: {self.umpire.scores} Wicket: {self.umpire.wickets} Overs: {self.umpire.overs}"
        )
        print("\n---------------------------------------------\n")

    def current_info(self, ball_count):
        print(
            f"Balls: {ball_count} Over: {self.umpire.overs} Run: {self.umpire.scores} Wicket: {self.umpire.wickets}"
        )

    def describe_final_result(self, name, scores, wickets):
        wickets_str = "wickets" if wickets != 1 else "wicket"
        print("--------------- Winner -----------------------")
        print(
            f"TEAM: {name} WON BY SCORE: {scores} with {wickets} {wickets_str} remaining"
        )
        print("\n---------------------------------------------\n")


class Match:
    def __init__(self, team1, team2, field, total_overs):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire(field)
        self.commentator = Commentator(self.umpire)
        self.total_overs = total_overs

    def start_match(self):
        self.team1.select_captain(random.choice(self.team1.players))
        self.team2.select_captain(random.choice(self.team2.players))
        self.team1.batting_order = self.team1.players.copy()
        self.team2.batting_order = self.team2.players.copy()
        self.team1.bowlers = self.team1.players.copy()
        self.team2.bowlers = self.team2.players.copy()

        self.commentator.describe_game(
            self.team1.captain.name,
            self.team2.captain.name,
            self.team1.name,
            self.team2.name,
            self.total_overs,
        )

        self.commentator.describe_start(self.team1.name)
        self.play_innings(self.team1, self.team2)
        self.commentator.describe_end()
        lastScores = self.commentator.umpire.scores

        self.commentator.umpire.scores = 0
        self.commentator.umpire.wickets = 0
        self.commentator.umpire.overs = 0
        self.commentator.describe_start(self.team2.name)
        self.play_innings(self.team2, self.team1)
        self.commentator.describe_end()
        newScores = self.commentator.umpire.scores

        if lastScores > newScores:
            self.commentator.describe_final_result(
                self.team1.name, lastScores, 10 - self.commentator.umpire.wickets
            )
        else:
            self.commentator.describe_final_result(
                self.team2.name, newScores, 10 - self.commentator.umpire.wickets
            )

    def play_innings(self, batting_team, bowling_team):
        ball_count = 1
        over = 0
        bowler = bowling_team.choose_bowler()
        batsman = batting_team.sending_next_player()

        while over < self.total_overs:
            self.commentator.current_info(ball_count)
            ball_description = self.commentator.describe_ball(batsman, bowler)

            print(ball_description)
            if ball_description.endswith("OUT!"):
                batsman = batting_team.sending_next_player()
                if batsman is None:
                    break
                self.umpire.update_wickets()
                print(f"Wickets: {self.umpire.wickets}, Overs: {self.umpire.overs}")
                print(f"New player {batsman.name} is playing...")
            else:
                runs = random.randint(0, 6)
                self.umpire.update_score(runs)

            if ball_count > 5:
                over += 1
                print(f"Over {over} Starting...")
                self.umpire.update_overs()
                bowler = bowling_team.choose_bowler()
                ball_count = 0

            self.commentator.current_info(ball_count)
            ball_count += 1


# Creating fake data
# Adding the players
player1 = []
for i in range(10):
    player1.append(
        Player(
            "Player1_" + str(i + 1),
            round(random.random(), 1),
            round(random.random(), 1),
            round(random.random(), 1),
            round(random.random(), 1),
            round(random.random(), 1),
        )
    )
player2 = []
for i in range(10):
    player2.append(
        Player(
            "Player2_" + str(i + 1),
            round(random.random(), 1),
            round(random.random(), 1),
            round(random.random(), 1),
            round(random.random(), 1),
            round(random.random(), 1),
        )
    )

# Adding players to teams
team1 = Team("Country1", player1)
team2 = Team("Country2", player2)

# Creating the field
field = Field("Large", 0.7, 0.8, 0.9)

# Setting the total overs for the match
total_overs = 1

# Creating and starting the match
match = Match(team1, team2, field, total_overs)
match.start_match()
