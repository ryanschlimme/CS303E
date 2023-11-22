# Flights.py
# Ryan Schlimme
# rjs4499
# CS 303E
#
# 16 November 2023
# This program defines a Flights class which reads a filename. If the file does not exist, it prints an error message.
# If it does exits, the program reads the first line as a list of city names and stores it as a private class attribute.
# Then, it reads the rest of the lines as cityA, cityB, price sets and creates a dictionary mapping cityA to pair cityB,price.
# Additionally, it maps cityB to cityA, price. Then, the class creates getters for cities, flights, neighboring cities, route,
# route helper, routeprice, and price. 

import os

class Flights:
    def __init__(self):
        self.__fileName = input("Enter a file name: ")
        if os.path.isfile(self.__fileName) == False:
            print("Cannot find file:", self.__fileName)
            return
        else:
            self.__file = open(self.__fileName, "r")
            self.__cities = self.__file.readline()
            self.__cityList = [s.strip() for s in self.__cities.split(",")]
            self.__dictionary = {}
            for i in self.__cityList:
                self.__dictionary[i] = []    
            self.__line = self.__file.readline()
            while self.__line:
                self.__contents = [s.strip() for s in self.__line.split(",")]
                self.__dictionary[self.__contents[0]].append((self.__contents[1], self.__contents[2]))
                self.__dictionary[self.__contents[1]].append((self.__contents[0], self.__contents[2]))
                self.__line = self.__file.readline()
    
    def getCities(self):
        return self.__cityList
    
    def getFlights(self):
        for i in self.__dictionary.items():
            destinations = []
        return self.__dictionary
    
    def __str__(self):
        self.__string = ""
        for i in self.__dictionary.items():
            self.__string = self.__string + "  " + str(i) + "\n"
        return ("Cities: " + str(self.__cityList) + "\n" + "Flights: \n" + self.__string)
    
    def getNeighboringCities(self, city):
        if city not in self.__cityList:
            print("City", city, "not found")
            return
        self.__close = self.__dictionary[city]
        self.__neighbors = set()
        for i in self.__close:
            self.__neighbors.add(i[0])
        return self.__neighbors
                    
    def getRouteHelper(self, startCity, endCity, visitedCities, count, route):
        if visitedCities == None:
            visitedCities = list()
            route = list()
        if startCity == endCity:
            visitedCities.append(endCity)
            route.append(endCity)
            return route
        else:
            visitedCities.append(startCity)
            route.append(startCity)
            neighbors = list(Flights.getNeighboringCities(self, startCity))
            if endCity in neighbors:
                visitedCities.append(endCity)
                route.append(endCity)
                return route
            if set(visitedCities).intersection(set(neighbors)) == set(neighbors):
                nextCity = visitedCities[-2]
                route = route[0:(-1-count)]
                count += 1
                if -1*(-1-count) == len(self.__cityList)-1:
                    return []
                return Flights.getRouteHelper(self, startCity = nextCity, endCity= endCity, 
                                              visitedCities= visitedCities, count = count, route = route)
            for i in neighbors:
                if i in visitedCities:
                    continue
                else:
                    count = 0
                    return Flights.getRouteHelper(self, startCity= i, endCity=endCity, 
                                                  visitedCities=visitedCities, count = 0, route = route)

    def getRoute(self, startCity, endCity):
        if startCity not in self.__cityList:
            print("City", startCity, "not found")
            return
        if endCity not in self.__cityList:
            print("City", endCity, "not found")
            return
        if startCity != endCity:
            result = self.getRouteHelper(startCity = startCity, endCity = endCity, 
                                       visitedCities = None, count = 0, route = list())
            return list(dict.fromkeys(result))
        else:
            return [startCity]
    
    def getRoutePrice(self, route):
        if route == []:
            return -1
        self.__price = 0
        for i in range(len(route)-1):
            self.__start = self.__dictionary[route[i]]
            self.__next = route[i+1]
            for j in self.__start:
                if j[0] == self.__next:
                    self.__price += int(j[1])
        return self.__price
    
    def getPrice(self, startCity, endCity):
        if startCity == endCity:
            return 0
        if startCity not in self.__cityList:
            print("City", startCity, "not found")
            return
        if endCity not in self.__cityList:
            print("City", endCity, "not found")
            return
        self.__route = Flights.getRoute(self, startCity, endCity)
        if self.__route == []:
            return -1
        else:
            return Flights.getRoutePrice(self, self.__route)