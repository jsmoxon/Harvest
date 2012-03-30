from django.db import models
from django.contrib.auth.models import User, Permission, Group

class Job(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return str(self.name)

class Referer(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return str(self.name)

PREFERRED_DAYS = (
    ("Weekdays", "Weekdays"),
    ("Weekends", "Weekends"),
    ("Either", "Either"),
)

class Volunteer(models.Model):
    user = models.ForeignKey(User)
    job = models.ManyToManyField(Job, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    group = models.TextField(null=True, blank=True)
    health = models.TextField(null=True, blank=True)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=15)
    minor = models.BooleanField()
    minor_contact = models.CharField(max_length=100, blank=True, null=True)
    referer = models.ManyToManyField(Referer, null=True, blank=True)
    newsletter = models.BooleanField(default=True)
    preferred_days = models.CharField(max_length=100, choices=PREFERRED_DAYS, blank=True, null=True)
    def __unicode__(self):
        return str(self.first_name)+" "+str(self.last_name)

class Comment(models.Model):
    volunteer =models.ForeignKey(Volunteer)
    comment = models.TextField()
    def __unicode__(self):
        return str(self.volunteer)

class YardLocation(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return str(self.name)

class Agency(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(null=True, blank=True)
    def __unicode__(self):
        return str(self.name)

class Production(models.Model):
    range = models.CharField(max_length=100)
    def __unicode__(self):
        return str(self.range)

class PostHarvestTree(models.Model):
    date = models.DateField()
    pounds = models.IntegerField()
    issues = models.TextField(blank=True, null=True)
    def __unicode__(self):
        return str(self.date)+" "+str(self.pounds)+"lbs"
    
class WhoWillHarvest(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return str(self.name)

class House(models.Model):
    owner = models.CharField(max_length=100, blank=True, null=True)
    owner_email = models.EmailField(max_length=75, blank=True, null=True)
    owner_phone = models.CharField(max_length=15, blank=True, null=True)
    who_will_harvest = models.ForeignKey(WhoWillHarvest, null=True, blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    reference = models.CharField(max_length=100, null=True, blank=True)
    reference_email = models.EmailField(max_length=75, null=True, blank=True)
    def __unicode__(self):
        return str(self.owner)+" "+str(self.address)+" "+str(self.city)

MONTHS = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December")
)


class Tree(models.Model):
    type = models.CharField(max_length=100, blank=True, null=True)
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, blank=True)
    yard_location = models.ForeignKey(YardLocation, on_delete=models.SET_NULL, blank=True, null=True)
    height = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    production = models.ForeignKey(Production, on_delete=models.SET_NULL, blank=True, null=True)
    sprayed = models.NullBooleanField()
    ripen_month = models.CharField(max_length=100, choices=MONTHS, blank=True, null=True)
    ripe = models.BooleanField()
    refererence = models.CharField(max_length=100, null=True, blank=True)
    reference_email = models.EmailField(max_length=75, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    harvests = models.ManyToManyField(PostHarvestTree, blank=True, null=True)
    def __unicode__(self):
        return str(self.type)+" "+str(self.house)

class SpottedTree(models.Model):
    type = models.CharField(max_length=100, blank=True, null=True)
    house = models.ForeignKey(House, null=True, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    yard_location = models.ForeignKey(YardLocation, on_delete=models.SET_NULL, blank=True, null=True)
    height = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    production = models.ForeignKey(Production, on_delete=models.SET_NULL, blank=True, null=True)
    sprayed = models.NullBooleanField()
    ripen_month = models.CharField(max_length=100, choices=MONTHS, blank=True, null=True)
    ripe = models.BooleanField()
    refererence = models.CharField(max_length=100, null=True, blank=True)
    reference_email = models.EmailField(max_length=75, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    harvests = models.ManyToManyField(PostHarvestTree, blank=True, null=True)
    def __unicode__(self):
        return str(self.type)+" "+str(self.address)


class Harvest(models.Model):
    trees = models.ManyToManyField(Tree)
    date = models.DateField()
    volunteers = models.ManyToManyField(Volunteer)
    agency = models.ForeignKey(Agency)
    leader = models.CharField(max_length=200)
    size = models.IntegerField(default=20)
    comment = models.ManyToManyField(Comment, blank=True, null=True)
    def __unicode__(self):
        return str(self.date)+" "+str(self.leader)
    
