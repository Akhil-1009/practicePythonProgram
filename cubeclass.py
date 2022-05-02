from platformdirs import site_data_dir


class cube:
    def __init__(self,side):
        self.side=side
    def sur_area(self):         #suface area 
        return 6*self.side*self.side
    def lat_area(self):         # lateral surface area
        return 4*self.side*self.side
    def volume(self):           # volume 
        return self.side*self.side*self.side
s=int(input("enter the side of cube"))
cub1=cube(s)
print("area is",cub1.sur_area())
print("lateral surface area is",cub1.lat_area())
print("volume is ",cub1.volume())