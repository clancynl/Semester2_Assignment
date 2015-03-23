from random import randint

class Building(object):
    def __init__ (self, num_floors, customers_for_boarding_list):        
        self.num_floors = num_floors
        self.boarding = customers_for_boarding_list
        self.elevator = Elevator(self, num_floors)

    def run(self, elevator):
        while self.elevator.passenger_list or  self.boarding:
            '''accept any passengers waiting at this floor from the building boarding_list
            goes onto the (Elevator) Passenger List - Embarking'''
            elevator.embarking_customer()
            #print('Customer Embarked')
            #Allow customers off if required floor matches that in Passenger List - 
            elevator.disembarking_customer()
            #print('Customer Disembarked')
           
            elevator.move()
    
        if len(self.boarding) == len(self.elevator.passenger_list):
            print('\nNo more customers on Board.  All Customers taken care of.  \n\nThank you for using DT249 Elevators.')
            #customer.output()

class Elevator(object):
    def __init__(self, num_floors, customers_for_boarding_list):
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
                print("Customer with ID: {}".format(customer.ID) + " gets on at floor {}".format(customer.starting_floor-1))
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

#elevator moves one floor at a time
    def move(self):
        print('Elevator is on floor {}'.format(self.current_floor))
        '''Move Elevator one floor at a time'''
        if self.direction == 'up' and self.current_floor == self.floors:
                self.direction = 'down'
        else:
            self.direction = 'up'

        if self.current_floor != self.floors:
            self.current_floor += 1
            print('Elevator moving up one floor')
            print('\nCurrent floor {}'.format(self.current_floor))
        elif self.direction == 'down':
            self.current_floor-=1
            print('Elevator moving down one floor')
            print('\nCurrent floor {}'.format(self.current_floor))
        if self.current_floor == 0:
            self.direction = 'up'

    #def doors_open(self):
        #let out any passengers who are at their destination floor
        #for customer in self.passenger_list:
            #if self.current_floor == customer.ending_floor:
                #self.disembarking_customer(customer)
                #print("Customer with ID: {}".format(customer.ID) + " gets off at floor {}".format(customer.ending_floor))
                #print('Customer disembarked')
        #for cust in self.passenger_list:
            #if cust.ending_floor == self.current_floor:
                #self.passenger_list.remove(cust)
                #print('Customer {}'.format(cust))
        
    #def doors_open_embarking(self):
        #for customer in self.customers_for_boarding_list:
            #if self.current_floor == customer.starting_floor:
                #self.embarking_customer(customer)
                #self.customers_for_boarding_list.remove(customer)
                #print('Customer Embarked')
    
class Customer(object):
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

    while True:
        try:
            floor_amount = int(input("Please enter the number of floors in the Building: "))
            num_customers = int(input("Please enter the number of customers in the Building:"))
            if floor_amount == int(0):
                raise ValueError
        except:
            print("Please enter an integer greater than zero")              # Catches user input for 0 floors
        else:
            break

    boarding_list = []

    #building = Building(num_floors, boarding_list)
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