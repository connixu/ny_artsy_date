from ny_artsy_date import ny_artsy_date as nydate
import numpy as np
import pandas as pd 
import pytest
import os

API_KEY = os.getenv('POETRY_GMAPS_TOKEN')


@pytest.mark.parametrize("location, maps, free, expect_zero, expected_len", [
    ('Met Museum', True, 1, True, 2),
    ('Met Museum', False, 0, False, 1),
    ('Hudson Yards', False, 1, True, 1),
    ('Guggenheim', True, 1, False, 2),
    ])

class TestClass:
    def test_length_return(self, location, maps, free, expect_zero, expected_len):
        if maps == True: 
            try:
                result, map = nydate.find_my_art_events(my_location = location, google_maps_key = API_KEY, mapping = maps)
            except Exception as exc:
                assert False, f"unexpected number of items, exception {exc}"
        else:
            try:
                result = nydate.find_my_art_events(my_location = location, google_maps_key = API_KEY, mapping = maps)
            except Exception as exc:
                assert False, f"unexpected number of items, exception {exc}"
                
    def test_length_return_2(self, location, maps, free, expect_zero, expected_len):
        if maps == True: 
            try:
                result, map = nydate.choose_my_art_date(my_location = location, google_maps_key = API_KEY, mapping = maps)
            except Exception as exc:
                assert False, f"unexpected number of items, exception {exc}"
        else:
            try:
                result = nydate.choose_my_art_date(my_location = location, google_maps_key = API_KEY, mapping = maps)
            except Exception as exc:
                assert False, f"unexpected number of items, exception {exc}"
                
    def test_float(self, location, maps, free, expect_zero, expected_len):
        result_df = nydate.find_my_art_events(my_location = location, google_maps_key = API_KEY)
        if result_df.shape[0] != 0:
            try: 
                result_df['Event_Price_Adult'].astype(float)
            except Exception as exc:
                assert False, f"'find_my_art_events' raised an exception {exc}"
        else:
            None
                
    def test_free_only(self, location, maps, free, expect_zero, expected_len):
        result_df = nydate.find_my_art_events(my_location = location, google_maps_key = API_KEY, free_only = free)
        if result_df.shape[0] != 0:
            result_df = result_df[result_df['Event_Price_Adult']!=np.NaN]
            actual = result_df['Event_Price_Adult'].astype(float).mean()
            if expect_zero == True: 
                assert actual == 0
            else: 
                None
        else:
            None
