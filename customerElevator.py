import random

class Customer(object):
    print("in Customer")
    def __init__(self, ID, num_floors, destination_floor=0, starting_floor=0, in_elevator=0, finished=0):
        self.ID = random.randint(1, num_customers)
        self.starting_floor = random.randint(1, num_floors)                          # Customer waits at a random floor
        #self.on_floor = current_floor
        self.destination_floor = random.randint(1, num_floors)                      # Customers floor selection is random
        
    def __str__(self):
        return "The customer with ID {}, got on at {}, and alighted at {}".format( self.ID, self.starting_floor, self.destination_floor)

num_customers = int(input("Please enter the number of customers: "))

customer_list = []

while len(customer_list) > 0:
    customer_list.append(Customer(object))
    print (customer_list)
    customer_list -= 1