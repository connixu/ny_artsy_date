# ny_artsy_date

A Python package to provide easy access to current and upcoming art-based events within a walkable / bikeable distance (500-3000 meters) in the New York Metro area using NYC ArtBeats and Google Maps API's.

## Installation

```bash
$ pip install ny_artsy_date
```
You can also clone this Github Repository.

## Usage

For more detailed usage cases, please refer to [Usage Vignette](). Below are two samples of use cases: 

```Python
from ny_artsy_date import ny_artsy_date as nydate
nydate.find_my_art_events(my_location = 'Chelsea Market', google_maps_key = API_KEY, free_only = 1)
```

   Event_Name 
0  Maria Lassnig “The Paris Years, 1960–68”   
1                       “Rested” Exhibition   
2       Rene Ricard “Growing Up in America”   
3                   “In Support” Exhibition   
5                  Neo Rauch “The Signpost”   
6     Portia Zvavahera “Ndakaoneswa murima”   

                                   Event_Description     DateEnd    Distance  Event_Lat  Event_Lon Event_Price_Adult                                        url\
0  Petzel presents Maria Lassnig: The Paris Years...  2021-12-17  198.808432  40.744239 -74.005967                 0   http://www.nyartbeat.com/event/2021/F832
1  Nicola Vassell Gallery presents Rested, a grou...  2022-01-08  269.415103  40.744873 -74.006051                 0   http://www.nyartbeat.com/event/2021/835B  
2  Vito Schnabel Gallery presents Rene Ricard: Gr...  2021-12-18  298.924224  40.745089 -74.005274                 0   http://www.nyartbeat.com/event/2021/EB40   
3  The Kitchen presents In Support, a group exhib...  2022-03-12  318.248758  40.745308 -74.006186                 0   http://www.nyartbeat.com/event/2021/DC0C   
5  David Zwirner presents The Signpost, an exhibi...  2021-12-18  337.384190  40.745461 -74.006464                 0   http://www.nyartbeat.com/event/2021/1EE0   
6  David Zwirner presents Ndakaoneswa murima, an ...  2021-12-18  337.384190  40.745461 -74.006464                 0   http://www.nyartbeat.com/event/2021/9D69  

                            Event_Address  
0  456 W 18th St, New York, NY 10011, USA  
1  456 W 18th St, New York, NY 10011, USA  
2  456 W 18th St, New York, NY 10011, USA  
3  456 W 18th St, New York, NY 10011, USA  
5  456 W 18th St, New York, NY 10011, USA  
6  456 W 18th St, New York, NY 10011, USA 

```Python
from ny_artsy_date import ny_artsy_date as nydate
df1, map = nydate.choose_my_art_date(my_location = 'Columbia University', google_maps_key = API_KEY, search_range = 3000,mapping = 1)
```
|    | Field              | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---:|:-------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | Event_Name         | “The Hare with Amber Eyes” Exhibition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|  3 | Event_Description  | The Jewish Museum presents The Hare with Amber Eyes, an exhibition that tells the story of the Ephrussi family—celebrated in the 2010 memoir and The New York Times bestseller of the same name by Edmund de Waal—and showcases the breadth and depth of their illustrious collection. The exhibition explores the family’s rise to prominence and splendor in the first half of the nineteenth century, followed by a focus on the prolific collector and historian of art, Charles Ephrussi, to the inter-war years, and finally World War II, when the family lost its fortune and collection to Nazi looting.                                                                                                                                                                                                                                  |
|    |                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|    |                    | At the exhibition’s centerpiece are the extraordinary collection of Japanese netsuke, miniature carved sculptures from the Edo Period (17th-19th centuries), originally collected by Charles Ephrussi in the late 1880s. The netsuke were hidden by a maid from German officials in her mattress during World War II and later returned to the family after the war. The collection of netsuke has since been handed down to subsequent generations, serving as a connection between the past and the present. The most recent member of the family to inherit the collection, author and ceramicist Edmund de Waal, drew from them the inspiration for his memoir The Hare with Amber Eyes, continuing the family’s storied legacy of artistic and cultural pursuits.This exhibition is supported through the Exhibitions Abroad Support Program. |
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
map1

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`ny_artsy_date` was created by Connie (Ye) Xu . It is licensed under the terms of the MIT license.

## Credits

`ny_artsy_date` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
