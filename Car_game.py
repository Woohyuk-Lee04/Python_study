condition = ""
started = False
while True:
    code = (input(">")).upper()
    
    if code == "HELP":
        print("""
start - to start a car
stop - to stop a car
quit - to quit
        """)
    elif code == "START":
       if not started:
        print("Car started... Ready to go!")
        started = True
       else:
        print("Your car is already started!")
    elif code == "STOP" and condition.upper() != "STOP":
        if started:
           print("Car stopped.")
           started = False
        else:
            print("Your car is not running.")
    elif code == "QUIT":
        break
    else:
        print("I don't understand that...")
    
    