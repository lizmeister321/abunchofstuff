# with open ("states.txt", "r") as some_variable:
# 	states = some_variable.read().split("\n")

# abbreviations = []
# state_names = []

# for index, state in enumerate(states):
# 	states[index] = state.split("\t")
# 	abbreviations.append(states[index][0])
# 	state_names.append(states[index][1])

# #print abbreviations
# #print state_names

# with open ("state-abbrev.txt", "w") as abbrev_file:
# 	abbrev_file.write(str(abbreviations))

# with open ("state-name.txt", "w") as name_file:
# 	for name in state_names:
# 		name_file.write(name + "\n")

# students = {"Shannon": "@shannonturner", 
# 			"Sarah-Jaine": "@sarahjaine",
# 			"Sarah": "@sng0616",
# 			"Lizzie": "@lizmeister321"}

# print students["Sarah"]


contacts = {
    "Hear Me Code": {
        "twitter": "@hearmecode",
        "github": "https://github.com/hearmecode"
    },
    "Shannon Turner": {
        "twitter": "@svt827",
        "github": "https://github.com/shannonturner"
    },
}

# How to add a new item to an existing dictionary:
contacts["Aliya Rahman"] = {
    "twitter": "@AliyaRahman",
    "github": "https://github.com/aliyarahman"
}

# Exercise 1: Add a new dictionary item to contacts for each person at your table.
#   Rather than editing lines 1-10 above, add new entries to the contacts dictionary below.
#   Keep in mind some people may not have a twitter account, and that's okay!

contacts["Vero Wrede"] = {
	"twitter": "",
	"github": "https://github.com/verowrede"
}

contacts["Shayna McCready"] = {
	"twitter": "mzsmcree",
	"github": "https://github.com/mzsmcree"
}

contacts["Galina Soloyeva"] = {
	"twitter": "",
	"github":"https://github.com/galinams"
}

contacts["Lucy Xu"] = {
	"twitter":"lucypxu",
	"github":"https://github.com/lucypxu"
}

contacts["Anjana Nair"] = {
	"twitter":"",
	"github":"https://github.com/anjanaN"
}

# Exercise 2: Loop through the contacts dictionary to display everyone's contact information.
#   Your output should look like this:

# Hear Me Code's info: 
#     twitter: @hearmecode
#     github: https://github.com/hearmecode
# Shannon Turner's info: 
#     twitter: @svt827
#     github: https://github.com/shannonturner

for key, value in sorted(contacts.items()):
	print key + "'s info:"
	for key2, value2 in value.items():
		print "\t" + key2 + ": " + value2

