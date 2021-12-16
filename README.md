# ny_artsy_date

This is a Python package to help making creatives plan dates and outings by providing easy access to current and upcoming art-based events and restaurants within the NYC Metro area by wrapping the [NYC ArtBeats API](https://www.nyartbeat.com/resources/doc/api) and by leveraging the [Google Maps API's](https://developers.google.com/maps) as accessed through [googlemaps package](https://github.com/googlemaps/google-maps-services-python) as well as [gmaps](https://pypi.org/project/gmaps/) package).

The functions within return data tables and maps as needed based on a specified search radius of a starting address. There is also a function (for those who like spontanaeity) to `choose_my_art_date`, which selects one art-based event and one restaurant nearby based on a starting point. Users can further adjust for a variety of needs, such as search radius from starting point, whether the event is free, and minimum Google Places Rating (for the restaurant). 

Note: this package is dependent on the `googlemaps` and `gmaps` packages, which acces the Google Maps API. Users should obtain a Google Maps API key to use this package to its full capacity.

## Installation

```bash
$ pip install ny_artsy_date
```
You can also clone this Github Repository.

## Usage
Below are two samples of simple use cases for this package: 

#### Finding art event details near Chelsea Market
```Python
from ny_artsy_date import ny_artsy_date as nydate
nydate.find_my_art_events(my_location = 'Chelsea Market', google_maps_key = API_KEY, free_only = 1)
```

|    | Event_Name                               | Event_Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | DateEnd    |   Distance |   Event_Lat |   Event_Lon |   Event_Price_Adult | url                                      | Event_Address                          |
|---:|:-----------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------|-----------:|------------:|------------:|--------------------:|:-----------------------------------------|:---------------------------------------|
|  0 | Maria Lassnig “The Paris Years, 1960–68” | Petzel presents Maria Lassnig: The Paris Years, 1960–68, an exhibition of paintings by the Austrian artist that have rarely been seen in the United States. The show, which includes over 20 important works developed in Lassnig’s studio on rue de Begnolet, covers Lassnig’s formative years in the City of Light.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | 2021-12-17 |    198.808 |     40.7442 |     -74.006 |                   0 | http://www.nyartbeat.com/event/2021/F832 | 456 W 18th St, New York, NY 10011, USA |
  

#### Pick an "artsy date" near Columbia University 

```Python
from ny_artsy_date import ny_artsy_date as nydate
df1, map = nydate.choose_my_art_date(my_location = 'Columbia University', google_maps_key = API_KEY, search_range = 3000,mapping = 1)
```
|    | Field              | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---:|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Event_Name         | “The Hare with Amber Eyes” Exhibition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|  3 | Event_Description  | The Jewish Museum presents The Hare with Amber Eyes, an exhibition that tells the story of the Ephrussi family—celebrated in the 2010 memoir and The New York Times bestseller of the same name by Edmund de Waal—and showcases the breadth and depth of their illustrious collection. The exhibition explores the family’s rise to prominence and splendor in the first half of the nineteenth century, followed by a focus on the prolific collector and historian of art, Charles Ephrussi, to the inter-war years, and finally World War II, when the family lost its fortune and collection to Nazi looting.                                                                                                                                                                                                                                  |
|  5 | DateEnd            | 2022-05-15                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|  7 | Distance           | 2498.1888746727                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|  9 | Event_Lat          | 40.785383                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 11 | Event_Lon          | -73.957622                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 13 | Event_Price_Adult  | 10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 15 | url                | http://www.nyartbeat.com/event/2021/09A4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 17 | Event_Address      | 1216 5th Ave, New York, NY 10029, USA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 18 | Restaurant_Name    | Lex Restaurant                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 20 | Price_Level        | $$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 22 | Restaurant_Rating  | 4.5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 24 | Restaurant_Address | 1370 Lexington Ave, New York                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 26 | Restaurant_Lat     | 40.7825                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 28 | Restaurant_Lon     | -73.9536111                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

<img src="https://github.com/connixu/ny_artsy_date/blob/main/docs/map_example.png" width="850" height="400">

*For more detailed usage cases, please refer to [Usage Vignette](https://github.com/connixu/ny_artsy_date/blob/main/docs/vignette_example.ipynb).*

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`ny_artsy_date` was created by Connie (Ye) Xu . It is licensed under the terms of the MIT license.

## Credits

`ny_artsy_date` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Contact Info

If you have any questions, concerns, or feedback about this package, please contact me at yx2625@columbia.edu. 
