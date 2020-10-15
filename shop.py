#shop.py


def check_money(total_cost, customer_money):
    if total_cost >= customer_money:
        print ("There was a problem prossesing your order...")
        return False

    elif total_cost <= customer_money:
        print ("Thank you for your purchase! \nHAVE A GREAT DAY!")
        return True


#This should print False
can_pay = check_money(107, 49)
print(can_pay)

#This should print True
can_pay = check_money(6, 88)
print(can_pay)
