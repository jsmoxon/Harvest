project_home="/Users/jackmoxon/Programming/Harvest/harvest/"

import sys, os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from trees.models import *


address = Address()
address.address = "22 Reliez Valley Ct." 
address.city = "Lafayette"
address.state = "California"
address.zip = "94549"
address.save()

agencies = ("Monument Crisis Center", "Food Bank")
for group in angencies:
    agency = Agency()
    agency.name = group
    agency.save()

jobs = ("Harvest Coordinater", "Harvest Helper", "Newsletter Editor/Contributor", "Driver", "Homeowner/Volunteer Interface", "Answer e-mails",
        "Community Outreach", "Partner Interface", "Press Contact", "Give Up My Birthday")

for j in jobs:
    job = Job()
    job.name = j
    job.save()

productions = ("<100 lbs", ">100lbs")
for p in productions:
    production = Production()
    production.range = p
    production.save()

yard_locations = ("Back Yard", "Front Yard")
for y in yard_locations:
    yard = YardLocation()
    yard.name = y
    yard.save()

who_will = ("I will harvest the fruit and leave it at the curbside for pick up", "I need help harvesting the fruit")
for w in who_will:
    who = WhoWillHarvest()
    who.name = w
    who.save()
