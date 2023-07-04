from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class UserProfile(models.Model):
    def __str__(self):
        return str(self.__dict__)
    
    def update(self ,*args, **kwargs):
        #update user profile with new data
        
        self.update(force_update=True,update_fields=['first_name', 'last_name', 'address', 'city', 'state', 'zipcode', 'phone', 'bio', 'profile_pic', 'age', 'birth_date'])
    # This field is required.

    user = models.OneToOneField(User  , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default='first name')
    last_name = models.CharField(max_length=50, default='last name')
    address = models.CharField(max_length=50, default='address')
    city = models.CharField(max_length=50, default='city')
    state = models.CharField(max_length=50, default='state')
    zipcode = models.CharField(max_length=50, default='zipcode')
    phone = models.CharField(max_length=50, default='phone')


    # Other fields here
    bio = models.TextField(max_length=500, default='neeeds a bio')
    profile_pic = models.ImageField(upload_to='profile_pics', default='defult.jpg')
    age = models.IntegerField(default=0)
    birth_date = models.DateField(null=True, blank=True)

    
    def create_user_profile(sender, instance, created, **kwargs):

        if created:

            UserProfile.objects.create(user=instance)


    post_save.connect(create_user_profile, sender=User)

