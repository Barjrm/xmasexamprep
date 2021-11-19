


car_game = ""
started = False
while True:
    car_game = input('>').lower()
    
    if car_game == 'start':
        if started:
            print('Car already started. ')
        else:
            started = True
            print('Car started. ')    
    elif car_game == 'stop':
        if not started:
           print('Car has already stopped. ') 
        else:
            started = False
            print('car has stopped. ')
    elif car_game == 'help':
        print('''
start - to start the car 
stop - to stop the car 
quit - to exit 
        ''')
    elif car_game == 'quit':
        break
    else:
        print('type help to see commands. ')

