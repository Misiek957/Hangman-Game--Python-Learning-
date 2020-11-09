'''
We have a class defined for vehicles. Create two new vehicles called car1 and car2.
Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to
be a blue van named Jump worth $10,000.00.
'''

# define the Vehicle class
class Vehicle:
    
    def __init__(self,name,kind,color,value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here


car1 = Vehicle("Fer","convertible","red","60000.00")
car2 = Vehicle("Jump","van","blue","10000.00")

# test code
print(car1.description())
print(car2.description())