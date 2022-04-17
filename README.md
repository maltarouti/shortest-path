# Shortest Path 🎯

![image](https://user-images.githubusercontent.com/63660298/163285108-fd875cb8-3c8a-4f9e-931a-54072a93ef09.png)

# Introduction 📗

Nowadays, we frequently use a web mapping application to find the shortest path between our location and the destination. It saves us a lot of time and makes everything much easier, especially when you're new to the place. In this project, I will aim to create a little system in Python using the A* search method to find the shortest path between any two Saudi cities. Please keep in mind that the program may not be perfectly right, so please use Google Maps instead 😉

# Algorithm 🧮

I used the A* search algorithm in this project, which is an efficient informed algorithm that avoids expanding the expensive solution by utilizing the heuristic function. The heuristic function is essentially a euclidean distance computation from the present state to the goal, allowing us to identify the quickest path possible.


# Sample run 🏃

This secion contains a sample run for A* algorthim finding the shortest path between two cities in Saudi Arabia, and calculate the time and cost in Riyal (SAR) based on the current gas price.

* The shortest path between Aldammam and Riyadh
```
$ python3 ShortestPath.py Aldammam Riyadh

The shortest path from Aldammam to Riyadh:
Aldammam ---> Umalerrad ---> Rumah ---> Riyadh
The total distance is 435.43 KM
The total cost in Saudi Riyal is 59.33 SAR
The estimated time to reach Riyadh from Aldammam is 3.96 hours
```


* The shortest path between Mecca and Abha
```
$ python3 ShortestPath.py mecca abha

The shortest path from Mecca to Abha:
Mecca ---> Hajrah ---> Almakhwah ---> Alardiyat ---> Tanumah ---> Tabab ---> Abha
The total distance is 458.18 KM
The total cost in Saudi Riyal is 62.43 SAR
The estimated time to reach Abha from Mecca is 4.17 hours

```

# Files 📁
```
.
├── cities_distance.txt | The distance between each city in Saudi Arabia
├── cities_location.txt | longitude and latitude of Saudi Arabia cities
├── City.py             | The city class
├── PriorityQueue.py    | A priority Queue data structure
├── README.md
└── ShortestPath.py     | The main program
```

# Conclusion ✅

In this project, we implemented A* search algorithm to find the shortest path, distance, cost in Riyal and the estimated time to reach the distanation. This program is not perfect so feel free to fork and work on improving it. You also can run the program on another country by changing the text files.
