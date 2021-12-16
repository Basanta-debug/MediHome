from django.db import models

# Create your models here.

class Hospital(models.Model):
    hname=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    price=models.IntegerField(null=True)



    def __str__(self):
        return self.hname


class Department(models.Model):
    dname=models.CharField(max_length=100)

    def __str__(self):
        return self.dname

class Time(models.Model):
    time=models.CharField(max_length=100)
    def __str__(self):
        return self.time


patient_gender = [
    ('m', 'Male'),
    ('fm', 'Female'),
    ('o', 'Others'),
]

Payment_method = [
    ('cod', 'Cash'),
    ('Khalti', 'Khalti'),

]
class appointment(models.Model):
    fname=models.CharField(max_length=150,null=True)
    lname=models.CharField(max_length=150,null=True)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100,null=True)
    gender= models.CharField(max_length=2, choices=patient_gender,null=True)
    hospital=models.ForeignKey(Hospital, on_delete=models.CASCADE,null=True)
    payment_method=models.CharField(max_length=20,choices=Payment_method,default="Cash On Delivery")
    payment_comlpeted=models.BooleanField(default=False,null=True,blank=True)
    department=models.ForeignKey(Department, on_delete=models.CASCADE,null=True)

    date=models.DateField()
    age= models.IntegerField(null=True)

    
    

    def __str__(self):
        return self.fname


class contact(models.Model):
    fullname=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    subject=models.CharField(max_length=100,null=True)
    message=models.CharField(max_length=400,null=True)


    def __str__(self):
        return self.fullname


class Medicine(models.Model):
    fname = models.CharField(max_length=150, null=True, verbose_name='First Name')
    lname = models.CharField(max_length=150, null=True, verbose_name='Last Name')
    Phone = models.IntegerField()
    Email = models.EmailField(max_length=100, null=True)
    delivry_add = models.CharField(max_length=200, null=True, verbose_name='Delivery Address')
    Gender = models.CharField(max_length=2, choices=patient_gender, null=True)
    Age = models.IntegerField()
    Med_name = models.CharField(max_length=200, null=True, verbose_name='Medicine Name')
    m_volume = models.IntegerField(verbose_name='Medicine Volume')
    m_description = models.CharField(max_length=400, null=True, verbose_name='Medicine Description')

    def __str__(self):
        return self.Med_name


