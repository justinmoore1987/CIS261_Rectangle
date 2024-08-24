#Justin Moore -- CIS261 -- Rectangle

from dataclasses import dataclass
#This code tells the stsyem what to do with the information provided by the user.
@dataclass
class Rectangle:
    height: int
    width: int

    def getPerimeter(self):
        perimeter = self.height * 2 + self.width * 2
        return perimeter

    def getArea(self):
        area = self.height * self.width
        return area
    
    def getStr(self):
        s = ""
        w = "* " * self.width + "\n"
        s += w
        for i in range(self.height - 2):
            s += "* "
            s += "  " * (self.width - 2)
            s += "* \n"
        s += w
        return s

#This code is the order the system should run the code to the user to collect information.
#Ask the user at the end if they would like to continue and start the input over.
def main():
    print("Rectangle Calculator")
    print()

    again= "y"
    while again.lower() == "y":
        height = int(input("height:  "))
        width = int(input("Width:  "))

        rectangle = Rectangle(height, width)
        print("Perimeter:", rectangle.getPerimeter())
        print("Area:  ", rectangle.getArea())
        print(rectangle.getStr())

        again = input("Continue? (y/n): ").lower()
        print()

    print("Bye!")

if __name__ == "__main__":
    main()