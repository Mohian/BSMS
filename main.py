import sys
from add_book import TotalManager  # Importing the class from add_books.py

class BookStore:
    def __init__(self):
        self.manager = TotalManager()  # Creating an instance of TotalManager

    def show_menu(self):
        # Unlimited loop until the user selects exit
        while True:
            print("\n=== Book Store Management System ===")
            print("1. Add")
            print("2. View")
            print("3. Search")
            print("4. Remove")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            try:
                if not choice.isnumeric():  # Checking if input is a number
                    raise ValueError("Eta kono number noy! Ekti number input din.")
                
                choice = int(choice)
                if choice not in range(1, 6):  # Ensuring input is between 1 and 5
                    raise ValueError("Apni thik input den nai. Value error. 1 theke 5 er moddhe number dite hobe.")
                
                if choice == 1:
                    print("Choice 1: Add selected")
                    self.manager.add_book()  # Calling add_book() method
                elif choice == 2:
                    print("Choice 2: View selected")
                elif choice == 3:
                    print("Choice 3: Search selected")
                elif choice == 4:
                    print("Choice 4: Remove selected")
                elif choice == 5:
                    print("Choice 5: Save data and exit selected")
                    sys.exit()
            
            except ValueError as valueerror:
                print(f"Sorry!! {valueerror}")

if __name__ == "__main__":
    cli = BookStore()
    cli.show_menu()
