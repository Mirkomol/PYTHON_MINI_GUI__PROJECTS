first_list = []
second_list = []


def add_data(number, patient_name, m_or_f, age, status,
             WBC, RBC, HGB, HCT):

    first_list.append((number, patient_name, m_or_f, age, status,
                       WBC, RBC, HGB, HCT))

    for item in first_list:
        for item2 in item:
            second_list.append(item2)
    # print("\nYou have added following datas\n")
    # print(second_list)

    if WBC < 4000 or WBC > 10000:
        print(
            "\n\033[91m {}\033[00m".format("\t\t\t\tWARNING!,YOUR WBC IS OUT OF NORMAL VALUE", "\n"))

    if m_or_f == "M":
        if RBC < 4.7 or RBC > 6.1:
            print("\n\033[91m {}\033[00m".format("\t\t\t\tWARNING!, YOU ARE MALE, AND YOUR RBC IS OUT OF NORMAL VALUE",
                                                 "\n"))
    elif m_or_f == "F":
        if RBC < 4.2 or RBC > 5.4:
            print("\n\033[91m {}\033[00m".format("\t\t\t\tWARNING!, YOU ARE FEMALE, AND YOUR RBC IS OUT OF NORMAL VALUE",
                                                 "\n"))

    if m_or_f == "M":
        if HGB < 13.5 or HGB > 17.5:
            print("\n\033[91m {}\033[00m".format("\t\t\t\tWARNING!, YOU ARE MALE, AND YOUR HGB IS OUT OF NORMAL VALUE",
                                                 "\n"))


    elif m_or_f == "F":
        if HGB < 12.5 or HGB > 15.5:
            print("\n\033[91m {}\033[00m".format("\t\t\t\tWARNING!, YOU ARE FEMALE, AND YOUR HGB IS OUT OF NORMAL VALUE" ,
                                                 "\n"))

    if m_or_f == "F":
        if HCT < 35 or HCT > 45:
            print("\n\033[91m {}\033[00m".format("\t\t\t\tWARNING!, YOU ARE FEMALE, AND YOUR HCT IS OUT OF NORMAL VALUE", "\n"))


    elif m_or_f == "M":
        if HCT < 39 or HCT > 50:
            print("\n\033[91m {}\033[00m".format("\t\t\t\tWARNING!, YOU ARE MALE, AND YOUR HCT IS OUT OF NORMAL VALUE", "\n"))


number = int(input("Enter Your Patient Number: (int) "))
full_name = input("Enter Your Full Name: (str) ")
gender= input("Your Gender (M/F): (str) ")
age = int(input("Your age: (int) "))
status = int(input("Your status: (int) "))
WBC = int(input("Your WBC: (int) "))
RBC = float(input("Your RBC: (float) "))
HGB = float(input("Your HGB: (float) "))
HCT = int(input("Your HCT: (int) "))
add_data(number, full_name, gender.upper(), age, status, WBC, RBC, HGB, HCT)



def scan_data(number):
    for data in second_list:
        if number == data:
            print("\n"f'\nHere is all Details for {number} number patient: \n')
            print(second_list)
            break
    else:
        print(f'No such {number} number patient in database')

prompt = int(input("\n""Enter Number of Patient to Scan, to see all details about: "))
scan_data(prompt)











