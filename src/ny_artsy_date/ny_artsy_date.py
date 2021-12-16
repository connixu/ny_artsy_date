import googlemaps
import os
import numpy as np
import requests
import lxml
import pandas as pd
import gmaps
from pandas import json_normalize
import re

def geocoding(my_location, google_maps_key):
    """
    Function to obtain latitude and longitude as needed given simple address data. This package interacts with google maps API 
    to create our visualization, thus an API key is required. 
        
        Args
        ----
        Required: 
            my_location(str): Starting point address - must be within NYC Metro Location
            google_maps_key (str): Google maps API key needed to geocode your location 
                To obtain a google maps API key, please refer to https://developers.google.com/maps

        Returns
        ---
        Latitude and Longitude
            Fields: 
                lat(float): Latitude of location
                lon(float): Longitude of location
            
        Usage Example
        ---
        [in]:
            geocode_events("Met Museum", google_maps_key)
            
        [out]:
            [40.7794, -73.9632]
    """
    
    if google_maps_key.startswith('AI'):
        google_maps = googlemaps.Client(key=google_maps_key) 
    else:
        raise ValueError("Invalid Google Maps Key. Please Refer to https://developers.google.com/maps to obtain a valid key.")
                
    geocode_result = google_maps.geocode(my_location)
    lat = geocode_result[0]['geometry']['location']['lat']
    lon = geocode_result[0]['geometry']['location']['lng']
    
    return lat, lon



def map_events(df, google_maps_key, lat_column, long_column, name_column, start_lon = None, start_lat = None):
    """
    Function to map latitude and longitude as needed given simple address dataframe. This package interacts with google maps API 
    to create our visualization, thus an API key is required. 
        
        Args
        ----
        Required: 
            df(str): Starting point address - must be within NYC Metro Location
            google_maps_key (str): Google maps API key needed to geocode your location 
                To obtain a google maps API key, please refer to https://developers.google.com/maps
            lat_column(str): name of df column containing latitude data we need (events, restaurants, etc)
            long_column(str): name of df column containing latitude data we need (events, restaurants, etc)
                To obtain a google maps API key, please refer to https://developers.google.com/maps
            name_column(str): name of df column containing name data we need (events, restaurants, etc)
        Optional:
            start_lon: longitudinal data of starting point 
            start_lat: latitudinal data of starting point 

        Returns
        ---
        Google Map with markers at the specified points 
            
        Usage Example
        ---
        [in]:
            map_events(df, google_maps_key,'Lat','Long','Name')
            
        [out]:
            Map (Optional): Interactive Google Maps Output with Hover Text Description of Data Point  
    """
    
    marker_locations = df[[lat_column, long_column]]

    hover_info = df[name_column]

    central_coordinates =  df[[lat_column, long_column]].median()
    fig = gmaps.figure(center=central_coordinates, zoom_level=14)

    markers = gmaps.marker_layer(marker_locations, hover_text = hover_info)
    fig.add_layer(markers)
    
    # Optional to add starting point - default when working with other package functions 
    if start_lat != None and start_lon != None:
        start_locations = [[start_lat, start_lon]]
        start_layer = gmaps.symbol_layer(start_locations, fill_color='blue', stroke_color='blue', hover_text = 'Starting Point')    
        fig.add_layer(start_layer)
        
    gmaps.configure(api_key=google_maps_key)

    return fig


def find_my_art_events(my_location = None, google_maps_key = None, lat = None, lon = None, free_only = 0, max_results = np.NaN, search_range = '500m', mapping = False):
    """
    Function to obtain art events data in the NY Metro area near a specified location (address OR latitude and longitude format), 
    using the NY ArtBeat API found at https://www.nyartbeat.com/resources/doc/api. Returns table with events matching a specified radius 
    from a specified location as well as map if requested. 
        
        Args
        ----
        Required: 
            my_location(str): Address starting point - Must be within NYC Metro Location
                Default: None
            google_maps_key (str): Google maps API key needed to geocode your location 
                To obtain a google maps API key, please refer to https://developers.google.com/maps
                Default: None, OR 
            lat(float): Latitude of starting point - Must be within NYC Metro Location 
                Default: None            
            lon(float): Longitude of starting point - Must be within NYC Metro Location 
                Default: None            
        Optional:
            google_maps_key (str): Google maps API key needed to geocode your location OPTIONAL if you have lat-lon location data
                To obtain a google maps API key, please refer to https://developers.google.com/maps
                Default: None
            free_only(bool): Boolean param specifying whether to only return free events 
                Default: False or 0
            max_results(int): Max results to be returned in Query - can be 5, 10, 20, 50 
                Default: np.NaN
            search_range(str): distance (in meters) from location for events queried - can be '500m',"1000m","1500m","3000m"
                Default: 500m
            mapping(bool): Boolean param specifying whether user wants a simple interactive map returned of matching locations

        Returns
        ---
        DataFrame with [max_results] art events in the New York Metro area in the [radius] of the [specified location]
            Fields: 
                Event_Name(str): Name of Event 
                Event_Description(str): Details about event
                Event_Price_Adult(float): Price for tickets
                Event_Price_Detailed(str)): Price for tickets (detailed info)
                DateEnd(date): Last date for exhibit or installation
                Event_Lat(float): Latitude of event 
                Event_Lon(float): Longitude of event
                Event_Address(str): Address for event - requires geocoding; google maps key (above).       
        Map (Optional): Interactive Google Maps Output with Markers for each event; Hover Text Description of Event  
      
        Usage Example
        ---
        [in]: 
            find_my_art_events(lat = 40.78, lon = -73.96, search_range = '3000m', max_results = 5)     
        [out]: 
            df 
            | Event_Name | Event_Description         | Price      | DateEnd | Distance | Latitude | Longitude | Event_Address                 | 
            |------------|---------------------------|------------|---------|----------|----------|-----------|-------------------------------|
            | The..      | The Costume Institute’s...| Adults $25 | 2022-09 |    90.158|    40.779|    -73.96 | 1005 5th Ave, New York...     |
        [out]: 
            Interactive Map  
            
    """
    
    valid_search_range = {'500m',"1000m","1500m","3000m"}
    valid_max_results = {np.NaN,5,10,20,50} 

    try:
        float(search_range)
        search_range = str(search_range)+"m"
    except:
        None  

    if search_range not in valid_search_range:
        raise ValueError("search range must be one of %r." % valid_search_range)
    if max_results != np.NaN and max_results not in valid_max_results:
        raise ValueError("max results must be one of %r." % valid_max_results)
        
    
    assert my_location != None or (lat != None and lon != None), 'Please make sure there are valid address parameters (address or lat/lon).'
    if lat == None or lon == None: 
        lat,lon = geocoding(my_location, google_maps_key)
        
    response = requests.get('http://www.nyartbeat.com/list/event_searchNear',
                            params={'Latitude': lat, 'Longitude': lon,'MaxResults': max_results, 'searchrange':search_range}
                                      )
    try: 
        df = pd.read_xml(response.content)
    except ValueError:
        print("No Results Found. Please try increasing your search range and make sure you are searching within the metro area.")
        return pd.DataFrame()
    
    try: 
        df['Event_Price_Adult'] = ""
        j = -1
        list = [match.group(3) for match in [re.search(r'(adult|adults|admission)(\s|\s\$|\s\:|\:\s|\:\s\$|\:\$)(\d{1,2})', l) for l in df['Price'].str.lower()] if match]
        for i in df.index: 
            string = df.at[i,'Price'].lower()
            if (string == 'free'):
                df.at[i,'Event_Price_Adult'] = 0 
            elif ('suggest' in string) and  ('donate' or 'donation' or 'contribute' or 'contribution' in string) : # e.g., suggested donate
                df.at[i,'Event_Price_Adult'] = 0
            elif [re.search(r'(adult|adults|admission)(\s|\s\$|\s\:|\:\s|\:\s\$|\:\$)(\d{1,2})', string)] != [None]:
                j = j+1 
                df.at[i,'Event_Price_Adult'] = list[j]  
            else: 
                df.at[i,'Event_Price_Adult'] = np.NaN
    except: 
        None 
        

    try:
        if free_only == 1 or free_only == True:
            df = df[df['Event_Price_Adult']==0]
        elif free_only == 0 or free_only == False: 
            None
    except:
        raise ValueError("search range must be 0,1, True, or False")
        
    df['url'] = df['href']
    df = df.rename(columns = {'Name':'Event_Name','Description':'Event_Description','Latitude':'Event_Lat','Longitude':'Event_Lon','Price':'Event_Price_Detailed'})
    df = df[['Event_Name','Event_Description','DateEnd','Distance','Event_Lat','Event_Lon','Event_Price_Adult','url','Event_Price_Detailed']]
   
    if google_maps_key != None:  
        if google_maps_key.startswith('AI'):
            google_maps = googlemaps.Client(key=google_maps_key) 
            try:
                df['Event_Address'] = df.apply(lambda x: google_maps.reverse_geocode((x.Event_Lat,\
                                                                                      x.Event_Lon)), axis=1)[0][1]['formatted_address']
            except:
                None
        else:
            raise ValueError("Invalid Google Maps Key. Please Refer to https://developers.google.com/maps to obtain a valid key.")
            
    df = df.sort_values(by = 'Distance') 
        
    if mapping == True: 
        nymap = map_events(df, google_maps_key = google_maps_key, start_lat = lat, start_lon = lon, lat_column = "Event_Lat", long_column = "Event_Lon", name_column = 'Event_Name')
        return df, nymap
    
    else: 
        return df

    

def find_my_dinner(google_maps_key, my_location = None, mapping = False, lat = None, lon = None, search_range = 500, min_rating = 4.3):
    """
    Returns Restaurant List within a specified range at a specified minimum rating (address OR latitude and longitude format).
        Args
        ----
        Required: 
            my_location(str): Address starting point - Must be within NYC Metro Location
                Default: None
            google_maps_key (str): Google maps API key needed to geocode your location 
                To obtain a google maps API key, please refer to https://developers.google.com/maps
                Default: None, OR 
            lat(float): Latitude of starting point - Must be within NYC Metro Location 
                Default: None            
            lon(float): Longitude of starting point - Must be within NYC Metro Location 
                Default: None
        Optional:
            search_range(float): Distance from starting point (radius for search, meters) 
                Default: 500
            min_rating(float): should be 1-5
                Default: 4.3
            mapping(bool): Boolean param specifying whether user wants a simple interactive map returned of matching locations
                Default: False

        Returns
        ---
        DataFrame with [max_results] restaurants in the New York Metro area in the [radius] of the [specified location]
            Fields: 
                Restaurant_Name(str): Name of restaurant 
                Price_Level(str): $ - $$$$
                Restaurant_Rating(float): 1-5
                Restaurant_Address(str): Distance from starting point (my location) 
                Restaurant_Lat(float): Latitude of restaurant 
                Restaurant_Lon(float): Longitude of restaurant  
        Map (Optional): Interactive Google Maps Output with Markers for each restaurant; Hover Text Description of Restaurant  

        Usage Example
        ---
        [in]:
            find_my_dinner(my_location = '314 11th Ave, New York',google_maps_key = google_maps_key)
        [out]: 
            df 
            | Restaurant_Name | Price_Level      | Restaurant_Rating | Restaurant_Address | 
            |-----------------|------------------|-------------------|--------------------|
            | The Four Seasons| $$$$             | 4.5               |      '1234 Main St'|
        [out]: 
            Interactive Map            
    """
    
    assert my_location != None or (lat != None and lon != None), 'Please make sure there are valid address parameters (address or lat/lon).'
    assert min_rating >= 0 and min_rating <= 5, 'Please make sure there are valid address parameters (address or lat/lon).'

    if lat == None or lon == None: 
        lat,lon = geocoding(my_location, google_maps_key)
    else: 
        None
    
    if google_maps_key.startswith('AI'):
        google_maps = googlemaps.Client(key=google_maps_key) 
    else:
        raise ValueError("Invalid Google Maps Key. Please Refer to https://developers.google.com/maps to obtain a valid key.")
        
    nearby_restaurants = google_maps.places_nearby(location = [lat,lon],radius = 500,keyword = 'restaurant')
    nearby_restaurants_df = pd.DataFrame.from_records(nearby_restaurants['results'])
    
    lat_lon = json_normalize(data=nearby_restaurants_df[['geometry']]['geometry'])
    lat_lon = lat_lon[['location.lat','location.lng']].rename(columns = {'location.lat':'Restaurant_Lat','location.lng':'Restaurant_Lon'})
    
    nearby_restaurants_df = nearby_restaurants_df[['name','price_level','rating','vicinity']].rename(columns = {'vicinity':'Restaurant_Address','rating':'Restaurant_Rating','price_level':'Price_Level','name':'Restaurant_Name'})  
    nearby_restaurants_df = pd.concat([nearby_restaurants_df,lat_lon], axis=1)
    
    nearby_restaurants_df['Price_Level'] = np.where(nearby_restaurants_df['Price_Level'] == 4, '$$$$',
                                                np.where(nearby_restaurants_df['Price_Level'] == 3, '$$$',
                                                        np.where(nearby_restaurants_df['Price_Level'] ==2, '$$',
                                                        np.where(nearby_restaurants_df['Price_Level'] ==1, '$',np.NaN))))

    nearby_restaurants_df = nearby_restaurants_df[nearby_restaurants_df['Restaurant_Rating'] > min_rating]

    if mapping == True: 
        nymap = map_events(nearby_restaurants_df, google_maps_key, start_lat = lat, start_lon = lon, \
                           lat_column = "Restaurant_Lat", long_column = "Restaurant_Lon", name_column = 'Restaurant_Name')
        return nearby_restaurants_df, nymap
    else: 
        return nearby_restaurants_df
    


def choose_my_art_date(my_location, google_maps_key, mapping = False, search_range = 500, min_rating = 4.3):
    """
    Function to select an artsy date and dinner; randomly selects local arts event from NY ArtBeat API 
    found at https://www.nyartbeat.com/resources/doc/api, and uses the arts event data to determine a nearby restaurant. 
        
        Args
        ----
        Required:
            my_location(str): Starting point address - must be within NYC Metro Location
            google_maps_key (str): Optional google maps API key needed to geocode your location 
                To obtain a google maps API key, please refer to https://developers.google.com/maps
        Optional:
            search_range(float): Distance from starting point (radius for search, meters) 
                Default: 500
            min_rating(float): should be 1-5
                Default: 4.3
            mapping(bool): Boolean param specifying whether user wants a simple interactive map returned of matching locations
                Default: False

        Returns        
        ---
        DataFrame with [max_results] art events in the New York Metro area in the [radius] of the [specified location]
            Fields: 
                Event_Name(str): Name of Event 
                Event_Description(str): Details about event
                Event_Price_Adult(float): Price for tickets
                DateEnd(date): Last date for exhibit or installation
                Event_Lat(float): Latitude of event 
                Event_Lon(float): Longitude of event
                Event_Address(str): Address for event - requires geocoding.
                Restaurant_Name(str): Name of restaurant 
                Price_Level(str): $ - $$$$
                Restaurant_Rating(float): 1-5
                Restaurant_Address(str): Distance from starting point (my location) 
                Restaurant_Lat(float): Latitude of restaurant 
                Restaurant_Lon(float): Longitude of restaurant
        Map (Optional): Interactive Google Maps Output with Markers for selected restaurant and selected event.

        Usage Example
        ---
        [in]:
            choose_my_art_date("Met Museum", google_maps_key)
        [out]:
            df
                | Event_Name        | Eugène Leroy “About Marina”
                | Event_Description | Michael Werner Gallery, New York presents an e...
                | Price             | Free
                | DateEnd           | 2021-12-23
                | Distance          | 438.962726
                | Event_Lat         | 40.775625
                ...
        [out]: 
            Interactive Map  
    """
    lat,lon = geocoding(my_location = my_location, google_maps_key = google_maps_key)
   
    df_events = find_my_art_events(my_location = my_location, google_maps_key = google_maps_key, lat = lat, lon = lon, mapping = False, search_range = search_range)
    selected_event_row = df_events.sample(n = 1)
    event_lat = selected_event_row['Event_Lat'].values
    event_lon = selected_event_row['Event_Lon'].values
    
    df_dinner = find_my_dinner(lat = event_lat, lon = event_lon, google_maps_key = google_maps_key, mapping = False, search_range = search_range)
    
    selected_restaurant_row = df_dinner.sample(n = 1) 
    
    date_night_df = pd.concat([selected_event_row,selected_restaurant_row], axis=1).unstack().reset_index().dropna().drop(columns = ['level_1']).rename(columns = {'level_0':'Field',0:'Value'})
    
    if mapping == True: 
        lat_lon_df = pd.concat([selected_event_row[['Event_Name','Event_Lat','Event_Lon']].rename(columns = {'Event_Name':'Name','Event_Lat':'Lat','Event_Lon':'Lon'}),\
                                selected_restaurant_row[['Restaurant_Name','Restaurant_Lat','Restaurant_Lon']].rename(columns = {'Restaurant_Name':'Name','Restaurant_Lat':'Lat','Restaurant_Lon':'Lon'})], axis=0).reset_index()
        nymap = map_events(lat_lon_df, google_maps_key, name_column = 'Name', start_lat = lat, start_lon = lon, lat_column = 'Lat', long_column = 'Lon')
        return date_night_df,nymap
    else: 
        return date_night_df
    