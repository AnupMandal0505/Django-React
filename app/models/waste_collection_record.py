from django.db import models
from .waste_collector import WasteCollector
from .waste_collection_point import CollectionPoint

WASTE_TYPE = (
    ("plastic", "plastic"),
    ("iron", "iron"),
    ("glass", "glass"),
    ("paper","paper"),
)

WORK_PROCESS = (
    ("complete", "complete"),
    ("pending", "pending"),
    ("cancel", "cancel"),
)

class WasteCollectionRecord(models.Model):
    collection_point_ref = models.OneToOneField(CollectionPoint, on_delete=models.CASCADE)
    # order_id=models.CharField(max_length=25,unique=True,default="NONE")
    record_id=models.CharField(max_length=25,primary_key=True)
    collection_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 20,choices = WORK_PROCESS,default = 'pending')
    payment_status = models.CharField(max_length = 20,default = 'failed')



    def __str__(self):
        return str(self.record_id)
    


class WasteTypeDetail(models.Model):
    record_ref = models.ForeignKey(WasteCollectionRecord, on_delete=models.CASCADE)
    waste_type = models.CharField(max_length = 20,choices = WASTE_TYPE,default = 'plastic')
    quantity_collected = models.IntegerField()
    pay=models.IntegerField()