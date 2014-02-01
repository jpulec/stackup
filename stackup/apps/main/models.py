from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=256)
    cl_id = models.IntegerField()
    cl_rent = models.IntegerField(null=True)
    star_difference = models.IntegerField(null=True)

    def __unicode__(self):
        return unicode(self.name)

class StandardOfLiving(models.Model):
    region = models.ForeignKey('Region')
    star_level = models.IntegerField()
    threshold = models.FloatField()

    def __unicode__(self):
        return unicode(self.region) + ":" + unicode(self.star_level) + ":" + unicode(self.threshold)
