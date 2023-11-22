from Flights import *

s = Flights()

longRoute = []

print(s.getRoute("Phoenix", "New York"))
print(s.getRoutePrice(longRoute))

#lst = ["Chicago", "Phoenix", "Miami", "Dallas"]
#lst = set(lst)
#print(set(lst))

#neighbors = s.getNeighboringCities("Dallas")

#print(neighbors.intersection(lst))

# print(s.getRoutePrice(longFlight))


# count = 0
# if neighbors.intersection(lst) == neighbors:
#     print(list(lst)[-2-count])
#     visitedCities = list(lst)[0:(-1-count)]
#     visitedCities = set(visitedCities)
#     print(visitedCities)
#     count += 1


