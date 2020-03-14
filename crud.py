"""
Perform crude operations on database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#function adds a new resturant to database
def createRestaurant(_name):
    restaurant = Restaurant(name=_name)
    session.add(restaurant)
    session.commit()

#Fuction queries all resturants in the database
def queryAllRestaurants():
    restarants = session.query(Restaurant).all()
    for restaurant in restarants:
        print(restaurant.name)


#get details of item in all restaurants
def getItemInAllRestaurants(item_name):
    items = session.query(MenuItem).filter_by(name=item_name)
    for item in items:
        print(item.id)
        print(item.price)
        print(item.restaurant.name)
        print("\n")

#Adds a new item to a restaurant
def addItemToRestaurant(_name, _description, _course, _price, _restaurant):
    item = MenuItem(name=_name, description=_description, price=_price, course=_course, restaurant=_restaurant)
    session.add(item)
    session.commit()

#Updates itme price using item id
def updateItemPrice(_id, _price):
    item = session.query(MenuItem).filter_by(id = _id).one()
    item.price = _price
    session.add(item)
    session.commit()

#deltes item from database using item id
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