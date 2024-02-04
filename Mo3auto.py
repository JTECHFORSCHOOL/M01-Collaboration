class Automobile:
    def __init__(self):
        self.year = "000"
        self.make = "not found"
        self.model = "nope"
        self.doors = "not given"
        self.roof = "no"

    def input(self):
        self.year = str(input("the year the car was made"))
        self.make = str(input("the make of the car"))
        self.model = str(input("the model of the car"))
        self.doors = str(input("the admount of doors the car was made with(2 for two door,4 for four doors)"))
        self.roof = str(input("the roof the car has(0 for no sunroof, 1 for a sun roof)"))
        checking = True
        while checking == True:
            if self.roof == "0":
                self.roof = "no sunroof"
            elif self.roof == "1":
                self.roof = "sunroof"
            else:
                print("error")
                break
        
            if self.doors == "2":
                self.roof = "2 doors"
                checking = False
            elif self.roof == "4":
                self.roof = "4 doors"
                checking = False
            else:
                print("error")
                break
        print("you have a "+ self.model+ " car made in the year "+ self.year+" that has a make of "+ self.make+ " with "+ self.doors+ " doors and "+self.roof)



car = Automobile()
car.input()
