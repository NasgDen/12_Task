import json


def get_avg_temp(filename: str, city: str):
    avg_temp = 0
    data = {}
    average_temp = {}

    with open(filename, mode="r", encoding="utf-8") as file:
        temp_cities = json.load(file)

    for cities in temp_cities:
        if city in cities:
            avg_temp = round(sum(temp_cities.get(cities).values()) / len(temp_cities[cities]), 2)

    average_temp["Average temperature"] = avg_temp
    data[city] = average_temp

    with open(f"../data/{city}.json", mode="w", encoding="utf-8") as file:
        json.dump(data, file)


if __name__ == "__main__":
    get_avg_temp("../data/weather.json", "Moscow")
