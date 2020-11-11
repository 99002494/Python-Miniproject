import csv
from data import *
        
d1 = data()
with open('satellite.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for i in range(len(row)):
            name = row[0]
            operator = row[1]
            user = row[2]
            purpose = row[3]
            OrbitClass = row[4]
            OrbitType = row[5]
            perigee = row[6]
            apogee = row[7]
            eccentricity = row[8]
            inclination = row[9]
            LaunchMass = row[10]
            LaunchYear = row[11]
            LifeTime = row[12]
            LaunchSite = row[13]
            LaunchVehicle = row[14]        
    
        d1.add_satellite(OrbitClass,OrbitType,LifeTime,purpose,LaunchVehicle, LaunchSite, LaunchYear, LaunchMass,perigee,apogee,eccentricity,inclination,name,operator,user)

print("Details Class Functions:")
print("Total number of elements:", d1.count_elements())    
print("Remove element by name:", d1.remove_by_name('1HOPSAT')) 
print("Count after removing:", d1.count_elements())  
print("Number of satellites for communication purpose:", d1.count_by_purpose('Communications'))
print("Max lifetime of satellite:", d1.max_lifetime())
print("Number of satellites of elliptical orbit:",  d1.all_satellites_by_OrbitType('Elliptical'))
print("No. of satellites between life range:", d1.count_bw_life_range(2,10))
print("\n")


