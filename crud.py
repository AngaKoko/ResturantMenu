from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def createRestaurant(rName):
    restaurant = Restaurant(name=rName)
    session.add(restaurant)
    session.commit()

def queryAllRestaurants():
    restarants = session.query(Restaurant).all()
    for restaurant in restarants:
        print(restaurant.name)

def getItemInAllRestaurants(itemName):
    items = session.query(MenuItem).filter_by(name=itemName)
    for item in items:
        print(item.id)
        print(item.price)
        print(item.restaurant.name)
        print("\n")

def addItemToRestaurant(_name, _description, _course, _price, _restaurant):
    item = MenuItem(name=_name, description=_description, price=_price, course=_course, restaurant=_restaurant)
    session.add(item)
    session.commit()

def updateItemPrice(_id, _price):
    item = session.query(MenuItem).filter_by(id = _id).one()
    item.price = _price
    session.add(item)
    session.commit()

def deleteItem(_id):
    item = session.query(MenuItem).filter_by(id = _id).one()
    session.delete(item)
    session.commit()

#addItemToRestaurant("Veggie Burger", "made with weath and mean", "Entry", "$5.99", Restaurant(name="Joe Beach"))
#createRestaurant("Joe Beach")
#queryAllRestaurants()
#getItemInAllRestaurants("Veggie Burger")
#updateItemPrice("42", "$10.1")
#deleteItem("42")