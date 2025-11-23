print("Conversion Calculator")

while True:
    print("""
    1. Length Conversion
    2. Currency Conversion
    3. Weight Conversion
    4. Time Conversion
    5. Temperature Conversion
    6. Exit
    """)

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        while True:
            print("""
            1. Kilometer to Meter
            2. Meter to Kilometer
            3. Meter to Centimeter
            4. Centimeter to Meter
            5. Centimeter to Millimeter
            6. Inch to Feet
            7. Feet to Inch 
            8. Return to Main Menu
            """)

            lenChoice = int(input("Enter Your Choice: "))

            if lenChoice == 1:
                km = float(input("Enter Kilometers: "))
                m = km * 1000
                print(f"{km} Kilometer = {m} Meter")

            elif lenChoice == 2:
                m = float(input("Enter Meters: "))
                km = m / 1000
                print(f"{m} Meter = {km} Kilometer")

            elif lenChoice == 3:
                m = float(input("Enter Meters: "))
                cm = m * 100
                print(f"{m} Meter = {cm} Centimeter")

            elif lenChoice == 4:
                cm = float(input("Enter Centimeters: "))
                m = cm / 100
                print(f"{cm} Centimeter = {m} Meter")

            elif lenChoice == 5:
                cm = float(input("Enter Centimeters: "))
                mm = cm * 10
                print(f"{cm} Centimeter = {mm} Millimeter")

            elif lenChoice == 6:
                inch = float(input("Enter Inches: "))
                feet = inch / 12
                print(f"{inch} Inch = {feet} Feet")

            elif lenChoice == 7:
                feet = float(input("Enter Feet: "))
                inch = feet * 12
                print(f"{feet} Feet = {inch} Inch")

            elif lenChoice == 8:
                print("Returning to Main Menu...\n")
                break

            else:
                print("Invalid Option! Try Again.")

    elif choice == 2:
        while True:
            print("""
            1. Dollar to Rupee
            2. Rupee to Dollar
            3. Return to Main Menu
            """)
            currChoice = int(input("Enter Your Choice: "))

            if currChoice == 1:
                dollar = float(input("Enter The Value in Dollar: "))
                rupee = dollar * 88.43
                print(f"{dollar} Dollar = {rupee} Rupees")

            elif currChoice == 2:
                rupee = float(input("Enter The Value in Rupee: "))
                dollar = rupee / 88.43
                print(f"{rupee} Rupee = {dollar} Dollar")

            elif currChoice == 3:
                print("Returning to Main Menu...\n")
                break

            else:
                print("Invalid Option! Try Again.")

    elif choice == 3:
        while True:
            print("""
            1. Kilogram to Gram
            2. Gram to Kilogram
            3. Return to Main Menu
            """)
            currChoice = int(input("Enter Your Choice: "))

            if currChoice == 1:
                kilogram = float(input("Enter The Value in Kilogram: "))
                gram = kilogram * 1000
                print(f"{kilogram} Kilogram = {gram} Gram")

            elif currChoice == 2:
                gram = float(input("Enter The Value in Gram: "))
                kilogram = gram / 1000
                print(f"{gram} Gram = {kilogram} Kilogram")

            elif currChoice == 3:
                print("Returning to Main Menu...\n")
                break

            else:
                print("Invalid Option! Try Again.")

    elif choice == 4:
        while True:
            print("""
            1. Hours to Minutes
            2. Minutes to Hours
            3. Seconds to Minutes
            4. Minutes to Seconds
            5. Return to Main Menu
            """)
            timeChoice = int(input("Enter Your Choice: "))

            if timeChoice == 1:
                hour = float(input("Enter Hours: "))
                minute = hour * 60
                print(f"{hour} Hour = {minute} Minutes")

            elif timeChoice == 2:
                minute = float(input("Enter Minutes: "))
                hour = minute / 60
                print(f"{minute} Minutes = {hour} Hours")

            elif timeChoice == 3:
                second = float(input("Enter Seconds: "))
                minute = second / 60
                print(f"{second} Seconds = {minute} Minutes")

            elif timeChoice == 4:
                minute = float(input("Enter Minutes: "))
                second = minute * 60
                print(f"{minute} Minutes = {second} Seconds")

            elif timeChoice == 5:
                print("Returning to Main Menu...\n")
                break

            else:
                print("Invalid Option! Try Again.")

    elif choice == 5:
        while True:
            print("""
            1. Celsius to Fahrenheit
            2. Fahrenheit to Celsius
            3. Celsius to Kelvin
            4. Kelvin to Celsius
            5. Return to Main Menu
            """)
            tempChoice = int(input("Enter Your Choice: "))

            if tempChoice == 1:
                c = float(input("Enter Celsius: "))
                f = (c * 9/5) + 32
                print(f"{c}°C = {f}°F")

            elif tempChoice == 2:
                f = float(input("Enter Fahrenheit: "))
                c = (f - 32) * 5/9
                print(f"{f}°F = {c}°C")

            elif tempChoice == 3:
                c = float(input("Enter Celsius: "))
                k = c + 273.15
                print(f"{c}°C = {k}K")

            elif tempChoice == 4:
                k = float(input("Enter Kelvin: "))
                c = k - 273.15
                print(f"{k}K = {c}°C")

            elif tempChoice == 5:
                print("Returning to Main Menu...\n")
                break

            else:
                print("Invalid Option! Try Again.")

    elif choice == 6:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Try Again.")
