class rocky:
    classVar1= False
    classVar2= "ON"
    @classmethod
    def rockybhai(cls):
        cls.classVar1=True
        cls.classVar2="OFF"
rocky.rockybhai()
print(rocky.classVar1)
#########################333
class car:
    def _init_(self,color,max_speed,acceleration,tyre_friction,start_engine,current_speed):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.start_engine=start_engine
        self.current_speed=current_speed
    def start_engine(self,engine):
        self.engine=engine
        print(self.engine)
        print("the car engine is turned on")
    def stop_engine(self,engine):
        self.engine=engine
        print(self.engine)
        print("the car engine is turned off")
    def appl=






