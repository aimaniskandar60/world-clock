import pycountry
import pycountry_convert as pc
from continents import continents

COUNTRIES = pycountry.countries
SUBDIVISIONS = pycountry.subdivisions


def get_country_data(country_name: str):
    return COUNTRIES.get(name=country_name)

def get_states_data(country_code: str):
    return [subdivision.name for subdivision in SUBDIVISIONS.get(country_code=country_code)]

def get_continent(country_code: str):
    return continents[pc.country_alpha2_to_continent_code(country_code)]