#create entries into the tables 
from app import db, Puppy,Owner,Toy

#creating 2 puppies 
rufus = Puppy('Rufus')
milo =Puppy('Milo')

#adding puppies to table 
db.session.add_all([rufus,milo])
db.session.commit()

#check the table
print(Puppy.query.all())

#pull data from the table  .first() will return the 1st item that is matched 
# rufus_in_db =Puppy.query.filter_by(name='Rufus').first()
# #pull data from the table  .all() will return all items matching that filter 
# rufus_in_db =Puppy.query.filter_by(name='Rufus').all()
#pull data from the table  .all() will return all items matching that filter btuonly limit the results to first item in the list [0] 
rufus_in_db =Puppy.query.filter_by(name='Rufus').all()[0]

#create owner object 
#we're creating a new user and linking him with an existing pup in the Puppy table
jose = Owner('Jose', rufus.id)

#give rufus some toys
toy1 =Toy('chew toy', rufus.id)
toy2 =Toy('ball', rufus.id)

#we can add items to different tables at the same time
db.session.add_all([jose, toy1, toy2])
db.session.commit()

#grab rufus from the table again 
rufus_in_db =Puppy.query.filter_by(name='Rufus').first()
print(rufus_in_db)

#accessing the report_toys from puppy class
rufus.report_toys()