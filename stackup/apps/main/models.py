from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=256)
    trulia_id = models.CharField(max_length=256, blank=True)
    trulia_rent = models.IntegerField(null=True)
    star_difference = models.IntegerField()

    def __unicode__(self):
        return unicode(self.name)

class StandardOfLiving(models.Model):
    region = models.ForeignKey('Region')
    star_level = models.IntegerField()
    threshold = models.FloatField()

    def __unicode__(self):
        return unicode(self.region) + ":" + unicode(self.star_level) + ":" + unicode(self.threshold)
