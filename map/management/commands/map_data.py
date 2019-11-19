from django.core.management.base import BaseCommand, CommandError
from map.models import Map
import json

class Command(BaseCommand):
    help = "deletes old data and replaces with new"


    def handle(self, *args, **options):
        with open("scriptsapp/final-path-graph.json", "r") as f:
            newdata = f.read()
        final_data = json.loads(newdata)
        data = Map.objects.all()
        data.delete()
        Map.objects.create(data=final_data)



