import unittest
import csv
from data import *

class TESTS(unittest.TestCase):

    def setUp(self):
        self.d1 = data()
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
                self.d1.add_satellite(OrbitClass,OrbitType,LifeTime,purpose,LaunchVehicle, LaunchSite, LaunchYear, LaunchMass,perigee,apogee,eccentricity,inclination, name,operator,user)
    
    def test_count(self):
        self.assertEqual(285,self.d1.count_elements())

    def test_remove(self):
        self.assertEqual('1HOPSAT',self.d1.remove_by_name('1HOPSAT'))
    
    def test_by_purpose(self):
        self.assertEqual(91,self.d1.count_by_purpose('Communications'))
    
    def test_max_lifetime(self):
        self.assertEqual(25,self.d1.max_lifetime())

    def test_by_orbit_type(self):
        l = self.d1.all_satellites_by_OrbitType('Elliptical')
        self.assertEqual(5,len(l))

    def test_bw_liferange(self):
        self.assertEqual(197,self.d1.count_bw_life_range(2,10))
    
    def test_highest_mass(self):
        self.assertEqual(18000,self.d1.highest_mass())

    def test_lowest_mass(self):
        self.assertEqual(1,self.d1.lowest_mass())
    
    def test_average_mass(self):
        self.assertEqual(1323,self.d1.average_mass())
    
    def test_total_satellites_in_year(self):
        self.assertEqual(14,self.d1.total_satellites_in_year(2010))

    def test_number_of_satellites_launched_by_vehicle(self):
        self.assertEqual(27,self.d1.number_of_satellites_by_vehicle('PSLV'))

    def test_bw_years_range(self):
        self.assertEqual(122,self.d1. number_of_satellites_bw_years_range(2005,2015))
        
    def test_max_perigee(self):
        self.assertEqual(23783,self.d1.MaxPerigee())

    def test_min_perigee(self):
        self.assertEqual(0,self.d1.MinPerigee())

    def test_avg_perigee(self):
        self.assertEqual(1314,self.d1.AvgPerigee())

    def test_max_apogee(self):
        self.assertEqual(330000,self.d1.MaxApogee())

    def test_min_apogee(self):
        self.assertEqual(0,self.d1.MinApogee())

    def test_avg_apogee(self):
        self.assertEqual(6089,self.d1.AvgApogee())

    def test_avg_eccentricity(self):
        self.assertEqual(2,self.d1.AvgEcentricity())
    
    def test_avg_inclination(self):
        self.assertEqual(79,self.d1.AvgInclination())  

if __name__ == '__main__':
    unittest.main()