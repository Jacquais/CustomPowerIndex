import requests
import time
import sys
import os.path
import platform
from colorama import init
from termcolor import colored
init()

def Quit():
    print(colored("\nBye Bye!", "green"))
    time.sleep(.5)
    sys.exit()


try:
    if platform.system() == "Windows":
        os.system('mode con: cols=115 lines=60')
        input("Press any key to continue...")
    elif platform.system() == "Darwin":
        os.system('printf "\e[8;60;115;t"')
        os.system('clear')
        input("Press any key to continue...")
    print(colored('''
    #######################################
    #######################################
    ############   #(    /#   #   #########
    ############   #  (#  #   #  ##########
    ############   #  ##  #      ##########
    ############   #  #####     ###########
    ############   #  #####     ,##########
    ########   #   #  ##,,#   ,  ##########
    ########   #   #  ##  #   #  ##########
    ########      /#      #   #   #########
    ##########  .#####  ###///#///#########
    #######################################\n\n''', "green"))
    def NCAA():
        print("Not Implemented.")


    def NFL():

        def fetch(week):
            print("Fetching data from week {}".format(week))
            schedule = requests.get(
                'http://api.sportradar.us/nfl-ot2/games/2017/REG/schedule.json?api_key=z45b8e45rg282tyqq686g5n5')
            schedule = schedule.json()
            GamesCount = len(schedule["weeks"][week]["games"])
            games = -1
            teams = {}
            week -= 1

            print("Getting Data and Calculating\n")
            for _ in range(GamesCount):
                games += 1
                homenamekey = 'HomeName' + str(games)
                homeidkey = 'HomeID' + str(games)
                awaynamekey = 'AwayName' + str(games)
                awayidkey = 'AwayID' + str(games)
                gameid = "GameID" + str(games)
                teams[homeidkey] = schedule["weeks"][week]["games"][games]["home"]["id"]  # Home Team ID
                teams[homenamekey] = schedule["weeks"][week]["games"][games]["home"]["name"]  # Home Team Name
                teams[awayidkey] = schedule["weeks"][week]["games"][games]["away"]["id"]  # Away Team ID
                teams[awaynamekey] = schedule["weeks"][week]["games"][games]["away"]["name"]  # Away Team Name
                teams[gameid] = schedule["weeks"][week]["games"][games]["id"]  # Game ID (For use in displaying game results)

                # CALCULATE
                time.sleep(1)
                HomeCall = requests.get("http://api.sportradar.us/nfl-ot2/seasontd/2017/REG/teams/" + teams[
                    homeidkey] + "/statistics.json?api_key=z45b8e45rg282tyqq686g5n5")
                HomeCall = HomeCall.json()

                time.sleep(1)
                AwayCall = requests.get("http://api.sportradar.us/nfl-ot2/seasontd/2017/REG/teams/" + teams[
                    awayidkey] + "/statistics.json?api_key=z45b8e45rg282tyqq686g5n5")
                AwayCall = AwayCall.json()


                hometouchdowns = HomeCall["record"]["touchdowns"]["total"]
                hometouchdownspergame = hometouchdowns / HomeCall["record"]["games_played"]

                homepasstouchdowns = HomeCall["record"]["touchdowns"]["pass"]
                homepasstouchdownspergame = homepasstouchdowns / HomeCall["record"]["games_played"]
                homeopponentpasstouchdownspergame = HomeCall["opponents"]["passing"]["touchdowns"] / HomeCall["opponents"]["games_played"]

                homerushtouchdowns = HomeCall["record"]["touchdowns"]["rush"]
                homerushtouchdownspergame = homerushtouchdowns / HomeCall["record"]["games_played"]
                homeopponentrushtouchdownspergame = HomeCall["opponents"]["rushing"]["touchdowns"] / HomeCall["opponents"]["games_played"]

                homerushyards = HomeCall["record"]["rushing"]["yards"]
                homerushyardspergame = homerushyards / HomeCall["record"]["games_played"]
                homeopponentrushyardspergame = HomeCall["opponents"]["rushing"]["yards"] / HomeCall["opponents"]["games_played"]

                homepassyards = HomeCall["record"]["passing"]["yards"]
                homepassyardspergame = homepassyards / HomeCall["record"]["games_played"]
                homeopponentpassyardspergame = HomeCall["opponents"]["passing"]["yards"] / HomeCall["opponents"]["games_played"]

                homerushespergame = HomeCall["record"]["rushing"]["attempts"] / HomeCall["record"]["games_played"]
                homepassespergame = HomeCall["record"]["passing"]["attempts"] / HomeCall["record"]["games_played"]
                homeopponentpassespergame = HomeCall["opponents"]["passing"]["attempts"] / HomeCall["opponents"]["games_played"]
                homeopponentrushespergame = HomeCall["opponents"]["rushing"]["attempts"] / HomeCall["opponents"]["games_played"]

                homefieldgoalspergame = HomeCall["record"]["field_goals"]["made"] / HomeCall["record"]["games_played"]
                homeconversions = HomeCall["record"]["extra_points"]["conversions"]["pass_successes"] + HomeCall["record"]["extra_points"]["conversions"]["rush_successes"]
                homeconversionspergame = homeconversions / HomeCall["record"]["games_played"]

                homepointspergameallowed = (
                                            (6*HomeCall["opponents"]["touchdowns"]["total"])+
                                            (3*HomeCall["opponents"]["field_goals"]["made"])+
                                            (HomeCall["opponents"]["extra_points"]["kicks"]["made"])+
                                            (2*(HomeCall["opponents"]["extra_points"]["conversions"]["pass_successes"] + HomeCall["opponents"]["extra_points"]["conversions"]["rush_successes"]))
                                            )



                awaytouchdowns = AwayCall["record"]["touchdowns"]["total"]
                awaytouchdownspergame = awaytouchdowns / AwayCall["record"]["games_played"]

                awaypasstouchdowns = AwayCall["record"]["touchdowns"]["pass"]
                awaypasstouchdownspergame = awaypasstouchdowns / AwayCall["record"]["games_played"]
                awayopponentpasstouchdownspergame = AwayCall["opponents"]["passing"]["touchdowns"] / AwayCall["opponents"]["games_played"]

                awayrushtouchdowns = AwayCall["record"]["touchdowns"]["rush"]
                awayrushtouchdownspergame = awayrushtouchdowns / AwayCall["record"]["games_played"]
                awayopponentrushtouchdownspergame = AwayCall["opponents"]["rushing"]["touchdowns"] / AwayCall["opponents"]["games_played"]

                awayrushyards = AwayCall["record"]["rushing"]["yards"]
                awayrushyardspergame = awayrushyards / AwayCall["record"]["games_played"]
                awayopponentrushyardspergame = AwayCall["opponents"]["rushing"]["yards"] / AwayCall["opponents"]["games_played"]

                awaypassyards = AwayCall["record"]["passing"]["yards"]
                awaypassyardspergame = awaypassyards / AwayCall["record"]["games_played"]
                awayopponentpassyardspergame = AwayCall["opponents"]["passing"]["yards"] / AwayCall["opponents"]["games_played"]

                awayrushespergame = AwayCall["record"]["rushing"]["attempts"] / AwayCall["record"]["games_played"]
                awaypassespergame = AwayCall["record"]["passing"]["attempts"] / AwayCall["record"]["games_played"]
                awayopponentpassespergame = AwayCall["opponents"]["passing"]["attempts"] / AwayCall["opponents"]["games_played"]
                awayopponentrushesspergame = AwayCall["opponents"]["rushing"]["attempts"] / AwayCall["opponents"]["games_played"]

                awayfieldgoalspergame = AwayCall["record"]["field_goals"]["made"] / AwayCall["record"]["games_played"]
                awayconversions = AwayCall["record"]["extra_points"]["conversions"]["pass_successes"] + AwayCall["record"]["extra_points"]["conversions"]["rush_successes"]
                awayconversionspergame = awayconversions / AwayCall["record"]["games_played"]

                awaypointspergameallowed = (
                                            (6*AwayCall["opponents"]["touchdowns"]["total"])+
                                            (3*AwayCall["opponents"]["field_goals"]["made"])+
                                            (AwayCall["opponents"]["extra_points"]["kicks"]["made"])+
                                            (2*(AwayCall["opponents"]["extra_points"]["conversions"]["pass_successes"] + AwayCall["opponents"]["extra_points"]["conversions"]["rush_successes"]))
                                            )

                HomeScore = (((((hometouchdownspergame*(6.98)+homefieldgoalspergame*(3)+homeconversionspergame*(2))+(((homerushtouchdownspergame+homeopponentrushtouchdownspergame)*(1+(homerushespergame+homeopponentrushespergame)/(homerushespergame+homeopponentpassespergame+homepassespergame+homeopponentpassespergame)))*(6.98))+(((homepasstouchdownspergame+homeopponentpasstouchdownspergame)*(1+(homepassespergame+homeopponentpassespergame)/(homerushespergame+homepassespergame+homeopponentrushespergame+homeopponentpassespergame))*(6.98))+homepointspergameallowed)/4)+((homerushyardspergame+homeopponentrushyardspergame)/115)+((homepassyardspergame+homeopponentpassyardspergame)/285))))
                AwayScore = (

                    (
                        (awaytouchdownspergame*(6.98)+awayfieldgoalspergame*(3)+awayconversionspergame*(2))+
                        (((awayrushtouchdownspergame+awayopponentrushtouchdownspergame)*(1+(awayrushespergame+awayopponentrushesspergame)/(homerushespergame +awayopponentrushesspergame+awaypassespergame+awayopponentpassespergame)))*(6.98))+
                        (((awaypasstouchdownspergame+awayopponentpasstouchdownspergame)*(1+(awaypassespergame+awayopponentpassespergame)/(awayrushespergame+awayopponentrushesspergame+awaypassespergame+awayopponentpassespergame))*(6.98))+awaypointspergameallowed)/4
                    )+
                        ((awayrushyardspergame+awayopponentrushyardspergame)/115)+
                        ((awaypassyardspergame+awayopponentpassyardspergame)/285)
                    )
               # print(HomeScore, " ", AwayScore) Verbose Mode?
                if HomeScore > AwayScore:
                    print("The " + teams[homenamekey] + " will beat the " + teams[awaynamekey], end='')

                    try:
                        if schedule["weeks"][week]["games"][games]["scoring"]["home_points"] > schedule["weeks"][week]["games"][games]["scoring"]["away_points"]:
                            print(colored(" CORRECT", "green"))
                        elif schedule["weeks"][week]["games"][games]["scoring"]["home_points"] <= schedule["weeks"][week]["games"][games]["scoring"]["away_points"]:
                            print(colored(" INCORRECT", "red"))
                        else:
                            print(colored(" GAME NOT PLAYED", "yellow"))
                    except KeyError:
                        print(colored(" GAME NOT PLAYED", "yellow"))

                elif HomeScore < AwayScore:
                    print("The " + teams[homenamekey] + " will lose to the " + teams[awaynamekey], end='')

                    try:
                        if schedule["weeks"][week]["games"][games]["scoring"]["home_points"] < schedule["weeks"][week]["games"][games]["scoring"]["away_points"]:
                            print(colored(" CORRECT", "green"))
                        elif schedule["weeks"][week]["games"][games]["scoring"]["home_points"] >= schedule["weeks"][week]["games"][games]["scoring"]["away_points"]:
                            print(colored(" INCORRECT", "red"))
                        else:
                            print(colored(" GAME NOT PLAYED", "yellow"))
                    except KeyError:
                        print(colored(" GAME NOT PLAYED", "yellow"))

                else:
                    print("The " + teams[homenamekey] + " will tie the " + teams[awaynamekey], end='')

                    try:
                        if schedule["weeks"][week]["games"][games]["scoring"]["home_points"] == schedule["weeks"][week]["games"][games]["scoring"]["away_points"]:
                            print(colored("CORRECT", "green"))
                        elif schedule["weeks"][week]["games"][games]["scoring"]["home_points"] != schedule["weeks"][week]["games"][games]["scoring"]["away_points"]:
                            print(colored(" INCORRECT", "red"))
                        else:
                            print(colored(" GAME NOT PLAYED", "yellow"))
                    except KeyError:
                        print(colored(" GAME NOT PLAYED", "yellow"))
            print()
        while True:
            Choice = input(
                "[1]Predict this weeks NFL games\n[2]Predict other weeks NFL games\n[99]Back\n")
            if Choice == "1":
                date = time.strftime("%y-%m-%d")
                if date < "17-09-07":
                    # week 1
                    fetch(1)
                elif "17-09-11" <= date <= "17-09-18":
                    # week 2
                    fetch(2)
                elif "17-09-19" <= date <= "17-09-25":
                    # week 3
                    fetch(3)
                elif "17-09-26" <= date <= "17-10-2":
                    # week 4
                    fetch(4)
                elif "17-10-3" <= date <= "17-10-9":
                    # week 5
                    fetch(5)
                elif "17-10-10" <= date <= "17-9-16":
                    # week 6
                    fetch(6)
                elif "17-10-17" <= date <= "17-10-23":
                    # week 7
                    fetch(7)
                elif "17-10-24" <= date <= "17-10-30":
                    # week 8
                    fetch(8)
                elif "17-10-31" <= date <= "17-11-06":
                    # week 9
                    fetch(9)
                elif "17-11-07" <= date <= "17-11-13":
                    # week 10
                    fetch(10)
                elif "17-11-14" <= date <= "17-11-20":
                    # week 11
                    fetch(11)
                elif "17-11-21" <= date <= "17-11-27":
                    # week 12
                    fetch(12)
                elif "17-11-28" <= date <= "17-12-04":
                    # week 13
                    fetch(13)
                elif "17-12-05" <= date <= "17-12-11":
                    # week 14
                    fetch(14)
                elif "17-12-12" <= date <= "17-12-18":
                    # week 15
                    fetch(15)
                elif "17-12-19" <= date <= "17-12-25":
                    # week 16
                    fetch(16)
                elif "17-12-25" <= date <= "17-12-31":
                    # week 17
                    fetch(17)
                else:
                    print("I need to update this, or your clock is broken.")
            elif Choice == "2":
                while True:
                    weekInput = input("Enter the week you would like to predict.\n")
                    try:
                        if 1 <= int(weekInput) <= 17:
                            fetch(int(weekInput))
                            break
                        else:
                            print("That is not a valid week- There are 17 weeks in the NFL Regular season.\n")
                            continue
                    except ValueError:
                        print("That is not a valid week- There are 17 weeks in the NFL Regular season.\n")
                        continue


    while True:
        choice = input("[1] Predict NFL games\n"
                       "[2] Predict CFB games\n"
                       "[99] Quit\n")
        if choice == "1":
            NFL()
        elif choice == "2":
            NCAA()
        elif choice == "99":
            Quit()
        else:
            print("That is not a valid response.")
except (KeyboardInterrupt, EOFError):
    # Really weird, but it works.
    try:
        Quit()
    except KeyboardInterrupt:
        sys.exit()
