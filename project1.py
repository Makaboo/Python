import math

firstName = "Xiao" # add your first name
lastName = "Li" # add your last name
print("Name: " + firstName + " " + lastName)
print("CPS 3320 - Project 1")

def main():
    print("Welcome to my Graduate School Project")
    print("Menu")
    print("C1 - Montclair State University - Public") # Montclair State University - Public
    print("C2 - New Jersey Institute of Technology - Public") # New Jersey Institute of Technology - Public
    print("C3 - Rider University - Private") # Rider University - Private
    print("Q - Quit")
    done = False
    while not done:
        choice = input("Choice: ")
        if choice == "Q":
            print("Quit!")
            done = True

        elif choice == "C1":
            about1()

        elif choice == "C2":
            about2()

        elif choice == "C3":
            about3()

        else:
            print("Invalid Choice")

# define College 1 About Function
def about1():
    infile = open('about_Montclair.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)

    while True:
        gradSchool = int(input("Enter how many year do you think you will finish Grad School? " +
                           "Enter: "))
        student = input("Are you Part Time or Full Time? [Enter: PT/FT] : ").upper()
        if student == "PT":
            break
        elif student == "FT":
            break
        else:
            print("\nInvalid input.",
                "\nPlease enter 'PT' for Part Time | 'FT' for Full Time.")

    if student == "PT":
        done = False
        while not done:
            creditsFA = int(input("Enter the number of credits for Fall semester: "))
            creditsSP = int(input("Enter the number of credits for Spring semester: "))

            if creditsFA <= 6 and creditsSP <= 6:
                print("A = In-State\tB = Out-of-State\tC = International Student")
                student = input("Are you In-State or Out-of-State or International Students? ").upper()

                tuition_FA = Fall_C1(creditsFA, student)
                tuition_SP = Spring_C1(creditsSP, student)
                done = True
            else:
                print("One or both of the credits is greater than 6. Please try again.")

    elif student == "FT":
        done = False
        while not done:
            creditsFA = int(input("Enter the number of credits for Fall semester: "))
            creditsSP = int(input("Enter the number of credits for Spring semester: "))

            if (6 <= creditsFA <= 15) and (6 <= creditsSP <= 15):
                print("A = In-State\tB = Out-of-State\tC = International Student")
                student = input("Are you In-State or Out-of-State or International Students? ")

                tuition_FA = Fall_C1(creditsFA, student)
                tuition_SP = Spring_C1(creditsSP, student)
                done = True
            else:
                print("All full-time graduate students must register for a minimum of six (6) credits per semester,",
                    "\nwith a maximum of fifteen (15) credits allowed.")

    done = False
    while not done:
        print("\nA = On-Campus\tB = Off-Campus\tC = Commute")
        housing = input("Do you like to live On-Campus, Off-Campus, or Commute: ").upper()

        if housing == "A" or housing == "B" or housing == "C":
            houses = house_C1(housing)
            done = True
        else:
            print("Invalid input. Please enter A, B, or C.")

    mealPlan = input("\nChoice your Meal Plan [Enter: Unlimited or Block]" +
                     "\nOr Do you perfer eating out [Enter: Eating Out]" +
                     "\nOr Do you perfer eating your own food [Enter: My Food]" +
                     "\nEnter your choice: ").lower()
    if mealPlan == "unlimited" or mealPlan == "block" or mealPlan == "eating out" or mealPlan == "my food":
        mealPlan = traditionalHall_C1(mealPlan)

    total_C1(creditsFA, creditsSP, tuition_FA, tuition_SP, houses, mealPlan, gradSchool)

# define College 1 Tuition Function
def Fall_C1(creditFA, person):
    if person == "In-State" or person == "Out-of-State" or person == "A" or person == "B" or person == "a" or person == "b":
        TuitionPerCredit = 809.00
        FeesPerCredit = 31.93
        Total = TuitionPerCredit + FeesPerCredit
        TuitionFA = Total * creditFA
        print("Fall Semester Tuition Cost: $", TuitionFA)
        return TuitionFA

    elif person == "C" or person == "International" or person == "International Student":
        TuitionPerCredit = 905.00
        FeesPerCredit = 31.93
        Total = TuitionPerCredit + FeesPerCredit
        TuitionFA = Total * creditFA
        print("Fall Semester Tuition Cost: $", TuitionFA)
        return TuitionFA

    else:
        return None

def Spring_C1(creditSP, person):
    if person == "In-State" or person == "Out-of-State" or person == "A" or person == "B" or person == "a" or person == "b":
        TuitionPerCredit = 809.00
        FeesPerCredit = 31.93
        Total = TuitionPerCredit + FeesPerCredit
        TuitionSP = Total * creditSP
        print("Spring Semester Tuition Cost: $", TuitionSP)
        return TuitionSP

    elif person == "C" or person == "International" or person == "International Student":
        TuitionPerCredit = 905.00
        FeesPerCredit = 31.93
        Total = TuitionPerCredit + FeesPerCredit
        TuitionSP = Total * creditSP
        print("Spring Semester Tuition Cost: $", TuitionSP)
        return TuitionSP

    else:
        return None

# define College 1 Housing Function
def house_C1(campus):
    if campus == "A": # On Campus Cost
        infile = open('MontclairOnCampusHousing.txt', 'r')
        file_contents = infile.read()
        infile.close()
        print(file_contents)

        done = False
        while not done:
            option = int(input("Which building are you interested in living On Campus? "))

            if option == 1:
                room = input("Do you prefer a Single, Double, Triple, or Quad? ").lower()
                if room == "single":
                    room = "Single"
                    price = 5722.00
                    print("\nYou are currently living either in Blanton Hall, Bohn Hall, Freeman Hall, or Stone Hall.")
                    print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif room == "double":
                    room = "Double"
                    price = 4656.00
                    print("\nYou are currently living either in Blanton Hall, Bohn Hall, Freeman Hall, or Stone Hall.")
                    print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif room == "triple":
                    room = "Triple"
                    price = 3724.00
                    print("\nYou are currently living either in Blanton Hall, Bohn Hall, Freeman Hall, or Stone Hall.")
                    print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif room == "quad":
                    room = "Quad"
                    price = 4609.00
                    print("\nYou are currently living either in Blanton Hall, Bohn Hall, Freeman Hall, or Stone Hall.")
                    print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price
                else:
                    print("Invalid input. Please Try Again")

            elif option == 2:
                room = input("Do you prefer a Single or Double? ").lower()
                if room == "single":
                    room = "Single"
                    price = 6538.00
                    print("\nYou are currently living in The Heights.")
                    print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif room == "double":
                    room = "Double"
                    price = 5980.00
                    print("\nYou are currently living in The Heights.")
                    print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                else:
                    print("Invalid input. Please Try Again")

            elif option == 3:
                room = input("Do you prefer a Single, Double, or Triple? ").lower()
                if room == "single":
                    room = "Single"
                    price = 6288.00
                    print("\nYou are currently living in Frank Sinatra Hall.")
                    print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif room == "double":
                    room = "Double"
                    price = 5557.00
                    print("\nYou are currently living in Frank Sinatra Hall.")
                    print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif room == "triple":
                        room = "Triple"
                        price = 4218.00
                        print("\nYou are currently living in Frank Sinatra Hall.")
                        print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                else:
                    print("Invalid input. Please Try Again")

            elif option == 4:
                room = "Double"
                price == 5209.00
                print("\nYou are currently living in Hawk Crossings.")
                print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                done = True
                return price

            elif option == 5:
                room = input("Do you prefer a Single or Double? ").lower()
                if room == "single":
                    room = "Single"
                    price = 6411.00
                    print("\nYou are currently living in The Village.")
                    print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif room == "double":
                    room = "Double"
                    price = 5665.00
                    print("\nYou are currently living in The Village.")
                    print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price
                else:
                    print("Invalid input. Please Try Again")

            else:
                print("Invalid input. Please enter 1, 2, 3, 4, or 5 for the Building(s) you prefer to live On-Campus.")

    elif campus == "B":
        infile = open('MontclairOffCampusHousing.txt', 'r')
        file_contents = infile.read()
        infile.close()
        print(file_contents)

        done = False
        while not done:
            option = int(input("Which building are you interested in living Off Campus? "))
            if option == 1:
                address = "19 Bamford Ave, Hawthorne, NJ 07506"
                rent = 3750.00
                semester = rent * 3
                print("\nYou currently live in", address,
                          "Your rent is due every month, your cost is $", str(rent),
                          "Your rent per semester will cost you $", str(semester))
                done = True
                return semester

            elif option == 2:
                address = "16 Christie Avenue, Clifton, NJ 07011"
                rent = 3500.00
                semester = rent * 3
                print("\nYou currently live in", address,
                          "Your rent is due every month, your cost is $", str(rent),
                          "Your rent per semester will cost you $", str(semester))
                done = True
                return semester

            elif option == 3:
                address = "650 New Jersey 23, Wayne, NJ 07470"
                rent = 1150.00
                semester = rent * 3
                print("\nYou currently live in", address,
                          "Your rent is due every month, your cost is $", str(rent),
                          "Your rent per semester will cost you $", str(semester))
                done = True
                return semester

            elif option == 4:
                address = "543 Main Street, Little Falls, NJ 07424"
                rent = 900.00
                semester = rent * 3
                print("\nYou currently live in", address,
                          "Your rent is due every month, your cost is $", str(rent),
                          "Your rent per semester will cost you $", str(semester))
                done = True
                return semester

            elif option == 5:
                address = "19 Bamford Ave"
                rent = 1700.00
                semester = rent * 3
                print("\nYou currently live in", address,
                          "Your rent is due every month, your cost is $", str(rent),
                          "Your rent per semester will cost you $", str(semester))
                done = True
                return semester

    elif campus == "C":
        print("Student must have a permits valid from September 1st to May 31st.\n")
        infile = open('MontclairCommuter.txt', 'r')
        file_contents = infile.read()
        infile.close()
        print(file_contents)

        done = False
        while not done:

            permitType = input("Choice your Permit Type [Commuter or Resident NJ Transit Permit] : ").lower()
            if permitType == "commuter":
                payment = input("Do you want to buy a Full Year or Per Semester? [Enter: Full Year Or Fall Semester Or Spring Semester] : ").lower()
                if payment == "full year":
                    permitType = "Commuter"
                    fee = 25.00
                    price = 260.00 + float(fee)
                    print("You are a", permitType, "to Montclair University and a Full Year Permit cost $", str(price))
                    done = True
                    return price
                elif payment == "fall semester" or payment == "spring semester":
                    permitType = "Commuter"
                    fee = 25.00
                    price = 135.00 + float(fee)
                    print("You are a", permitType, "to Montclair University and a Per Semster Permit cost $", str(price))
                    done = True
                    return price
                else:
                    print("Invalid input. Please Try Again")

            elif permitType == "resident nj transit permit":
                permitType = "Resident NJ Transit Permit"
                price = 400.00
                print("You have a", permitType, "to Montclair University and the permit cost $", str(price))
                done = True

# define College 1 Meals Function
def traditionalHall_C1(meal):
    if meal == "block":
        plan = int(input("Enter either Block 125, Block 175, Block 210, or Block 220: [Enter: 125, 175, 210, 220] : "))
        if plan == 125:
            flex = int(input("Do you want $250 Flex Dollar or $500 Flex Dollar? [Enter: 250 or 500] : "))
            if flex == 250:
                rate = 2150.00
                print("Your Meal plan is 125 Block +$250 Flex Dollars",
                      "Each Semester will cost you $", rate,
                      "Description: 125 swipes/semester = approx. 8 meals/week")
                return rate
            elif flex == 500:
                rate = 2400.00
                print("Your Meal plan is 125 Block +$500 Flex Dollars",
                      "Each Semester will cost you $", rate,
                      "Description: 125 swipes/semester = approx. 8 meals/week")
                return rate

        elif plan == 175:
            flex = int(input("Do you want $250 Flex Dollar or $500 Flex Dollar? [Enter: 250 or 500] : "))
            if flex == 250:
                rate = 2415.00
                print("Your Meal plan is 175 Block +$250 Flex Dollars",
                      "\nEach Semester will cost you $", rate,
                      "\nDescription: 175 swipes/semester = approx. 11 meals/week")
                return rate
            elif flex == 500:
                rate = 2650.00
                print("Your Meal plan is 175 Block +$500 Flex Dollars",
                      "\nEach Semester will cost you $", rate,
                      "\nDescription: 175 swipes/semester = approx. 11 meals/week")
                return rate

        elif plan == 210:
            rate = 2700.00
            print("Your Meal plan is 210 Block +$500 Flex Dollars",
                      "\nEach Semester will cost you $", rate,
                      "\nDescription: 210 swipes/semester = approx. 13 meals/week")
            return rate

        elif plan == 220:
            rate = 2700.00
            print("Your Meal plan is 220 Block +$325 Flex Dollars",
                      "\nEach Semester will cost you $", rate,
                      "\nDescription: 220 swipes/semester = approx. 14 meals/week")
            return rate

    elif meal == "unlimited":
        rate = 2800.00
        print("Your Meal plan is Your Choice Unlimited +7 +$250 Flex Dollars",
                      "\nEach Semester will cost you $", rate,
                      "\nDescription: Unlimited AYCTE dining hall meals + 7 retail swipes per week + $250 flex dollars")
        return rate

    elif meal == "eating out":
        rate = 0
        print("You chose to eat out, Drive Safe and Enjoy your food")
        return rate

    elif meal == "my food":
        rate = 0
        print("Enjoy your food")
        return rate

# define College 1 Total Function
def total_C1(CFA, CSP, TFA, TSP, home, eat, year):
    print("\nFall Semester")
    print("Fall Credits:", CFA)
    print("Tuition: $", TFA)
    print("Housing: $", home)
    print("Meals: $", eat)
    fallTotal = TFA + home + eat
    print("Fall Total: $", fallTotal)

    print("\nSpring Semester")
    print("Fall Credits:", CSP)
    print("Tuition: $", TSP)
    print("Housing: $", home)
    print("Meals: $", eat)
    springTotal = TSP + home + eat
    print("Spring Total: $", springTotal)

    FullYr = fallTotal + springTotal
    print("\nAcademic Year Total will cost $", FullYr)

    total = FullYr * year
    print("\nIf it takes you", year, "years to receive Master Degree.",
          "\nEstimated Degree Total: $", total)

#-----------------------------------------------------------------------------------

# define College 2 About Function
def about2():
    infile = open('about_NJIT.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)

    while True:
        gradSchool = int(input("Enter how many year do you think you will finish Grad School? " +
                           "Enter: "))
        student = input("Are you Part Time or Full Time? [Enter: PT/FT] : ").upper()
        if student == "PT":
            break
        elif student == "FT":
            break
        else:
            print("\nInvalid input.",
                "\nPlease enter 'PT' for Part Time | 'FT' for Full Time.")

    if student == "PT":
        done = False
        while not done:
            creditsFA = int(input("Enter the number of credits for Fall semester: "))
            creditsSP = int(input("Enter the number of credits for Spring semester: "))

            if creditsFA <= 9 and creditsSP <= 9:
                print("A = In-State\tB = Out-of-State")
                student = input("Are you In-State or Out-of-State? ").upper()

                tuition_FA = Fall_C2(creditsFA, student)
                tuition_SP = Spring_C2(creditsSP, student)
                done = True
            else:
                print("One or both of the credits is greater than 9. Please try again.")

    elif student == "FT":
        done = False
        while not done:
            creditsFA = int(input("Enter the number of credits for Fall semester: "))
            creditsSP = int(input("Enter the number of credits for Spring semester: "))

            if (9 <= creditsFA <= 12) and (9 <= creditsSP <= 12):
                print("A = In-State\tB = Out-of-State")
                student = input("Are you In-State or Out-of-State? ")

                tuition_FA = Fall_C2(creditsFA, student)
                tuition_SP = Spring_C2(creditsSP, student)
                done = True
            else:
                print("All full-time graduate students must register for a minimum of six (9) credits per semester,",
                    "\nwith a maximum of fifteen (12) credits allowed.")

    done = False
    while not done:
        print("\nA = On-Campus\tB = Off-Campus\tC = Commute")
        housing = input("Do you like to live On-Campus, Off-Campus, or Commute: ").upper()

        if housing == "A" or housing == "B" or housing == "C":
            houses = house_C2(housing)
            done = True
        else:
            print("Invalid input. Please enter A, B, or C.")


    infile = open('NJITMealPlan.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)

    done = False
    while not done:
        mealPlan = input("\nChoice your Meal Plan between A to H" +
                        "\nOr Do you perfer Commuter Only Meal Plan. Enter: J" +
                        "\nOr Eat Out / My Food" +
                        "\nEnter your choice: ").lower()
        if mealPlan in ["a", "b", "c", "d", "e", "f", "g", "h", "j", "eat out", "my food" ]: # Using Array - necessary conditions
            mealPlan = traditionalHall_C2(mealPlan)
            done = True
            break
        else:
            print("Invalid Choice")


    total_C2(creditsFA, creditsSP, tuition_FA, tuition_SP, houses, mealPlan, gradSchool)

# define College 2 Tuition Function
def Fall_C2(creditFA, person):
    if creditFA <= 11:
        if person == "A":
            TuitionPerCredit = 1226.00
            FeesPerCredit = 199.00
            Total = TuitionPerCredit + FeesPerCredit
            TuitionFA = Total * creditFA
            print("Fall Semester Tuition Cost: $", TuitionFA)
            return TuitionFA

        elif person == "B":
            TuitionPerCredit = 1760.00
            FeesPerCredit = 199.00
            Total = TuitionPerCredit + FeesPerCredit
            TuitionFA = Total * creditFA
            print("Fall Semester Tuition Cost: $", TuitionFA)
            return TuitionFA

    elif creditFA >= 12:
        if person == "A":
            Tuition = 11267.00
            Fees = 1692.00
            Total = Tuition + Fees
            TuitionFA = Total
            print("Fall Semester Tuition Cost: $", TuitionFA)
            return TuitionFA

        elif person == "B":
            Tuition = 16659.00
            Fees = 1692.00
            Total = Tuition + Fees
            TuitionFA = Total
            print("Fall Semester Tuition Cost: $", TuitionFA)
            return TuitionFA

    else:
        return None

def Spring_C2(creditSP, person):
    if creditSP <= 11:
        if person == "A":
            TuitionPerCredit = 1226.00
            FeesPerCredit = 199.00
            Total = TuitionPerCredit + FeesPerCredit
            TuitionSP = Total * creditSP
            print("Spring Semester Tuition Cost: $", TuitionSP)
            return TuitionSP

        elif person == "B":
            TuitionPerCredit = 1760.00
            FeesPerCredit = 199.00
            Total = TuitionPerCredit + FeesPerCredit
            TuitionSP = Total * creditSP
            print("Spring Semester Tuition Cost: $", TuitionSP)
            return TuitionSP

    elif creditSP >= 12:
        if person == "A":
            Tuition = 11267.00
            Fees = 1692.00
            Total = Tuition + Fees
            TuitionSP = Total
            print("Spring Semester Tuition Cost: $", TuitionSP)
            return TuitionSP

        elif person == "B":
            Tuition = 16659.00
            Fees = 1692.00
            Total = Tuition + Fees
            TuitionSP = Total
            print("Spring Semester Tuition Cost: $", TuitionSP)
            return TuitionSP

    else:
        return None

# define College 2 Housing Function
def house_C2(campus):
        if campus == "A": # On Campus Cost
            infile = open('NJITOnCampusHousing.txt', 'r')
            file_contents = infile.read()
            infile.close()
            print(file_contents)

            done = False
            while not done:
                option = int(input("Which building are you interested in living On Campus? "))

                if option == 1:
                    room = input("Do you prefer a Double, Double P, Single S, or Single P? [P - Private Bath/ S - Shared Bath] : ").lower()
                    if room == "double":
                        room = "Double Room"
                        price = 4830.00
                        print("\nYou are currently living in Cypress Hall.")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "double p":
                        room = "Double Room, Private Bath"
                        price = 4950.00
                        print("\nYou are currently living in Cypress Hall.")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "single s":
                        room = "Single Room, Shared Bath"
                        price = 5650.00
                        print("\nYou are currently living in Cypress Hall.")
                        print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "single p":
                        room = "Single Room, Private Bath"
                        price = 6010.00
                        print("\nYou are currently living in Cypress Hall.")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    else:
                        print("Invalid input. Please Try Again")

                elif option == 2:
                    room = input("Do you prefer a Double, Double P, Single S, or Single P? [P - Private Bath/ S - Shared Bath] : ").lower()
                    if room == "double":
                        room = "Double Room"
                        price = 4960.00
                        print("\nYou are currently living in Martinson Residence Hall (Honors).")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "double p":
                        room = "Double Room, Private Bath"
                        price = 5090.00
                        print("\nYou are currently living in Martinson Residence Hall (Honors).")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "single s":
                        room = "Single Room, Shared Bath"
                        price = 5800.00
                        print("\nYou are currently living in Martinson Residence Hall (Honors).")
                        print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "single p":
                        room = "Single Room, Private Bath"
                        price = 6140.00
                        print("\nYou are currently living in Martinson Residence Hall (Honors).")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    else:
                        print("Invalid input. Please Try Again")

                elif option == 3:
                    room = input("Do you prefer a Double, Double P, C-Single S, Single S, or Single P? [P - Private Bath/ S - Shared Bath] : ").lower()
                    if room == "double":
                        room = "Double Room"
                        price = 4830.00
                        print("\nYou are currently living in Laurel Hall.")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "double p":
                        room = "Double Room, Private Bath"
                        price = 4950.00
                        print("\nYou are currently living in Laurel Hall.")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "c-single s":
                        room = "C Single Room, Shared Bath"
                        price = 5540.00
                        print("\nYou are currently living in Laurel Hall.")
                        print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "single s":
                        room = "Single Room, Shared Bath"
                        price = 5650.00
                        print("\nYou are currently living in Laurel Hall.")
                        print("Room for " + room + " (Per Resident) would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "single p":
                        room = "Single Room, Private Bath"
                        price = 6010.00
                        print("\nYou are currently living in Laurel Hall.")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    else:
                        print("Invalid input. Please Try Again")

                elif option == 4:
                    room = input("Do you prefer a Single or Double? ").lower()
                    if room == "single":
                        room = "Single Room"
                        price = 5310.00
                        print("\nYou are currently living in Redwood Hall.")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "double":
                        room = "Double Room"
                        price = 4620.00
                        print("\nYou are currently living in Redwood Hall.")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    else:
                        print("Invalid input. Please Try Again")

                elif option == 5:
                    room = input("Do you prefer a Double or Single S? ").lower()
                    if room == "double":
                        room = "Double Room"
                        price = 4830.00
                        print("\nYou are currently living in Oak Hall.")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "single s":
                        room = "Single Room, Shared Bath"
                        price = 5650.00
                        print("\nYou are currently living in Oak Hall.")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    else:
                        print("Invalid input. Please Try Again")

                elif option == 6:
                    room = input("Do you prefer a Rented or Owned? ").lower()
                    if room == "rented":
                        room = "Rented Units Double Room"
                        price = 4960.00
                        print("\nYou are currently living in Greek Village.")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    elif room == "owned":
                        room = "Owned Units Double Room"
                        price = 4830.00
                        print("\nYou are currently living in Greek Village.")
                        print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                        done = True
                        return price
                    else:
                        print("Invalid input. Please Try Again")

                else:
                    print("Invalid input. Please enter 1, 2, 3, 4, 5 or 6 for the Building(s) you prefer to live On-Campus.")

        elif campus == "B":
            infile = open('NJITOffCampusHousing.txt', 'r')
            file_contents = infile.read()
            infile.close()
            print(file_contents)

            room = int(input("Do you prefer a Studio (Private), 1BR/1BA (Double), 2BR/1BA (Private), 2BR/2BA (Double) or 4BR/2BA (Private)? " +
                         "\nEnter: 1, 2, 3, 4, or 5" +
                         "\nEnter: "))

            if room == 1:
                room = "Studio (Private)"
                price = 8660.00
                print("\nYou are currently living in Maple Hall Apartment.")
                print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                done = True
                return price

            elif room == 2:
                room = "1BR/1BA (Double)"
                price = 6740.00
                print("\nYou are currently living in Maple Hall Apartment.")
                print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                done = True
                return price

            elif room == 3:
                room = "2BR/1BA (Private)"
                price = 7280.00
                print("\nYou are currently living in Maple Hall Apartment.")
                print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                done = True
                return price

            elif room == 4:
                room = "2BR/2BA (Double)"
                price = 5930.00
                print("\nYou are currently living in Maple Hall Apartment.")
                print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                done = True
                return price

            elif room == 5:
                room = "4BR/2BA (Private)"
                price = 7190.00
                print("\nYou are currently living in Maple Hall Apartment.")
                print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                done = True
                return price

            else:
                print("Invalid input. Please Try Again")

        elif campus == "C":
            print("Student must have a permits valid from September 1st to May 31st.\n")
            infile = open('NJITCommuter.txt', 'r')
            file_contents = infile.read()
            infile.close()
            print(file_contents)

            payment = input("\nDo you want to buy a Full Time or Part Time? [Enter: FT/PT] : ").lower()
            if payment == "ft":
                permitType = "Full Time"
                price = 346.53
                print("You purchase a ", permitType, "Parking Permit for NJIT and the cost is $", str(price))
                return price

            elif payment == "pt":
                permitType = "Part Time"
                price = 194.06
                print("You purchase a ", permitType, "Parking Permit for NJIT and the cost is $", str(price))
                return price

# define College 2 Meals Function
def traditionalHall_C2(meal):
    if meal == "a":
        rate = 2223
        print("A Plan: $", rate)
        print("Continuous Unlimited Dining, 10 Guest entries; and $0 Tech Bucks")
        return rate

    elif meal == "b":
        rate = 2323
        print("B Plan: $", rate)
        print("Continuous Unlimited Dining, 10 Guest entries; and $100 Tech Bucks")
        return rate

    elif meal == "c":
        rate = 2424
        print("C Plan: $", rate)
        print("Continuous Unlimited Dining, 10 Guest entries; and and $200 Tech Bucks")
        return rate

    elif meal == "d":
        rate = 2623
        print("D Plan: $", rate)
        print("Continuous Unlimited Dining, 10 Guest entries; and and $400 Tech Bucks")
        return rate

    elif meal == "e":
        rate = 2823
        print("E Plan: $", rate)
        print("Continuous Unlimited Dining, 10 Guest entries; and $600 Tech Bucks")
        return rate

    elif meal == "f":
        rate = 1517
        print("F Plan: $", rate)
        print("80 Anytime Meals Per Semester, 10 guest entries; and $400 Tech Bucks")
        return rate

    elif meal == "g":
        rate = 1414
        print("G Plan: $", rate)
        print("$1,414 Tech Bucks")
        return rate

    elif meal == "h":
        rate = 1117
        print("H Plan: $", rate)
        print("80 Anytime Meals Per Semester, 10 guest entries; and $0 Tech Bucks")
        return rate

    elif meal == "j":
        rate = 873
        print("H Plan: $", rate)
        print("5 meals per week, Breakfast and/or Lunch entry")
        return rate

    elif meal == "eating out":
        rate = 0
        print("You chose to eat out, Drive Safe and Enjoy your food")
        return rate

    elif meal == "my food":
        rate = 0
        print("Enjoy your food")
        return rate

# define College 2 Total Function
def total_C2(CFA, CSP, TFA, TSP, home, eat, year):
    print("\nFall Semester")
    print("Fall Credits:", CFA)
    print("Tuition: $", TFA)
    print("Housing: $", home)
    print("Meals: $", eat)
    fallTotal = TFA + home + eat
    print("Fall Total: $", fallTotal)

    print("\nSpring Semester")
    print("Fall Credits:", CSP)
    print("Tuition: $", TSP)
    print("Housing: $", home)
    print("Meals: $", eat)
    springTotal = TSP + home + eat
    print("Spring Total: $", springTotal)

    FullYr = fallTotal + springTotal
    print("\nAcademic Year Total will cost $", FullYr)

    total = FullYr * year
    print("\nIf it takes you", year, "years to receive Master Degree.",
          "\nEstimated Degree Total: $", total)

#-----------------------------------------------------------------------------------

# define College 3 About Function
def about3():
    infile = open('about_Rider.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)

    while True:
        gradSchool = int(input("Enter how many year do you think you will finish Grad School? " +
                           "Enter: "))
        student = input("Are you Part Time or Full Time? [Enter: PT/FT] : ").upper()
        if student == "PT":
            break
        elif student == "FT":
            break
        else:
            print("\nInvalid input.",
                "\nPlease enter 'PT' for Part Time | 'FT' for Full Time.")

    if student == "PT":
        done = False
        while not done:
            creditsFA = int(input("Enter the number of credits for Fall semester: "))
            creditsSP = int(input("Enter the number of credits for Spring semester: "))

            if creditsFA <= 6 and creditsSP <= 6:
                print("A = On-Campus\tB = Online")
                student = input("Are you On Campus or Online? ").upper()

                tuition_FA = Fall_C3(creditsFA, student)
                tuition_SP = Spring_C3(creditsSP, student)
                done = True
            else:
                print("One or both of the credits is greater than 6. Please try again.")

    elif student == "FT":
        done = False
        while not done:
            creditsFA = int(input("Enter the number of credits for Fall semester: "))
            creditsSP = int(input("Enter the number of credits for Spring semester: "))

            if (6 <= creditsFA <= 12) and (6 <= creditsSP <= 12):
                print("A = On-Campus\tB = Online")
                student = input("Are you On Campus or Online? ").upper()

                tuition_FA = Fall_C3(creditsFA, student)
                tuition_SP = Spring_C3(creditsSP, student)
                done = True
            else:
                print("All full-time graduate students must register for a minimum of six (6) credits per semester,",
                    "\nwith a maximum of fifteen (12) credits allowed.")

    done = False
    while not done:
        print("\nA = On-Campus\tB = Off-Campus\tC = Commute")
        housing = input("Do you like to live On-Campus, Off-Campus, or Commute: ").upper()

        if housing == "A" or housing == "B" or housing == "C":
            houses = house_C3(housing)
            done = True
        else:
            print("Invalid input. Please enter A, B, or C.")


    infile = open('RiderMealPlan.txt', 'r')
    file_contents = infile.read()
    infile.close()
    print(file_contents)

    done = False
    while not done:
        mealPlan = input("\nChoice your Meal Plan between A to C" +
                        "\nOr Eat Out / My Food" +
                        "\nEnter your choice: ").lower()
        if mealPlan in ["a", "b", "c", "eat out", "my food" ]: # Using Array - necessary conditions
            mealPlan = traditionalHall_C3(mealPlan)
            done = True
            break
        else:
            print("Invalid Choice")


    total_C3(creditsFA, creditsSP, tuition_FA, tuition_SP, houses, mealPlan, gradSchool)

# define College 3 Tuition Function
def Fall_C3(creditFA, person):
    if creditFA <= 12:
        if person == "A":
            TuitionPerCredit = 1020.00
            FeesPerSemester = 600.00
            Total = (TuitionPerCredit * creditFA) + FeesPerSemester
            TuitionFA = Total
            print("Fall Semester Tuition Cost: $", TuitionFA)
            return TuitionFA

        elif person == "B":
            TuitionPerCredit = 1040.00
            FeesPerSemester = 600.00
            Total = (TuitionPerCredit * creditFA) + FeesPerSemester
            TuitionFA = Total
            print("Fall Semester Tuition Cost: $", TuitionFA)
            return TuitionFA

    else:
        return None

def Spring_C3(creditSP, person):
    if creditSP <= 12:
        if person == "A":
            TuitionPerCredit = 1020.00
            FeesPerSemester = 600.00
            Total = (TuitionPerCredit * creditSP) + FeesPerSemester
            TuitionSP = Total
            print("Spring Semester Tuition Cost: $", TuitionSP)
            return TuitionSP

        elif person == "B":
            TuitionPerCredit = 1040.00
            FeesPerSemester = 600.00
            Total = (TuitionPerCredit * creditSP) + FeesPerSemester
            TuitionSP = Total
            print("Spring Semester Tuition Cost: $", TuitionSP)
            return TuitionSP
    else:
        return None

# define College 2 Housing Function
def house_C3(campus):
        if campus == "A": # On Campus Cost
            infile = open('RiderOnCampusHousing.txt', 'r')
            file_contents = infile.read()
            infile.close()
            print(file_contents)

            done = False
            while not done:
                option = int(input("Which building are you interested in living On Campus? "))

                if option == 1:
                    room = "Standard Double"
                    price = 5215.00
                    print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif option == 2:
                    room = "Air Conditioned Double"
                    price = 5885.00
                    print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif option == 3:
                    room = "Double as Single"
                    price = 6795.00
                    print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif option == 4:
                    room = "Suites"
                    price = 6395.00
                    print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif option == 5:
                    room = "Apartments"
                    price = 6680.00
                    print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif option == 6:
                    room = "RA/CA Rate"
                    price = 1305.00
                    print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif option == 7:
                    room = "Poyda Double/Single with Air"
                    price = 6120.00
                    print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                elif option == 8:
                    room = "Poyda Double/Single without Air"
                    price = 5620.00
                    print("Room for " + room + " would cost you $" + str(price) + " Per Semester.")
                    done = True
                    return price

                else:
                    print("Invalid input. Please enter 1, 2, 3, 4, 5, 6, 7, or 8 for the Building(s) you prefer to live On-Campus.")

        elif campus == "B":
            infile = open('RiderOffCampusHousing.txt', 'r')
            file_contents = infile.read()
            infile.close()
            print(file_contents)

            room = int(input("Do you prefer House 1, 2, or 3? " +
                         "\nEnter: "))

            if room == 1:
                price = 1872
                print("\nYou are currently living in The Crossings at Ewing.")
                print("1 Bed would cost you $" + str(price))
                done = True
                return price

            elif room == 2:
                price = 1790
                print("\nYou are currently living in Stewards Crossing.")
                print("1 Bed would cost you $" + str(price))
                done = True
                return price

            elif room == 3:
                price = 1650
                print("\nYou are currently living in Parkside Court.")
                print("1 Bed would cost you $" + str(price))
                done = True
                return price

            else:
                print("Invalid input. Please Try Again")

        elif campus == "C":
            print("Student must have a permits before Fall Semester for all students who park a car on campus.\n")
            print("Permits are $250 for the full academic year, $125 for half the academic year")

            payment = input("\nDo you want to buy a Full Time or Part Time? [Enter: FT/PT] : ").lower()
            if payment == "ft":
                permitType = "Full Time"
                price = 250
                print("You purchase a ", permitType, "Parking Permit for Rider University and the cost is $", str(price))
                return price

            elif payment == "pt":
                permitType = "Part Time"
                price = 125
                print("You purchase a ", permitType, "Parking Permit for Rider University and the cost is $", str(price))
                return price

# define College 3 Meals Function
def traditionalHall_C3(meal):
    if meal == "a":
        rate = 3150
        print("A Plan: $", rate)
        print("Fall or Spring Carte Blanche Plus with $275 Bronc Bucks (includes unlimited meal swipes at Daly Dining Hall)")
        return rate

    elif meal == "b":
        rate = 3150
        print("B Plan: $", rate)
        print("Fall or Spring - 14 Meal Plan with $375 Bronc Bucks")
        return rate

    elif meal == "c":
        rate = 2650
        print("C Plan: $", rate)
        print("Fall or Spring Greek Plan - 10 meals per week with $175 Bronc Bucks")
        return rate

    elif meal == "eating out":
        rate = 0
        print("You chose to eat out, Drive Safe and Enjoy your food")
        return rate

    elif meal == "my food":
        rate = 0
        print("Enjoy your food")
        return rate

# define College 3 Total Function
def total_C3(CFA, CSP, TFA, TSP, home, eat, year):
    print("\nFall Semester")
    print("Fall Credits:", CFA)
    print("Tuition: $", TFA)
    print("Housing: $", home)
    print("Meals: $", eat)
    fallTotal = TFA + home + eat
    print("Fall Total: $", fallTotal)

    print("\nSpring Semester")
    print("Fall Credits:", CSP)
    print("Tuition: $", TSP)
    print("Housing: $", home)
    print("Meals: $", eat)
    springTotal = TSP + home + eat
    print("Spring Total: $", springTotal)

    FullYr = fallTotal + springTotal
    print("\nAcademic Year Total will cost $", FullYr)

    total = FullYr * year
    print("\nIf it takes you", year, "years to receive Master Degree.",
          "\nEstimated Degree Total: $", total)

# call to main function, do not delete!
main()
