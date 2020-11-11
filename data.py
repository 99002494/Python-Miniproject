# changed so and so details
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
