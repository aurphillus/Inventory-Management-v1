from django.db import models

# Create your models here.

# Models in Django are used to create tables.
# Models is the single, definitive source of information about the data. It contains the essential fields and behaviors of data we're storing.
# Each Model maps to a single database table.




class Device(models.Model):     #Creating a generic class that will be inherited by other classes to create the subsequent tables for different Classes.

# CharField is used to create a field with character type.
# max_length specifies the maximum length that is allocated to the field
# blank specifies whether or not the field can be kept empty, If false, It is compulsary to fill the field
# IntegerField is used to take an integer as an input.
# choices are used to specify the choices that can be used. It creates a drop down list as an input


    type = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    # choices are defined under () brackets where it is seperated by comma, the first part gets stored in the database and the seccond part is used to show to the user.
    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item already purchased'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    #Defining meta class and changing the abstract to True makes sure that no Table called Device is created, as it will be inherited by other classes
    class Meta:
        abstract = True

    #Overwriting default __str__ function and passing the values required as output to be shown.
    def __str__(self):
        return 'Type: {0} | Price: {1} | Issues: {2}'.format(self.type, self.price,self.issues)


class Laptop(Device):   #Inheriting Device class and creating a table for Laptop.
    pass


class Desktop(Device):  #Inheriting Device class and creating a table for Desktop.
    pass

class Mobile(Device):   #Inheriting Device class and creating a table for Mobile.
    pass
