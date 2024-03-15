from django.db import models
from .state_waste_collector import StatePosition
from .user import User
GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others"),
)

DISTRICT = (
    ("Dhanbad", "Dhanbad"),
    ("Bokaro", "Bokaro"),
    ("None", "None"),

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

class DistrictPosition(models.Model):
    district_waste_collector_id=models.CharField(max_length=25,unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    district_level = models.CharField(max_length = 20,choices = DISTRICT,unique=True,null=True,blank=True)
    state = models.CharField(max_length = 20,choices = STATE,null=True,blank=True)

    user_ref = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.district_waste_collector_id)