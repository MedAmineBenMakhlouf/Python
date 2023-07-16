class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]
    
    @classmethod
    def get_team(cls, team_list):
        players = []
        for player_dict in team_list:
            player = cls(player_dict)
            players.append(player)
        return players

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Forward",
        "team": "Philadelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

# Challenge 2: Create instances using individual player dictionaries
kevin = Player(players[0])
jason = Player(players[1])
kyrie = Player(players[2])

# Challenge 3: Populate a new list with Player instances from the list of players
new_team = Player.get_team(players)

# Print player information for the instances
print("Kevin:")
print(f"Name: {kevin.name}, Age: {kevin.age}, Position: {kevin.position}, Team: {kevin.team}\n")
print("Jason:")
print(f"Name: {jason.name}, Age: {jason.age}, Position: {jason.position}, Team: {jason.team}\n")
print("Kyrie:")
print(f"Name: {kyrie.name}, Age: {kyrie.age}, Position: {kyrie.position}, Team: {kyrie.team}\n")

# Print player information for the new_team list
print("New Team:")
for player in new_team:
    print(f"Name: {player.name}, Age: {player.age}, Position: {player.position}, Team: {player.team}")