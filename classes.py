class details:
    def __init__(self,OrbitClass,OrbitType,LifeTime,Purpose):
        self.OrbitClass = OrbitClass
        self.OrbitType = OrbitType
        self.LifeTime = LifeTime
        self.Purpose = Purpose

class Satellite(details,launch,orbit):
    def __init__(self,OrbitClass,OrbitType,LifeTime,Purpose,LaunchVehicle, LaunchSite, LaunchYear, LaunchMass,perigee,apogee,eccentricity,inclination,Name,Operator,User):
        details.__init__(self,OrbitClass,OrbitType,LifeTime,Purpose)
        launch.__init__(self, LaunchVehicle, LaunchSite, LaunchYear, LaunchMass)
        orbit.__init__(self,perigee,apogee,eccentricity,inclination)
        self.Name = Name
        self.Operator = Operator
        self.User = User
