import sys

class InvalidChoiceError(Exception):
    pass

class BookStore:
    def __init__(self):
        pass
    def show_menu(self):
        #unlimited time menu show hobe jotokkhon na 5 press kore exit kora hocche. 
        while True:
            print("\n=== Book Store Management System ===")
            print("1. Add")
            print("2. View")
            print("3. Search")
            print("4. Remove")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            try:
                #error message 
                if not choice.isnumeric():
                    raise InvalidChoiceError("eta kono number noy! ekti number input din")
                
                choice = int(choice)
                if choice not in range(1, 6):
                    raise ValueError("Apni thik input den nai.  value error. 1 theke 5 er moddhe number dite hobe.")
                
                if choice == 1:
                  
                   print("choice 1 Add selected")
                elif choice == 2:
                   
                    print("choice 2 view selected")
                elif choice == 3:
                    print("choice 3 search selected")
                   
                elif choice == 4:
                    print("choice 4 delete selected")

                    
                elif choice == 5:
                    
                    print("choice 5 save data and exit selected")
                    sys.exit()
            except InvalidChoiceError as e:
                print(f"Sorry! {e}")
            except ValueError as valueerror:
                print(valueerror)
if __name__ == "__main__":
    cli = BookStore()
    cli.show_menu()