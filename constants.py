from types import new_class


new_players_list = [{}]
team_players = []
player_list_names = []
team_panthers =  []
team_bandits = []
team_warriors = []

def clean_height():
    for i in PLAYERS:
        get_height = i['height']
        height_split = get_height.split(" ")
        i['height'] = int(height_split[0])
    return i


def clean_xp():
    for i in PLAYERS:
        get_xp = i['experience']
        if i['experience'] == 'YES':
            i['experience'] = True
        else:
            i['experience'] = False
    return i         

def updated_players_list():
    new_list = [{}]
    for i in PLAYERS:
        new_list.append(i)
    return new_list


def num_players_team_calc():
    num_players_team = int(len(PLAYERS) / len(TEAMS))
    print("number of players on each team should be {}".format(num_players_team))

def main():
    clean_height()
    clean_xp()
    updated_players_list()
    new_players_list.append(updated_players_list())
    print(new_players_list)
    num_players_team_calc()
    team_list()
    player_list()
    seperate_names()

def seperate_names():
    team_panthers = player_list_names[0:6]
    team_bandits =  player_list_names[6:12]
    team_warriors = player_list_names[12:18]
    print(team_panthers)
    print(team_bandits)
    print(team_warriors)

def team_list():
    for i in TEAMS:
        team_players.append(i)


def player_list():
    for i in PLAYERS:
        names = i['name']
        player_list_names.append(names)


TEAMS = [
'Panthers',
'Bandits',
'Warriors',
]

PLAYERS = [{
        'name': 'Karl Saygan',
        'guardians': 'Heather Bledsoe',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Matt Gill',
        'guardians': 'Charles Gill and Sylvia Gill',
        'experience': 'NO',
        'height': '40 inches'
    },
    {   'name': 'Sammy Adams',
        'guardians': 'Jeff Adams and Gary Adams',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Chloe Alaska',
        'guardians': 'David Alaska and Jamie Alaska',
        'experience': 'NO',
        'height': '47 inches'
    },
    {
        'name': 'Bill Bon',
        'guardians': 'Sara Bon and Jenny Bon',
        'experience': 'YES',
        'height': '43 inches'
    },
    {
        'name': 'Joe Kavalier',
        'guardians': 'Sam Kavalier and Elaine Kavalier',
        'experience': 'NO',
        'height': '39 inches'
    },
    {
        'name': 'Phillip Helm',
        'guardians': 'Thomas Helm and Eva Jones',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Les Clay',
        'guardians': 'Wynonna Brown',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Sal Dali',
        'guardians': 'Gala Dali',
        'experience': 'NO',
        'height': '41 inches'
    },
    {
        'name': 'Suzane Greenberg',
        'guardians': 'Henrietta Dumas',
        'experience': 'YES',
        'height': '44 inches'
    },
    {
        'name': 'Jill Tanner',
        'guardians': 'Mark Tanner',
        'experience': 'YES',
        'height': '36 inches'
    },
    {
        'name': 'Arnold Willis',
        'guardians': 'Claire Willis',
        'experience': 'NO',
        'height': '43 inches'
    },
    {
        'name': 'Herschel Krustofski',
        'guardians': 'Hyman Krustofski and Rachel Krustofski',
        'experience': 'YES',
        'height': '45 inches'
    },
    {
        'name': 'Eva Gordon',
        'guardians': 'Wendy Martin and Mike Gordon',
        'experience': 'NO',
        'height': '45 inches'
    },
    {
        'name': 'Ben Finkelstein',
        'guardians': 'Aaron Lanning and Jill Finkelstein',
        'experience': 'NO',
        'height': '44 inches'
    },
    {
        'name': 'Joe Smith',
        'guardians': 'Jim Smith and Jan Smith',
        'experience': 'YES',
        'height': '42 inches'
    },
    {
        'name': 'Diego Soto',
        'guardians': 'Robin Soto and Sarika Soto',
        'experience': 'YES',
        'height': '41 inches'
    },
    {
        'name': 'Kimmy Stein',
        'guardians': 'Bill Stein and Hillary Stein',
        'experience': 'NO',
        'height': '41 inches'
    }
]
