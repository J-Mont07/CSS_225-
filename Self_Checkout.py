#Juan Montoya

#October 15, 2020

#This program will allow the customer to look at what we have at the store for the day.
#They will decide on what to buy
#The program will give them the total amount they have to pay.

#Starts of by printing a welcome sentence.

print ("Welcome to Authentic SheepRecords")

#Asks for the user to input there name.

user = input ("Can I get your name? ")

#Greets user.

print ("Hello, " + user + "!")

#Prints the items in stock.

print ("Here's a list of what we have in stock for today: ")

#Prints the items with the price tag.

print ("Pink Floyd: $40")

print ("Hellripper: $20")

print ("Bathory: $30"  + "!\nsleeves: $1")

#Asks the user for the quantities of the items listed.

print ("How many records do you want?")

a = int (input ("Pink Floyd: "))

b = int (input ("Hellripper: "))

c = int (input ("Bathory: "))

d = int (input ("Record sleeves: "))

#The function that will calculate the quantites of each product.
#Adds them all together and returns the value.
def product_total (a, b, c, d) :
    a = a * 40

    b = b * 20

    c = c * 30
    
    d = d * 1
    
    t = a + b + c + d

    return t

print ("Great choice " + user + "!" + "\nYour total will be: ")

#prints the total amount owed

print (product_total (a, b, c, d))

#function for checking customer money.

def check_ammount (product_total, customer_money):
    if product_total >= customer_money:
        print ("There was a problem prossesing your order...")
        return False

    elif product_total <= customer_money:
        print ("Thank you for shopping at Authentic SheepRecords! " + "Where you will get the baaaast deals. \nHAVE A GREAT DAY")
        return True

#Payment that is being processed
payment = check_ammount(91, 100)
print (payment)


