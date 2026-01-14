def main():
    while True:
        choice_list = ["1","2","3","4","5","6","7","8","9"]
        print("1. Weights")
        main_choice = input("\nWhich Category would you like to choose")
        
        if main_choice in choice_list:
            if main_choice == "1":
                weights()
                break
                
        else:
            print("The option u typed isnt listed")




def weights():
    while True:
        print("\n1. Gram to KG")
        print("2. KG to gram")
        print("Enter nothing to go back!")
        Weight_choice = input("Which measure would you like to choose: ")

        if Weight_choice == "1":
            gram = input("How many grams: ")
            try:
                gram = float(gram)
                kilogram = gram / 1000
                print(f"{kilogram} Kilogram(s)")
                weights()
                break
                
            except:
                print("ERROR please input a int or a float not a str!")
        if Weight_choice == "2":
            kilogram = input("How many Kilograms: ")
            try:
                kilogram = float(kilogram)
                gram = kilogram * 1000
                print(f"{gram} gram(s)")
                weights()
                break
                
            except:
                print("ERROR please input a int or a float not a str!")
        if Weight_choice == "":
            main()
            break
                

main()