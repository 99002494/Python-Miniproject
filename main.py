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

print("Launch Class Functions:")
print("Highest mass is:",d1.highest_mass())
print("Lowest mass is:", d1.lowest_mass())
print("Average mass is:", d1.average_mass())
print("Total number of satellites in 2010 is:", d1.total_satellites_in_year(2010))
print("Number of satellites launched by PSLV are:", d1.number_of_satellites_by_vehicle('PSLV'))
print("Total satellites launched between 2005 to 2015:",d1. number_of_satellites_bw_years_range(2005,2015))
print("\n")

print("Orbit Class Functions:")
print("max Perigee:", d1.MaxPerigee())
print("min Perigee:", d1.MinPerigee())
print("Avg Perigee:", d1.AvgPerigee())
print("max Apogee:", d1.MaxApogee())
print("min Apogee:", d1.MinApogee())
print("Avg Apogee:", d1.AvgApogee())
print("Avg Ecentricity:", d1.AvgEcentricity())
print("Avg Inclination:", d1.AvgInclination())
