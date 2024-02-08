from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User,WasteCollector,DistrictPosition,StatePosition,CollectionPoint,WasteCollectionRecord,Wallet,WasteTypeDetail,SavedAddress
# from .waste_collector import WasteCollector


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id','phone','email','first_name', 'user_type','status','delete']


@admin.register(WasteCollector)
class UserAdmin(admin.ModelAdmin):
    list_display = ['waste_collector_id','district_level','state','user_ref','join_date']


@admin.register(DistrictPosition)
class UserAdmin(admin.ModelAdmin):
    list_display = ['district_waste_collector_id','district_level','state','user_ref','join_date']

@admin.register(StatePosition)
class UserAdmin(admin.ModelAdmin):
    list_display = ['state_waste_collector_id','state_level','user_ref','join_date']

@admin.register(CollectionPoint)
class UserAdmin(admin.ModelAdmin):
    list_display = ['collection_point_id','customer_ref','waste_collector_ref','date','status','created','updated']

@admin.register(WasteCollectionRecord)
class UserAdmin(admin.ModelAdmin):
    list_display = ['record_id','collection_point_ref','collection_date','status']

@admin.register(WasteTypeDetail)
class UserAdmin(admin.ModelAdmin):
    list_display = ['record_ref','waste_type','quantity_collected','pay']


@admin.register(Wallet)
class UserAdmin(admin.ModelAdmin):
    list_display = ['order_id','payment_id']


@admin.register(SavedAddress)
class UserAdmin(admin.ModelAdmin):
    list_display = ['saved_address_id']
