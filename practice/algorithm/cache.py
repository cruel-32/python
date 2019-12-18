import math

def getLRUTotalTime(cacheSize, cities):
    time = 0
    cachedCities = []

    for key in cities:
        if(key.lower() in cachedCities):
            time+=1
        else:
            time+=5
            cachedCities.append(key.lower())
            if(len(cachedCities) > cacheSize):
                cachedCities.pop(0)
    return time


print(
    getLRUTotalTime(3, [
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA",
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA"
    ])
)

print(
    getLRUTotalTime(3, [
        "Jeju",
        "Pangyo",
        "Seoul",
        "Jeju",
        "Pangyo",
        "Seoul",
        "Jeju",
        "Pangyo",
        "Seoul"
    ])
)

print(
    getLRUTotalTime(2, [
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA",
        "SanFrancisco",
        "Seoul",
        "Rome",
        "Paris",
        "Jeju",
        "NewYork",
        "Rome"
    ])
)

print(
    getLRUTotalTime(5, [
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA",
        "SanFrancisco",
        "Seoul",
        "Rome",
        "Paris",
        "Jeju",
        "NewYork",
        "Rome"
   ])
)

print(
    getLRUTotalTime(2, [
        "Jeju",
        "Pangyo",
        "NewYork",
        "newyork"
    ])
)

print(
    getLRUTotalTime(0, [
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA"
   ])
)


