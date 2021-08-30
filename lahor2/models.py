from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager


# Create your models here.

class Incidences(models.Model):
    name=models.CharField(max_length=60)
    location=models.PointField(srid=4326)
    objects=models.Manager()

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural="Incidences" 

class Countie(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.counties

class Lahore(models.Model):
    objectid = models.BigIntegerField()
    tehsil_n = models.CharField(max_length=50)
    district_n = models.CharField(max_length=50)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
        return self.tehsil_n
    class Meta:
        verbose_name_plural="Lahore"

    
