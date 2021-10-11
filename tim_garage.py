class Garage():
    def __init__(self, avail_tix = [1,2,3,4,5,6,7,8,9,10], taken_tix = {}):
        self.avail_tix = avail_tix
        self.taken_tix = taken_tix

    def take_tix(self):
        if not self.avail_tix:
            print("Lot is currently full. Please try again later.")
        else:
            self.taken_tix[self.avail_tix[0]] = " "
            self.avail_tix.pop(0)
            print(f"Available: {self.avail_tix}")
            print(f"Taken: {self.taken_tix}")


    def leave_garage(self):
        response = input("What is your ticket number?")
        if int(response) in self.taken_tix:
            if self.taken_tix[int(response)] == " ":
                print("Please pay your ticket.")
                self.pay_tix()
            elif self.taken_tix[int(response)] == "Paid":
                print("You are free to go. See you tomorrow!")
                self.avail_tix.append(int(response))
                self.taken_tix.pop(int(response))
                print(f"Available: {self.avail_tix}")
                print(f"Taken: {self.taken_tix}")
        else:
            print("Invalid ticket number.")
    
    def pay_tix(self):
        response = input("What ticket would you like to pay?")
        if int(response) in self.taken_tix:
            if self.taken_tix[int(response)] == " ":
                payment = input("Type anything and press enter to swipe card: ")
                if payment == "":
                    print("Not a valid card. Please try again.")
                else:
                    self.taken_tix[int(response)] = "Paid"
                    print("Payment complete - thank you! Please leave and make room for others.")
                    print(f"Available: {self.avail_tix}")
                print(f"Taken: {self.taken_tix}")
        
    def park_car(self):
        while True:
            response = input("What would you like to do? Park, pay, or leave? Please process one item at a time.")
            if response.lower() == "park":
                self.take_tix()
            elif response.lower() == "pay":
                self.pay_tix()
            elif response.lower() == "leave":
                self.leave_garage()
            elif response.lower() == "quit":
                print("Thank you! See you tomorrow.")
                break
            else:
                print("I do not recognize that command. Please try again.")
            

def run_garage():
    my_garage = Garage()
    my_garage.park_car()

run_garage()