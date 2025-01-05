for i in range(0, 10):    
    # Here, we are declaring an inner loop to handle number of columns    
    # Here, the values are changing according to outer loop    
        for j in range(0, i + 1):    
            # Here, we are declaring a for loop for printing stars    
            for k in range (0,j+1):
                  print(" - ")
            print("* ", end="")       
        # Here, we are giving the ending line after each row    
        print() 