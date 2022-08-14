log_file = open("um-server-01.txt")


def generate_sales_reports(log_file): # function to generate report. 
    for line in log_file:
        line = line.rstrip()
        day = line[0:3] # Day is taken from the first 3 characters. 
        if day == "Mon":  # Records of the day we want in the file. 
            print(line)


generate_sales_reports(log_file)
