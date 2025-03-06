import sys
from add_book import TotalManager  
from remove_book import BookRemover  
from view_books import BookViewer
from search_book import BookSearcher
class BookStore:
    def __init__(self):
        self.manager = TotalManager()  
        self.remover = BookRemover()
        self.viewer = BookViewer()
        self.searcher = BookSearcher()

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
                if not choice.isnumeric():
                    raise ValueError("Eta kono number noy! Ekti number input din.")
                
                choice = int(choice)
                if choice not in range(1, 6): 
                    raise ValueError("Apni thik input den nai. Value error. 1 theke 5 er moddhe number dite hobe.")
                
                if choice == 1:
                    print("Choice 1: Add selected")
                    self.manager.add_book()
                elif choice == 2:
                    print("Choice 2: View selected")
                    self.viewer.view_books()
                elif choice == 3:
                    print("Choice 3: Search selected")
                    self.searcher.search_book()
                elif choice == 4:
                    print("Choice 4: Remove selected")
                    self.remover.removebook()  
                elif choice == 5:
                    print("Choice 5: Save data and exit selected")
                    sys.exit()
            
            except ValueError as valueerror:
                print(f"Sorry!! {valueerror}")

if __name__ == "__main__":
    cli = BookStore()
    cli.show_menu()
