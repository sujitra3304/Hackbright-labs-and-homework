def paid_status():

    melon_cost= 1.0

    data = open("customer-orders.txt")
    for line in data:
        line = line.rstrip() 
        values = line.split('|')
        # print (values)
    

        customer_name = values[1]
        melon_quantity = values[2]
        melon_quantity = float(melon_quantity)
        customer_paid = values[3]
        customer_paid = float(customer_paid)

        customer_expected = melon_quantity * melon_cost
        if customer_expected != customer_paid:
             print(f"{customer_name} paid ${customer_paid:.2f},",
                   f"expected ${customer_expected:.2f}")

paid_status()

