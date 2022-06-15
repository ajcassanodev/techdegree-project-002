from tkinter import N
from types import new_class


new_players_list = []
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

def main_menu():
    print("BASKETBALL TEAM STATS TOOL\n\n")
    print("----MENU----\n\n")
    print("Here are your choices:\nA)  Display Team Stats\nB)  Quit\n\n")
    main_choice = input("Enter an Option:  ")
    main_choice = main_choice.capitalize()
    if main_choice == "A":
        team_pick()
    elif main_choice == "B":
        print("Have a nice day!")
    else:
        print("invalid pick, please try again") 
        main_menu()

def team_pick():
    while True:
        print("\n\n1) Panthers\n2) Bandits\n3) Warriors\n4) Quit\n\n")
        team_pick = input("Enter an Option: " )
        try:
            team_pick = int(team_pick)
            if team_pick  > 4 :
                raise ValueError("invalid pick, please try again")
            elif team_pick < 1:
                raise ValueError("invalid pick,please try again ")
        except ValueError as err:
            print("oops {} ".format(err))
        if team_pick == 1:
            team_panthers_menu()
        if team_pick == 2:
            team_bandits_menu()
        if team_pick == 3:
            team_warriors_menu()
        if team_pick == 4:
            print("Have a great day!")
            break


def team_panthers_menu():
    print("\n\nTeam: Panthers Stats")
    print("--------------------")
    print("Total players: {} \n\n".format(len(team_panthers)))
    print("Players on Team:")
    print(*team_panthers , sep=', ')


def team_bandits_menu():
    print("\n\nTeam: Bandits Stats")
    print("--------------------")
    print("Total players: {} \n\n".format(len(team_bandits)))
    print("Players on Team:")
    print(*team_bandits , sep=', ')


def team_warriors_menu():
    print("\n\nTeam: Warriors Stats")
    print("--------------------")
    print("Total players: {} \n\n".format(len(team_warriors)))
    print("Players on Team:")
    print(*team_warriors , sep=', ')


def main():
    clean_height()
    clean_xp()
    updated_players_list()
    new_players_list.extend(updated_players_list())
    num_players_team_calc()
    team_list()
    player_list()
    seperate_names()
    main_menu()
    

def seperate_names():
    team_panthers.extend(player_list_names[0:6])
    team_bandits.extend(player_list_names[6:12])
    team_warriors.extend(player_list_names[12:18])

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
