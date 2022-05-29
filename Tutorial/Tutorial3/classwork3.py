'Zhang Junyan, 1129832'
'Lin Qingxin, 1098238'

# Define Person class:
class Person:
    
    # Person Attributes (Constructor function to initiate the variables)
    def __init__(self):
        # Name is string
        self.Name = ''
        # Below data is number
        self.Age = 0
        self.Weight = 0
        self.Height = 0
        
    # Input user data
    def input_person_data(self):
        # Input age as string value
        self.Name = input("\nPlease enter your name: ")
        # Input age as integer value
        self.Age = int(input("Please enter your age: "))
        # Input weight as float value
        self.Weight = float(input("Please enter your weight: "))
        # Input height as float value
        self.Height = float(input("Please enter your height: "))
        
    # Print user data
    def get_person_data(self):
        print("\nName of user is: ", self.Name)
        print("Age of user is: ", self.Age, "years old")
        print("Weight of user is: ", self.Weight, "kg")
        print("Height of user is: ", self.Height, "cm")
        
# Main method to run program
if __name__ == "__main__":
    # Create object and run
    person = Person()
    person.input_person_data()
    person.get_person_data()
    
    # Can still create object for other users
    person1 = Person()
    person1.input_person_data()
    person1.get_person_data()
