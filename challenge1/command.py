def hello(name):
    # When this command is used, everything after the word "hello" in the message will be sent to this function.
    # Example: "@Jam hello Ronan" -> this function receivces "Ronan" as the messsage.
    #
    # Your job is to process the message so that this function returns the correct outputs for challenge 1.
    # (for now, it just echoes back the same message)
    message = " "
    
    if(len(name) > 0):
        message = "Hello " + name
    elif (len(name) == 0):
        message = "Hello, Cisco!"
    elif (name.__eq__("Chuck Robbins")):
        message = "Hello Cisco's favourite CEO Chuck Robbins!"
    
    if (name.__eq__("Maxwell")):
        message = "I am a wolf"
    elif (name.__eq__("David")):
        message = "Animals love me"
    elif (name.__eq__("Ivona")):
        message = "Cats love me"
    elif (name.__eq__("Kevin")):
        message = "Blondie"
    
    if(name.__eq__("Cisco")):
        message = "Hello, Cisco!"
    elif(sorted(name)== sorted("Cisco")):
        message = "Hello, Cisco in disguise!."

    return message
    
