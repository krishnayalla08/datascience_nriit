while True:
    print("\n*** CALCULATOR ***")
    print("1. Add  2. Sub  3. Mul  4. Div  5. Mod")
    print("6. Pow  7. Sqr  8. Sqrt 9. Fact 10. Exit")
    
    choice = int(input("\nEnter choice (1-10): "))
    
    if choice == 10:
        print("Goodbye!")
        break

    if choice in [1, 2, 3, 4, 5, 6]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if choice == 1: print("Result:", a + b)
        elif choice == 2: print("Result:", a - b)
        elif choice == 3: print("Result:", a * b)
        elif choice == 4:
            if b == 0: print("Cannot divide by zero!")
            else: print("Result:", a / b)
        elif choice == 5:
            if b == 0: print("Cannot divide by zero!")
            else: print("Result:", a % b)
        elif choice == 6: print("Result:", a ** b)
        
   
    elif choice in [7, 8, 9]:
        a = float(input("Enter number: "))
        
        if choice == 7: 
            print("Result:", a ** 2)
        elif choice == 8: 
            print("Result:", a ** 0.5) 
        elif choice == 9: 
         
            fact = 1
            for i in range(1, int(a) + 1):
                fact = fact * i
            print("Result:", fact)
    else:
        print("Invalid choice!")
