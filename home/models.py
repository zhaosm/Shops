from django.db import models

# Create your models here.
from django.utils import timezone


class ShopManager(models.Manager):
    def get_by_natural_key(self, urlID):
        return self.get(urlID=urlID)

    def count_occurrence(self, classify_by):
        """
        custom query function which count the occurrence times of each distinct value in a specified classify_by
        the 'classify_by' input should be a column name(string)
        this return a table like:
        -----------------------------------------------------------------------------
        |classify_by                              |num                               |
        -----------------------------------------------------------------------------
        |the distinct value of column classify_by |row number of rows with this value|
        -----------------------------------------------------------------------------
        |...                                      |                                  |
        -----------------------------------------------------------------------------
        """
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("SELECT " + classify_by + ", count(*) num FROM shops GROUP BY " + classify_by)
        result = sorted([row for row in cursor.fetchall()], key=lambda x: -x['num'])
        return result

class Shop(models.Model):
    """
    shops' data structure
    """
    objects = ShopManager()

    urlID = models.BigIntegerField(default=0)
    loc = models.CharField(max_length=50)
    tel = models.CharField(max_length=20, default="")
    pic = models.URLField(default="")
    shopname = models.CharField(max_length=50)
    service = models.FloatField(default=0)
    taste = models.FloatField(default=0)
    foodtype = models.CharField(max_length=50)
    shoplevel = models.CharField(max_length=50)
    envi = models.FloatField(default=0)
    avgcost = models.IntegerField(default=0.0)
    street_address = models.CharField(default="", max_length=50)

    class Meta:
        unique_together = (('urlID',),)

    def __str__(self):
        return "{}: id: {}, 位置: {}, 分类: {}, 味道: {}, 服务: {}, 环境: {}".format(self.shopname, self.id,
                                                     self.loc, self.foodtype, self.taste, self.service, self.envi)


class Comment(models.Model):
    """
    comments' class
    one shop may have many reviews, but one review only belongs to one shop
    same for the 'user' field
    
    NOTE: since Comment has a foreign key referencing User, we need to add natural key handling to users' class
    see https://docs.djangoproject.com/en/1.11/topics/serialization/#natural-keys for detail
    """
    content = models.TextField(max_length=1000)
    shop = models.ForeignKey(Shop)  # shop's urlID
    # user = models.ForeignKey('User')  # TO DO: need to add this
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "id: {}, content: {}, created at: {}, shop id: {}".format(self.id, self.content,
                                                                         self.created_at, self.shop_id)









