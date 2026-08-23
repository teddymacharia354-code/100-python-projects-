
while True:
    Lamp_on = input("Is the lamp on,Yes/No?:").lower()
    if Lamp_on == 'yes':
        Bulb_burnt = input ("Is Bulb dim/not lighting,Yes/No?:").lower()
        if Bulb_burnt == 'yes':
            while True:
                print("buy a new bulb")
                buy_bulb = input("Did you buy the bulb?,Yes/No?:").lower()
                if buy_bulb == 'yes':
                    new_bulb_burnt = input ("Is the new Bulb dim/not lighting,Yes/No?:").lower()
                    if new_bulb_burnt == 'no':
                        print("aah problem solved")
                        exit()
                    else:
                        print("You got a defective bulb. Try again!")
                else:
                    print("Please buy a new bulb!")
        else: 
            print("aah problem solved")
            exit()
    else: 
        while True:
            Lamp_plugged= input ("Is the lamp plugged in,Yes/No?:").lower()
            if Lamp_plugged == 'yes' : 
                print("Buy a new lamp")
                break
            else: 
                print("please plug in Lamp!")
