from django.db import models
from .user import User
GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others"),
)

STATE = (
    ("AN", "Andaman and Nicobar Islands"),
    ("AP", "Andhra Pradesh"),
    ("AR", "Arunachal Pradesh"),
    ("AS", "Assam"),
    ("BR", "Bihar"),
    ("CG", "Chandigarh"),
    ("CH", "Chhattisgarh"),
    ("DN", "Dadra and Nagar Haveli"),
    ("DD", "Daman and Diu"),
    ("DL", "Delhi"),
    ("GA", "Goa"),
    ("GJ", "Gujarat"),
    ("HR", "Haryana"),
    ("HP", "Himachal Pradesh"),
    ("JK", "Jammu and Kashmir"),
    ("JH", "Jharkhand"),
    ("KA", "Karnataka"),
    ("KL", "Kerala"),
    ("LA", "Ladakh"),
    ("LD", "Lakshadweep"),
    ("MP", "Madhya Pradesh"),
    ("MH", "Maharashtra"),
    ("MN", "Manipur"),
    ("ML", "Meghalaya"),
    ("MZ", "Mizoram"),
    ("NL", "Nagaland"),
    ("OR", "Odisha"),
    ("PY", "Puducherry"),
    ("PB", "Punjab"),
    ("RJ", "Rajasthan"),
    ("SK", "Sikkim"),
    ("TN", "Tamil Nadu"),
    ("TS", "Telangana"),
    ("TR", "Tripura"),
    ("UP", "Uttar Pradesh"),
    ("UK", "Uttarakhand"),
    ("WB", "West Bengal"),
    ("NONE", "NONE"),
)

class StatePosition(models.Model):
    state_waste_collector_id=models.CharField(max_length=25,unique=True)
    # first_name = models.CharField(max_length=255, blank=True)
    # last_name = models.CharField(max_length=255, blank=True)
    # phone = models.CharField(max_length=13,blank=True)
    # email = models.EmailField(max_length=255, blank=True)
    # password = models.CharField(max_length=255, blank=True,default="none")
    # age = models.IntegerField()
    # gender = models.CharField(max_length = 20,choices = GENDER,default = 'Male')
    # blood_group = models.CharField(max_length = 20,choices = BLOOD_GROUP,default = '1')
    state_level = models.CharField(max_length = 20,choices = STATE,unique=True,null=True,blank=True)
    join_date = models.DateTimeField(auto_now_add=True)
    # status = models.BooleanField(default=False)
    # delete = models.BooleanField(default=False)
    user_ref = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.state_waste_collector_id)