
import json
file=open("api_json\person.json","w")

name=input("Your name: ")
dob=int(input("Your birth year: "))

person={
    "name":name,
    "dob":dob
}


json.dump(person,file,indent=2)
