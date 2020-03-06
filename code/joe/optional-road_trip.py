# Lab : Road Trip
# Author : Joe

# city_to_accessible_cities = {
#   "Boston": {"New York", "Albany", "Portland"},
#   "New York": {"Boston", "Albany", "Philadelphia"},
#   "Albany": {"Boston", "New York", "Portland"},
#   "Portland": {"Boston", "Albany"},
#   "Philadelphia": {"New York"}
# }

cities = {
  "Boston": {"New York": 4, "Albany": 6, "Portland": 3},
  "New York": {"Boston": 4, "Albany": 5, "Philadelphia": 9},
  "Albany": {"Boston": 6, "New York": 5, "Portland": 7},
  "Portland": {"Boston": 3, "Albany": 7},
  "Philadelphia": {"New York": 9},
}


user_city = input("Enter city: ")
while user_city not in cities:
    user_city = input("Not a recognized city, please try again: ")

while True:
    try:
        num_hops = int(input("Enter number of hops: "))
        if num_hops > 0:
            break
    except ValueError:
        pass
    print("Must enter an integer greater than 0!")


# Recursive function to handle a dynamic number of hops
hops = dict() #hops are {city_name: total_travel_time, ...}
def findHops(city, num, time):
    if num < 1:
        return
    for n in cities[city]:
        #only record a hop if it doesn't exist or if travel time is reduced (and never record a hop to the origin city)
        if (n not in hops or hops[n] > time + cities[city][n]) and n != user_city:
            hops[n] = time + cities[city][n]
            findHops(n, num-1, hops[n])
    
findHops(user_city, num_hops, 0)

print(f"\nTravel times to cities from {user_city} in {num_hops} hops or less:")
for n in hops:
    print(f"\t-{n}:\t{hops[n]}")
    

# Version 1
# print(f"\nCities connected to {user_city}:")
# for n in city_to_accessible_cities[user_city]:
#     print(f"\t-{n}")

# two_hop = []

# for n in city_to_accessible_cities[user_city]:
#     for m in city_to_accessible_cities[n]:
#         if m not in city_to_accessible_cities[user_city] and m not in two_hop and m != user_city:
#             two_hop.append(m)

# print(f"\nCities within two hops of {user_city}:")
# for n in two_hop:
#     print(f"\t-{n}")

# Version 2