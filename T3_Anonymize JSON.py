import json

file_name="users_1k.json"

with open (file_name,"r") as json_file:
        data=json.load(json_file)


for entry in data:
    entry["name"] = None

    for friend in entry["friends"]:
        friend["name"] = None 


with open (file_name,"w") as file:
        json.dump(data,file,indent=2)
