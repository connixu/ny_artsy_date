from ny_artsy_date import ny_artsy_date as nydate
import numpy as np
import pandas as pd 
import pytest
import os

API_KEY = os.getenv('POETRY_GMAPS_TOKEN')


@pytest.fixture
def met_df_function():
    df = nydate.find_my_art_events(my_location = 'Met Museum', google_maps_key = API_KEY)
    return df

def test_art_events(): 
    try: 
        nydate.find_my_art_events(my_location = 'Met Museum', google_maps_key = API_KEY, mapping = True)
    except Exception as exc:
                assert False, f"'find_my_art_events' raised an exception {exc}"
            
def test_far_locations():
    expected = 0
    df = nydate.find_my_art_events(my_location = "University of Minnesota", google_maps_key = API_KEY)
    actual = df.shape[0]
    assert actual == expected

with pytest.raises(ValueError):
    # with improper google key 
    nydate.geocoding(my_location = 'Met Museum', google_maps_key = "jwbeuqbrvuwoq")
    nydate.find_my_dinner(my_location = 'Met Museum', google_maps_key = "jwbeuqbrvuwoq")
    nydate.find_my_art_events(my_location = 'Met Museum', google_maps_key = "jwbeuqbrvuwoq")
    # with improper max_results (larger than max) 
    nydate.find_my_art_events(my_location = 'Met Museum', google_maps_key = API_KEY, max_results = 500)
    # with incorrectly formatted search_range 
    nydate.find_my_art_events(my_location = 'Met Museum', google_maps_key = API_KEY, search_range = 500)
    # with improper search_range (larger than max) 
    nydate.find_my_art_events(my_location = 'Met Museum', google_maps_key = API_KEY, search_range = '10000m')
    # with too far radius
    nydate.find_my_art_events(my_location = "University of Minnesota", google_maps_key = API_KEY)
    # with no free only
    nydate.find_my_art_events(my_location = "Met Museum", google_maps_key = API_KEY, free_only = 'absolutely')

with pytest.raises(TypeError):
    nydate.map_events("columbia university")
