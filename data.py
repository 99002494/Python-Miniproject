# changed so and so details user name and email
from classes import * 

class data():

    def __init__(self):
        self.info = []
    
    def add_satellite(self,OrbitClass,OrbitType,LifeTime,Purpose,LaunchVehicle, LaunchSite, LaunchYear, LaunchMass,perigee,apogee,eccentricity,inclination,Name,Operator,User):
        s1 = Satellite(OrbitClass,OrbitType,LifeTime,Purpose,LaunchVehicle, LaunchSite, LaunchYear, LaunchMass,perigee,apogee,eccentricity,inclination,Name,Operator,User)
        self.info.append(s1)
    
    def remove_by_name(self,name):
        x=0
        for obj in self.info:
            if obj.Name==name:
                index = self.info.index(obj)
                var = self.info.pop(index)
                x = var.Name
        return x

   
    def count_elements(self):
        return len(self.info)

  
    def display(self):
        for element in self.info:
            print(element.Name,element.Purpose)

#Details class related functions

    def count_by_purpose(self,purpose):
        count = 0
        for obj in self.info:
            if obj.Purpose == purpose:
                count = count + 1
        return count

    def max_lifetime(self):
        max = 0.0
        for obj in self.info:
            x = float(obj.LifeTime)
            if(max < x):
                max = x
        return max

    def all_satellites_by_OrbitType(self,Type):
        sats = []
        for obj in self.info:
            if obj.OrbitType == Type:
                sats.append(obj.Name)
        return sats

    def count_by_user_operator(self,user,operator):
        count=0
        for obj in self.info:
            if obj.User==user and obj.Operator==operator:
                count = count+1
        return count

    def count_bw_life_range(self,min,max):
        count=0
        for obj in self.info:
            x = float(obj.LifeTime)
            if x>min and x<max:
                count = count+1
        return count
    # Launch Class related functions
    def highest_mass(self):
        max_mass=0
        for obj in self.info:
            a = int(obj.LaunchMass)
            if(max_mass < a): 
                max_mass = a
        return max_mass

    def lowest_mass(self):
        min_mass=1
        for obj in self.info:
            if(min_mass > int(obj.LaunchMass)):
               min_mass = int(obj.LaunchMass)
        return min_mass

    def average_mass(self):
        sum_mass = 0
        avg_mass = 0
        count = len(self.info)
        for obj in self.info:
            sum_mass = sum_mass + int(obj.LaunchMass)
        avg_mass = int((sum_mass)/count)
        return avg_mass

    def total_satellites_in_year(self, year):
        count = 0
        for obj in self.info:
            if int(obj.LaunchYear) == year:
                count = count+1
        return count

    def number_of_satellites_by_vehicle(self, vehicle):
        count = 0
        for obj in self.info:
            if obj.LaunchVehicle == vehicle:
                count = count+1
        return count

    def number_of_satellites_bw_years_range(self,min,max):
        count=0
        for obj in self.info:
            if int(obj.LaunchYear)>min and int(obj.LaunchYear)<max:
                count = count+1
        return count
    
    #orbit class related functions

    def MaxPerigee(self):
        max_p = 0
        for i in self.info:
            m = int(i.perigee)
            if(max_p < m):
                max_p = m
        return max_p

    def MinPerigee(self):
        min_p = 0
        for i in self.info:
            n = int(i.perigee)
            if(min_p > n):
                min_p = n
        return min_p

    def AvgPerigee(self):
        sum_perigee = 0
        avg_perigee = 0
        cnt=len(self.info)
        for i in self.info:
            sum_perigee = sum_perigee + int(i.perigee)
            avg_perigee = int((sum_perigee)/cnt)
        return int(avg_perigee)

    def MaxApogee(self):
        max = 0.0
        for i in self.info:
            m = int(i.apogee)
            if(max < m):
                max = m
        return max

    def MinApogee(self):
        min = 0
        for i in self.info:
            m = int(i.apogee)
            if(min > m):
                min = m
        return min

    def AvgApogee(self):
        sum_apogee = 0
        avg_apogee = 0
        cnt=len(self.info)
        for i in self.info:
            sum_apogee = sum_apogee + int(i.apogee)
            avg_apogee = sum_apogee/cnt
        return int(avg_apogee)

    def AvgEcentricity(self):
        sum_e = 0
        avg_e = 0
        cnt=len(self.info)
        for i in self.info:
            sum_e = sum_e + float(i.eccentricity)
            avg_e = sum_e/cnt
        return round(avg_e)

    def AvgInclination(self):   
        sum_i = 0
        avg_i = 0
        cnt=len(self.info)
        for j in self.info:
            sum_i = sum_i + float(j.inclination)
            avg_i = sum_i/cnt
        return round(avg_i)
