"""
Function which will return relavent data for different api types
"""
def get_country_data():
    return {
        "name": "Iran",
        "population": "50000",
        "area": 2500,
        "no_of_hospital": 10,
        "no_of_nationalparks": 10,
        "no_of_rivers": 10,
        "no_of_schools": 10,
        "continent_id" : 1
    }

def get_continent_data():
    return {
        "name": "Australia",
        "population": "400000",
        "area": 40000
    }

def get_city_data():
    return {
        "name": "Pune",
        "population": "50000",
        "area": 2500,
        "no_of_roads": 10,
        "no_of_trees": 10,
        "no_of_shops": 10,
        "no_of_schools": 5,
        "country_id" : 1
    }
