# Python Dictionaries

# programming_dictionaries = {
# 	"Bug":"An error in a code that doesn't allow it to execute.",
# 	"Function" : "Piece of code that can be called.",
# 	"Loop": "An action of doing something over and over again."
# }

# # Retrieving items from Dictionaries
# print(programming_dictionaries["Bug"])
# print(programming_dictionaries["Function"])
# print(programming_dictionaries["Loop"])
#
# #Adding new items to your dictionary
# programming_dictionaries["Loop"] = "Process of doing something repeatedly."
# # print(programming_dictionaries)
#
# # Empty dictionaries
# empty_dictionary = {}
#
# # Wipe an existing dictionary
# programming_dictionaries = {}

# Edit an item in a dictionary
# programming_dictionaries["Bug"] = "A moth in your computer"
# print(programming_dictionaries)

# Loop through a dictionary
# for key in programming_dictionaries:
# 	print(key)
# 	print(programming_dictionaries[key])

# NESTING DICTIONARIES(putting one inside of the other)
Capitals = {
	"France":"Paris",
	"Germany":"Berlin"
}

# Nesting a list in a Dictionary
travel_log = {

	"France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_travel":12},
	"Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits":50}
  }

# Nesting a dictionary in a list

travel_logg = [
	{
		"country": "France",
		"cities_visited": ["Paris", "Lille", "Dijon"],
		"total_visits" : 12,
	},
	{
	    "country": "Germany",
		"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits" : 5,
   }
]



# Assignent
# Modify the nested dictionary above


# define the function
def add_new_country(country_visited, times_visited, cities_visited):
	new_country = {}
	new_country["country"] = country_visited
	new_country["visits"] = times_visited
	new_country["cities"] = cities_visited
	travel_logg.append(new_country)

# print out the travel_logg
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_logg)

