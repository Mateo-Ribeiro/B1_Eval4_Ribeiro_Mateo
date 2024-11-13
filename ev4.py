#exercice 1
import json
def survey_func():
    survey=[]
    stop="N"
    while stop!="Y" and len(survey)<2:
        if stop=="Y":
            print("Not enought data collected")
        surname=input("What is your surname? ")
        name=input("What is your name? ")
        birth_date=input("what is your date of birth? (DD/MM/YYYY) ")
        fav_color=input("what is your favorite color? ")
        survey.append({"surname":surname,"name":name,"birth date":birth_date,"favorite color":fav_color})
        stop=input("Do you wish to stop? (Y/N) ")
    with open("survey.json","w") as outfile:
        json.dump(survey,outfile,indent=4)
    with open("survey.json","r") as outfile:
        survey_update=json.load(outfile)
    surname_update=input("What is your surname? ")
    name_update=input("What is your name? ")
    flag=True
    i=0
    for answer in survey_update:
        if answer["surname"]==surname_update and answer["name"]==name_update:
            print("Person found")
            answer["number of pet"]=input("How many pet do you own? ")
            break
        if answer==survey_update[-1]:
            print("Person not found")
    with open("survey.json","w") as outfile:
        json.dump(survey,outfile,indent=4)
    with open("survey.json","r") as outfile:
        survey_pet_update=json.load(outfile)
    for answer in survey_pet_update:
        if "number of pet" not in answer:
            print(f"Number of pet owned by {answer["surname"]} {answer["name"]} is unknown")
            answer["number of pet"]=input("How many pet do you own? ")
    with open("survey.json","w") as outfile:
        json.dump(survey,outfile,indent=4)