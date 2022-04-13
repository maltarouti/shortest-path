import re
import sys
from PriorityQueue import PriorityQueue
from City import City


class ShortestPath:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal

        self.distances = None
        self.locations = None

        # The number of cities you can get from expanding one city
        # This has been initialized because we don't have enough data
        # that tells us the cities we can visit directly from one country
        self.SIGHT = 10

        # The average speed in Saudi Arabia in KM
        self.AVERAGE_SPEED = 110

        # The rate of Liter/KM
        self.LITER_USAGE = 0.13625

    def _load_files(self) -> None:
        """
        Load cities distance and cities location
        Cities distance: shows the distance between each city
        Cities location: shows the latitude and longitude of each city
        """
        distances = {}
        with open("cities_distance.txt", "r") as f:
            data = f.readlines()
            for row in data:
                try:
                    cities = re.findall("[A-Za-z]+", row)
                    A, B = cities[0], cities[1]
                    distance = re.findall("[0-9]+.*[0-9]*", row)[0]
                except:
                    continue

                if A not in distances:
                    distances[A] = {}

                if B not in distances[A]:
                    distances[A][B] = float(distance)
            self.distances = distances

        locations = {}
        with open("cities_location.txt", "r") as f:
            data = f.readlines()
            for row in data:
                try:
                    city = re.findall("[A-Za-z]+", row)[0]
                    location = re.findall("[0-9]+\\.*[0-9]*", row)
                    location = float(location[0]), float(location[1])
                    if city not in locations:
                        locations[city] = location
                except:
                    continue
        self.locations = locations

    def _verify_inputs(self) -> bool:
        """
        verify if start and goal were valid
        """
        if (self.start not in self.distances
                or self.goal not in self.distances):
            raise "Please make sure to enter valid cities."
        return True

    def _get_result(self, city: City) -> tuple:
        """
        :param: a city as a City object
        :return: 
            1. Path: list of cities that has been passed to reach the given city
            2. Total distance: the total distance of the path
            3. Total time: the estimated time of the path
            4. Total cost: the total cost of travling using that path
        """
        total_distance = 0
        path = [city.city_name]

        while city.previous_city != None:
            previous_city = city.previous_city
            total_distance += self.distances[city.city_name][previous_city.city_name]
            path.append(previous_city.city_name)
            city = previous_city

        total_distance = round(total_distance, 2)
        total_time = round(total_distance / self.AVERAGE_SPEED, 2)
        total_cost = round(total_distance * self.LITER_USAGE, 2)
        return path[::-1], total_distance, total_time, total_cost

    def get_adjacents(self, city: str) -> list:
        """
        :param: city: a city name 
        :return: a list of cities sorted from nearest to farthest from city A
        """
        adjacents = self.distances[city]

        try:
            adjacents.pop(city)
        except:
            pass

        adjacents = list(adjacents.items())
        adjacents = sorted(adjacents, key=lambda x: x[1])[:self.SIGHT]
        return adjacents

    def get_heuristic(self, A: str, B: str) -> float:
        """
        :param: A: the name of city A
        :param: B: the name of city B
        return: the cost between two cities using euclidean distance
        """
        A_location = self.locations[A]
        B_location = self.locations[B]
        cost = ((A_location[0] - B_location[0])**2 +
                (A_location[1] - B_location[1])**2)**0.5
        return cost

    def Astar(self) -> City:
        """
        A* search algorithm to find the goal with shortest path from the start point
        """
        self._load_files()
        self._verify_inputs()

        frontier = PriorityQueue()
        visited = set()
        starting_city = City(city_name=self.start,
                             cost=0,
                             previous_city=None)

        frontier.enqueue(starting_city)

        while not frontier.is_empty():
            city = frontier.dequeue()

            if self.goal == city.city_name:
                return self._get_result(city)

            adjacents = self.get_adjacents(city.city_name)

            for adjacent in adjacents:
                if adjacent[0] in visited:
                    continue
                cost = self.get_heuristic(adjacent[0], self.goal) + city.cost
                adjacent_city = City(adjacent[0], cost, city)
                frontier.enqueue(adjacent_city)

            visited.add(city.city_name)
        return None


if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        A, B = args[0].lower(), args[1].lower()
    else:
        exit(print("Please enter cities. Exmaple: `Python Aldammam Mecca`"))

    app = ShortestPath(A, B)
    path, km, time, cost = app.Astar()

    print("===============================================")
    print("The path from {} to {}:".format(A, B))
    for i, city in enumerate(path):
        if i != len(path)-1:
            print("{} --->".format(city), end=" ")
        else:
            print("{}".format(city))

    print("The total distance is {} KM".format(km))
    print("The total cost in Saudi Riyal is {} SAR".format(cost))
    print("The estimated time to reach {} from {} is {} hours".format(A, B, time))
    print("===============================================")
