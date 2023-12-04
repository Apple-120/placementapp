from django.db import models
from django.contrib.auth.models import User




class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)


    def __str__(self):
        return self.name
    
class Jobs(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()
    experience=models.PositiveIntegerField(default=0)
    last_date=models.DateField()
    vacancies=models.PositiveIntegerField(default=1)
    poster_image=models.ImageField(upload_to="posterimages",null=True,blank=True)
    contact=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
    Category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    status=models.BooleanField(default=True)


    def __str__(self):
        return self.title
class Studentprofile(models.Model):
    qualification=models.CharField(max_length=200)
    resume=models.FileField(upload_to="resume",null=True,blank=True)
    skills=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    options=(
        ("male","male"),("female","female")
    )
    gender=models.CharField(max_length=200,choices=options,default="male")
    experience=models.PositiveIntegerField(default=0)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="profile_pic",null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)


class Applications(models.Model):
    jobs=models.ForeignKey(Jobs,on_delete=models.DO_NOTHING)
    students=models.ForeignKey(User,on_delete=models.CASCADE)
    applied_date=models.DateField(auto_now_add=True)
    options=(
        ("pending","pending"),("rejected","rejected"),("processing","processing")
    )
    status=models.CharField(max_length=200,choices=options,default="pending")

class Projects(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    gitlink=models.CharField(max_length=200)
    user=models.ForeignKey(Studentprofile,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

# Create your models here.
