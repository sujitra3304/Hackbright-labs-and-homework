

def melon_delivery_report(file_name, day_num):
    the_file = open(file_name)

    print(f'Day {day_num}')
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
        


        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

melon_delivery_report("um-deliveries-day-1.txt",1)
melon_delivery_report("um-deliveries-day-2.txt",2)
melon_delivery_report("um-deliveries-day-3.txt",3)
