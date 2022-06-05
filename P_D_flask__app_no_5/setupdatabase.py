
#create an SQL DB and table using SQLAlchemy
from app import db,Puppy

 
#create all the tables, transforms  model into  db table
db.create_all()

sam =Puppy('Sammy', 3)
frank = Puppy('frank', 6)

#adding items to the table --> Multiple items
db.session.add_all([sam, frank])

#adding items to the table --> single item
# db.session.add(sam)

#saving the udpade so that info is added to the table
db.session.commit()

#sanity check , inspect if IDs have been added when 2 pups were added to the table 
print(sam.id)
print(frank.id)