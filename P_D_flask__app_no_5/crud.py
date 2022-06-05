#CRUD activity on the table and records 
#the print output will be presented in the format described in __repr__ function

from app import db,Puppy



#CREATE a new entry to the table 
my_puppy = Puppy('Rufus', 5)

db.session.add(my_puppy)
db.session.commit()


# READING  the entries in DB
all_puppies=Puppy.query.all() #list all puppies in the table 
print(all_puppies)

#select by ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name) #access the 1st record - only then name column 

#FILTER using column name
puppy_frankie= Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())
#the output will be presented in the format described in __repr__

#UPDATE records 
#first we need to locate the data that is going to be updated 
first_puppy = Puppy.query.get(1)
#once located the record gets updated
first_puppy.age =10
#add the record again and commit changes to save 
db.session.add(first_puppy)
db.session.commit()

#DELETE records
second_pup =Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

#check for changes at the very end 
all_puppies=Puppy.query.all()
print(all_puppies)

#NOTE errors in the script if it is run for a second time . The problem  is when the script asks to delete items that are not in the table 