"""Elevator simulation"""

from random import randint

class Building(object):
    '''Initialiser for the Building Class.  Contains number of floors in the building and 
    list for number of customers in the Building.  Elevator created from the Elevator Class
    '''
    def __init__ (self, num_floors, customers_for_boarding_list):        
        self.num_floors = num_floors
        self.boarding = customers_for_boarding_list
        self.elevator = Elevator(self, num_floors)

    def run(self, elevator):
        '''accept any passengers waiting at this floor from the building boarding_list
        goes onto the (Elevator) Passenger List - Embarking
        '''
        while self.elevator.passenger_list or  self.boarding:
            elevator.embarking_customer()
            elevator.disembarking_customer()
           
            elevator.move()
    
        if len(self.boarding) == len(self.elevator.passenger_list):
            print('\nNo more customers on Board.  All Customers taken care of.  \n\nThank you for using DT249 Elevators.')
            #customer.output()

class Elevator(object):
    
    def __init__(self, num_floors, customers_for_boarding_list):
        '''
        Initialiser for the Elevator Class.  Contains number of floors the Elevator has to travel and  
        a list for number of customers about to Board the Elevator and a list for Passengers in the Elevator.
        '''        
        self.floors = num_floors
        self.passenger_list = []
        self.customers_for_boarding_list = customers_for_boarding_list
        self.current_floor = 0
        self.embarked_customer = 0
        self.disembarked_customer = 0
        self.direction = 'up'

    #customer moves from customers_for_boarding_list and embarks onto (Elevator)passenger_list
    def embarking_customer(self):
        for customer in self.customers_for_boarding_list:
            if customer.starting_floor == self.current_floor:
                self.passenger_list.append(customer)
                self.customers_for_boarding_list.remove(customer)
                self.embarked_customer += 1
                print('Customer Alighting . . . Doors Open ... ')
                print("Customer with ID: {}".format(customer.ID) + " gets on at floor {}".format(customer.starting_floor))
                # + "& presses the button for floor:"item.ending_floor)
                print('... Customer embarked ...')
                print('... Doors Close ...')

    #customer exits lift and is removed from (Elevator)passenger_list
    def disembarking_customer(self):
        for customer in self.passenger_list:
            if customer.ending_floor == self.current_floor:
                self.passenger_list.remove(customer)
                self.disembarked_customer += 1
                print('Customer Disembarking . . . Doors Open ...')
                print("Customer with ID: {}".format(customer.ID) + " gets off at floor {}".format(customer.ending_floor))
                print('... Customer disembarked ...')
                print('... Doors Close ...')


    #elevator moves one floor at a time, 
    def move(self):
    
        print('Elevator is on floor {}'.format(self.current_floor))
        '''Move Elevator one floor at a time'''
        #if self.direction == 'up' and self.current_floor != self.floors:
                #self.current_floor += 1
        
        if self.current_floor != self.floors and self.direction == 'up':
            self.current_floor += 1
            print('Elevator moving up one floor')
            print('\nCurrent floor {}'.format(self.current_floor))
        if self.current_floor != 1 and self.direction == 'down':
            self.current_floor-=1
            print('Elevator moving down one floor')
            print('\nCurrent floor {}'.format(self.current_floor))
        if self.current_floor == self.floors:
            self.direction = 'down'
        if self.current_floor == 1:
            self.direction = 'up'

    
class Customer(object):
    '''Initialiser for the Customer Class.  Contains Starting floor for Custoemr and ending floor for the Customer, and an ID.
    '''  
    def __init__(self, ID, starting_floor, ending_floor):
        self.ID = ID
        self.starting_floor = starting_floor
        self.ending_floor = ending_floor
    
    def __str__(self):
        return ("Customer with ID: {}".format(self.ID) + " boarded on floor {}".format(self.starting_floor) + " and alighted at floor {}".format(self.ending_floor))

    def __repr__(self):
        return ('{},{},{}'.format(self.ID, self.starting_floor, self.ending_floor))
    
    def output(self):
        print("Customer with ID: {}".format(self.ID) + " starts on floor {}".format(self.starting_floor) + " and gets off at floor {}".format(self.ending_floor))
        return    
    
def main():
    # Prompts user for number of floors for the Building and a number or prospective customers for the Elevator.
    # Also catches user input for 0 floors (Hotel cannot have zero floors)
    while True:
        try:
            floor_amount = int(input("Please enter the number of floors in the Building: "))
            num_customers = int(input("Please enter the number of customers in the Building:"))
            if floor_amount == int(0):
                raise ValueError
        except:
            print("Please enter an integer greater than zero")
        else:
            break

    boarding_list = []

    cust_id = 0
    for customer in range(0, num_customers):
        customer = Customer(starting_floor=randint(1, floor_amount), ending_floor=randint(1, floor_amount), ID = cust_id)
        customer.output()
        boarding_list.append(customer)
        cust_id += 1
        
    print('\nCustomers in List format: {}\n'.format(boarding_list))
        
    building = Building(floor_amount, boarding_list)
    elevator=Elevator(floor_amount, boarding_list)
    building.run(elevator)

if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod(extraglobs={'e': Elevator(3, 3)})