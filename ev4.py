# exercice 1
import json


def survey_func():
    survey = []
    stop = "N"
    while stop != "Y" or len(survey) < 10:
        if stop == "Y":
            print("Not enought data collected")
        surname = input("What is your surname? ")
        name = input("What is your name? ")
        birth_date = input("what is your date of birth? (DD/MM/YYYY) ")
        fav_color = input("what is your favorite color? ")
        survey.append(
            {
                "surname": surname,
                "name": name,
                "birth date": birth_date,
                "favorite color": fav_color
            }
        )
        stop = input("Do you wish to stop? (Y/N) ")
    with open("survey.json", "w") as outfile:
        json.dump(survey, outfile, indent=4)

    with open("survey.json", "r") as outfile:
        survey_update = json.load(outfile)
    surname_update = input("What is your surname? ")
    name_update = input("What is your name? ")
    flag = True
    i = 0

    for answer in survey_update:
        if answer["surname"] == surname_update and answer["name"] == name_update:
            print("Person found")
            answer["number of pet"] = input("How many pet do you own? ")
            break
        if answer == survey_update[-1]:
            print("Person not found")
    with open("survey.json", "w") as outfile:
        json.dump(survey, outfile, indent=4)

    with open("survey.json", "r") as outfile:
        survey_pet_update = json.load(outfile)

    for answer in survey_pet_update:
        if "number of pet" not in answer:
            print(
                f"Number of pet owned by {answer["surname"]} {answer["name"]} is unknown"
            )
            answer["number of pet"] = input("How many pet do you own? ")

    with open("survey.json", "w") as outfile:
        json.dump(survey, outfile, indent=4)


# exercice 2
import datetime


def survey_analize():
    color_ranking = {}
    today = str(datetime.date.today()).split("-")
    month_list = (
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    )
    with open("survey.json", "r") as outfile:
        survey = json.load(outfile)

    for answer in survey:
        if answer["favorite color"] in color_ranking:
            color_ranking[answer["favorite color"]] += 1
        else:
            color_ranking[answer["favorite color"]] = 1
    print(color_ranking)
    
    for answer in survey:
        birth_date = answer["birth date"].split("/")
        if today[1] == birth_date[1] and today[2] < birth_date[0]:
            print(
                f"the {birth_date[0]} {month_list[int(birth_date[1])-1]} {answer["name"]} {answer["surname"]} will celebrate their {int(today[0])-int(birth_date[2])} years"
            )