import pygame


pygame.init()

# Initialize dictionary, since pygame will generate a
# pygame.JOYDEVICEADDED event for every joystick connected
# at the start of the program.
joysticks = {}

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        #buttons pressed only on the first joystick plugged in.
        #You can remove the "and event.joy==0" if you're only using one joystick
        if event.type == pygame.JOYBUTTONDOWN and event.joy==0:
            if event.button == 0:
                print("A button pressed")
            elif event.button == 1:
                print("B button pressed")
            elif event.button == 2:
                print("X button pressed")
            elif event.button == 3:
                print("Y button pressed")
            elif event.button == 4:
                print("L button pressed")
            elif event.button == 5:
                print("R button pressed")
            elif event.button == 6:
                print("Select button pressed")
            elif event.button == 7:
                print("Start button pressed")
                
        #Buttons released only on the first joystick plugged in.
        #You can remove the "and event.joy==0" if you're only using one joystick                
        if event.type == pygame.JOYBUTTONUP and event.joy==0:
            if event.button == 0:
                print("A button released")
            elif event.button == 1:
                print("B button released")
            elif event.button == 2:
                print("X button released")
            elif event.button == 3:
                print("Y button released")
            elif event.button == 4:
                print("L button released")
            elif event.button == 5:
                print("R button released")
            elif event.button == 6:
                print("Select button released")
            elif event.button == 7:
                print("Start button released")
                
        

        #d-pad input
        if event.type == pygame.JOYAXISMOTION:
            if event.axis==0:
                if round(event.value)==1:
                    print("right")
                elif round(event.value)==-1:
                    print("left")
                elif round(event.value)==-0:
                    print("stop moving right or left")

            if event.axis==1:
                if round(event.value)==1:
                    print("down")
                elif round(event.value)==-1:
                    print("up")
                elif round(event.value)==0:
                    print("stop moving up or down")
                
#                print(round(event.value),0)
#                print(event)
            
            
        if event.type == pygame.JOYDEVICEADDED:
            # This event will be generated when the program starts for every
            # joystick, filling up the list without needing to create them manually.
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks[joy.get_instance_id()] = joy
            print(f"Joystick {joy.get_instance_id()} connencted")

        if event.type == pygame.JOYDEVICEREMOVED:
            del joysticks[event.instance_id]
            print(f"Joystick {event.instance_id} disconnected")
