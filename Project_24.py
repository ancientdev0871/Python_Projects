travel_log = [
  {
    "country": "India",
    "cities_visited": ["Mumbai", "Kolkata", "Kerela"],
    "total_visits": 17
  },  
  {
    "country": "USA",
    "cities_visited": ["San Francisco", "Las Vegas", "Connecticut", "New york"],
    "total_visits": 3
  },
]
def add_new_country(country,cities, visits):
    new_country =  {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)
add_new_country("Canada",["Vancouver", "Toronto"], 1)
print(travel_log)

