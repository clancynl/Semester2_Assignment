from random import randint

class Building(object):
    def __init__ (self, num_floors, customers_for_boarding_list):        
        self.num_floors = num_floors
        self.boarding = customers_for_boarding_list
        self.elevator = Elevator(self, num_floors)            

    def run(self, elevator):
        while self.elevator.customers_for_boarding_list and  self.elevator.passenger_list != 0:
            #accept any passengers waiting at this floor from the building boarding_list
            #goes onto the (Elevator) Passenger List
            for customer in self.boarding:
                if self.elevator.current_floor == customer.starting_floor:
                    self.elevator.embarking_customer()
                    print('Customer Embarked')
            #Allow customers off if required floor matches that in Passenger List
            for customer in self.elevator.passenger_list:
                self.elevator.doors_open(customer)
                print('Customer Disembarked')
           
            self.elevator.move()
    
        if len(self.boarding) == len(self.elevator.passenger_list):
            print('\nNo more customers on Board.  All Customers taken care of.  \n\nThank you ')
            #customer.output()

    #def cust_embark(self, customer):
        #self.boarding.remove(customer)


class Elevator(object):
    def __init__(self, num_floors, customers_for_boarding_list):
        self.num_floors = num_floors
        self.customers_for_boarding_list = customers_for_boarding_list
        self.passenger_list = []
        self.current_floor = 0
        self.alighted_customer = 0
        self.direction = 'up'

#customer moves from customers_for_boarding_list and embarks onto (Elevator)passenger_list
    def embarking_customer(self):
        for customer in self.customers_for_boarding_list:
            if customer.current_floor == self.current_floor:
                self.passenger_list.append(customer)
                self.customers.for_boarding_list.remove(customer)
                print('Customer', item.id, 'has embarked')


    def disembarking_customer(self):
        for customer in self.customers_for_boarding_list:
            if customer.ending_floor == self.current_floor:
                self.passenger_list.remove(customer)
                self.alighted_customer += 1
                print('Customer with ID: ', item.id,'has disembarked on floor:', item.ending_floor)


    def move(self):
        '''Move Elevator one floor at a time'''
        Elevator.embarking_customer(self)
        Elevator.disembarking_customer(self)
        if self.direction == 'up' and self.current_floor == self.num_floors:
                self.direction = 'down'
        else:
            self.direction = 'up'
            
        if self.current_floor != self.num_floors:
            self.current_floor += 1
            print('Elevator moving up one floor')
            print('\nCurrent floor {}'.format(self.current_floor))
        elif self.direction == 'down':
            self.current_floor-=1
            print('Elevator moving down one floor')
            print('\nCurrent floor {}'.format(self.current_floor))
        if self.current_floor == 0:
            self.direction = 'up'

    def doors_open(self):
        #let out any passengers who are at their destination floor
        for customer in self.passenger_list:
            if self.current_floor == customer.ending_floor:
                self.disembarking_customer(customer)
                print("Customer with ID: {}".format(customer.ID) + " gets off at floor {}".format(customer.ending_floor))
                print('Customer disembarked')
        #for cust in self.passenger_list:
            #if cust.ending_floor == self.current_floor:
                #self.passenger_list.remove(cust)
                #print('Customer {}'.format(cust))
        
    def doors_open_embarking(self):
        for customer in self.customers_for_boarding_list:
            if self.current_floor == customer.starting_floor:
                self.embarking_customer(customer)
                self.customers_for_boarding_list.remove(customer)
                print('Customer Embarked')
    
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
            num_floors = int(input("Please enter the number of floors in the Building: "))
            num_customers = int(input("Please enter the number of customers in the Building:"))
            if num_floors == int(0):
                raise ValueError
        except:
            print("Please enter an integer greater than zero")              # Catches user input for 0 floors)
        else:
            break

    boarding_list = []

    #building = Building(num_floors, boarding_list)

    for cust_id in range(num_customers):
        ID = cust_id+1
        customer = Customer(cust_id, starting_floor=randint(1, num_floors), ending_floor=randint(1, num_floors))
        customer.output()
        boarding_list.append(customer)
        
    print('\nCustomers in List format: {}\n'.format(boarding_list))
        

    elevator=Elevator(num_floors, boarding_list)
    building = Building(num_floors, boarding_list)
    building.run(elevator)


if __name__ == '__main__':
    main()