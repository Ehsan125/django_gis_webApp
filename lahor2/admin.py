from django.contrib import admin
from .models import Countie, Incidences, Lahore
#from django.contrib.gis.db import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    #pass
    list_display=('name', 'location')
class CountyAdmin(LeafletGeoAdmin):
    list_display = ('counties','cty_code', 'codes')
    search_fields = ('counties',)
    filter_fields = ('counties','cty_code')

class LahoreAdmin(LeafletGeoAdmin):
    list_display = ('tehsil_n','district_n', 'shape_leng', 'shape_area', 'geom')
    search_fields = ('tehsil_n',)
    filter_fields = ('tehsil_n','district_n')

#admin.site.register(Incidence, IncidenceAdmin)

#© 2021 GitHub, Inc.

admin.site.register(Incidences, IncidencesAdmin)
admin.site.register(Countie, CountyAdmin)
admin.site.register(Lahore, LahoreAdmin)