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
        self.__fileName = "flights.txt"
        #self.__fileName = input("Enter a file name: ")
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
    
    def getRouteHelper(self, startCity, endCity, visitedCities):
        if startCity == endCity:
            return [startCity]
        else:
            visitedCities.append(startCity)
            self.__neighbors = list(Flights.getNeighboringCities(self, startCity))
            for i in self.__neighbors:
                print(i)
                if i not in visitedCities:
                    if i == endCity:
                        visitedCities.append(endCity)
                        return visitedCities
                    else:
                        return Flights.getRouteHelper(self, startCity = i, endCity=endCity, visitedCities=visitedCities)
                else:
                    visitedCities = []
                    break
                    

    def getRoute(self, startCity, endCity):
        if startCity not in self.__cityList:
            print("City", startCity, "not found")
            return
        if endCity not in self.__cityList:
            print("City", endCity, "not found")
            return
        return self.getRouteHelper(startCity, endCity, visitedCities = [])
    
    def getRoutePrice(self, route):
        self.__price = 0
        for i in len(route-1):
            self.__start = self.__dictionary[route[i]]
            self.__next = route[i+1]
            for j in self.__start:
                if j[0] == self.__next:
                    self.__price += j[1]
        return self.__price
    
    def getPrice(self, startCity, endCity):
        self.__route = Flights.getRoute(startCity, endCity)
        return Flights.getRoutePrice(self.__route)
    
# Need to finish route finding algorithm (getRouteHelper)
# Need to test getRoutePrice, getPrice