import os 
from django.contrib.gis.utils import LayerMapping
from .models import Lahore, Countie

countie_mapping = {
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOLYGON',
}


county_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'counties.shp'),
)

lahore_mapping = {
    'objectid': 'OBJECTID',
    'tehsil_n': 'Tehsil_N',
    'district_n': 'District_N',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

lahore_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'Punjab', 'Tehsil.shp'),
)
def run(verbose=True):
	lm = LayerMapping(Countie, county_shp, countie_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)

def run1(verbose=True):
	lm = LayerMapping(Lahore, lahore_shp, lahore_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)