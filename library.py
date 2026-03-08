from abc import ABC,abstractmethod
from datetime import date
class InvalidItemTypeException(Exception):
    pass
class AlreadyIssuedItemException(Exception):
    pass
class NotBorrowedException(Exception):
    pass
class OverdueReturnException(Exception):
    pass
class LibraryItem(ABC):
    def __init__(self,id,title,issue_date,is_issued):
        self.id=id
        self.title=title
        self.issue_date=issue_date
        self.is_issued=is_issued
    @abstractmethod
    def calculate_fine(self,return_date):
        pass
class Book(LibraryItem):
    def calculate_fine(self,return_date):
        self.days_diff=(return_date-self.issue_date).days
        if self.days_diff<=14:
            self.fine=0
        else:
            self.overdue=self.days_diff-14
            self.fine=self.overdue*2
        return self.fine
class Journal(LibraryItem):
    def calculate_fine(self,return_date):
        self.days_diff=(return_date-self.issue_date).days
        if self.days_diff<=7:
            self.fine=0
        else:
            self.overdue=self.days_diff-7
            self.fine=self.overdue*5
        return self.fine
class DigitalMedia(LibraryItem):
    def calculate_fine(self,return_date):
        return 0
class LibraryUser():
    def __init__(self,user_id,name):
        self.user_id=user_id
        self.name=name
        self.borrowed_items=[]
    def borrow_item(self,item):
        if (isinstance(item,LibraryItem)):
            #valid
            item.issue_date=date.today()
            if not item.is_issued:
                if item not in self.borrowed_items:
                    item.is_issued=True
                    self.borrowed_items.append(item)
                    print("\nItem borrowed successfully")
                else:
                    print("Item already in the borrowed list")
            else:
                raise AlreadyIssuedItemException("User already borrowed this item")
        else:
            raise InvalidItemTypeException("Invalid item type")
    def return_item(self,item,return_date):
        if item in self.borrowed_items:
            self.return_date=return_date
            self.fine=item.calculate_fine(self.return_date)
            self.borrowed_items.remove(item)
            print("\nItem removed successfully")
            if self.fine>0:
                    raise OverdueReturnException(f"Overdue  !!! Fine amount : {self.fine}")
            self.borrowed_items.remove(item)
            print("\nItem removed successfully")
        else:
            raise NotBorrowedException('Item was not borrowed')
libraryitems=[]
users=[]
ch=0
def find_item(itemid):
    for item in libraryitems:
        if item.id==itemid:
            return item
    return None
def find_user(userid):
    for user in users:
        if user.user_id==userid:
            return user
    return None
while ch!=7:
    ch=int(input('\nEnter a choice:\n1.Add a book to library\n2.Add a journal to library\n3.Add a digital media to libary\n' \
    '4.Add a user\n5.Borrow an item\n6.Return an item\n7.Exit\n'))
    match ch:
        case 1:
            bid=input("Enter the book id: ")
            btitle=input("Enter the book title: ")
            if btitle=='' or bid =='':
                print("Enter a valid input")
                break
            book=Book(bid,btitle,None,False)
            libraryitems.append(book)
            print("\nBook added successfully")
        case 2:
            jid=input("Enter the journal id: ")
            jtitle=input("Enter the journal title: ")
            if jtitle=='' or jid =='':
                print("Enter a valid input")
                break
            journal=Journal(jid,jtitle,None,False)
            libraryitems.append(journal)
            print("\nJournal added successfully")
        case 3:
            did=input("Enter the digitalmedia id: ")
            dtitle=input("Enter the digitalmedia title: ")
            if dtitle=='' or did =='':
                print("Enter a valid input")
                break
            digital=DigitalMedia(did,dtitle,None,False)
            libraryitems.append(digital)
            print("\nDigital media added successfully")
        case 4:
            uid=input("Enter the user id: ")
            uname=input("Enter the user name: ")
            if uid=='' or uname =='':
                print("Enter a valid input")
                break
            user=LibraryUser(uid,uname)
            users.append(user)
            print("\nUser added successfully")
        case 5:
            uid=input("Enter the user id: ")
            iid=input("Enter the item id: ")
            user=find_user(uid)
            item=find_item(iid)
            if user and item:
                try:
                    user.borrow_item(item)
                except AlreadyIssuedItemException as e:
                    print(e)
                except InvalidItemTypeException as e:
                    print(e)
            else:
                print("User or item not found")
        case 6:
            uid=input("Enter the user id: ")
            iid=input("Enter the item id: ")
            y,m,d=map(int,input("Enter the return date: ").split(','))
            d=date(y,m,d)
            user=find_user(uid)
            item=find_item(iid)
            if user and item:
                try:
                    user.return_item(item,d)
                except OverdueReturnException as e:
                    print(e)    
                except NotBorrowedException as e:
                    print(e)
            else:
                print("User or item not found")
        case 7:
            print("\nExiting...")
            break
        case _:
            print("Invalid choice")