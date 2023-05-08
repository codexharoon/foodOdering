from django.db import models 
import uuid 
# Create your models here.

class baseModel(models.Model):
    uid = models.UUIDField(primary_key=True , editable=False, default=uuid.uuid4)
    created = models.DateField(auto_created=True)
    updated = models.DateField(auto_created=True)

    class Meta:
        abstract = True



class Products(baseModel):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.CharField(blank=True)


class ProductsMetaInfo(baseModel):
    products = models.OneToOneField(Products,on_delete=models.CASCADE , related_name="meta-info")
    measuring = models.CharField(blank=True,choices=(("L","L"),("ML","ML"),("KG","KG"),(None,None)))
    isRestrict = models.BooleanField(default=False)
    restrict = models.IntegerField()
    quantity = models.IntegerField()


class Images(baseModel):
    products = models.ForeignKey(Products,on_delete=models.CASCADE,related_name="images")
    images = models.ImageField(upload_to="products")
