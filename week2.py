#question 1
names = ["shaun", "zack", "lewis"]
#print(names)

#question 2
#for x in range(3):
#   print("Hello " + names[x] + " how are you?")

#question3
#places = ["England", "Russia", "India", "Oman", "UAE"]
#print(places)
#print(sorted(places))
#print(places)
#places.sort(reverse=True)
#print(places)
#places.reverse()
#print(places)

#question4
cities = ["Kiev", "London", "Liverpool", "Amsterdam", "Barcelona", "Madrid"]
#del(cities)
#cities = ["Kiev", "London", "Liverpool", "Amsterdam", "Barcelona", "Madrid"]

len(cities)
cities.append("Manchester") #adds onto end of the list
cities.insert(1, "Vancouver") #inserts vancouver at position 1 so second position as it starts at 0
cities.remove("Barcelona") #removes the third item of the list
removedItem = cities.pop(5)
print(removedItem)
print(cities)