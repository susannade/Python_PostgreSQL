from database import Database
from user import User

Database.initialise(user='postgres', password='****', database='learning', host="localhost")

user = User('emilyp@gmail.com', 'Emily', 'Mann', None)

user.save_to_db()

user_db = User.load_from_db_by_email('johns@gmail.com')

print(user_db)