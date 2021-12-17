# ny_artsy_date

This is a Python package to help plan dates and outings by providing information about art-based events and restaurants within the NYC Metro area based on an initial meeting point. This package serves as a wrapper for the [NYC ArtBeats API](https://www.nyartbeat.com/resources/doc/api) and leverages various functionalities from the [Google Maps API](https://developers.google.com/maps) (as accessed through [googlemaps package](https://github.com/googlemaps/google-maps-services-python) as well as [gmaps](https://pypi.org/project/gmaps/) package) to make planning artsy dates and gatherings simple and fun.

The functions within return data tables and maps as needed based on a specified search radius of a starting address. There is also a function (for those who like spontanaeity) to `choose_my_art_date`, which selects one art-based event and one restaurant nearby based on a starting point. Users can further adjust for a variety of needs, such as search radius from starting point, whether the event is free, and minimum Google Places Rating (for the restaurant). 

Note: this package is dependent on the `googlemaps` and `gmaps` packages, which acces the Google Maps API. Users should obtain a Google Maps API key to use this package to its full capacity.

## Installation

```bash
$ pip install ny_artsy_date
```
You can also clone [this Github Repository](https://github.com/connixu/ny_artsy_date).

## Usage

For more detailed usage cases, please refer to [Usage Vignette](https://github.com/connixu/ny_artsy_date/blob/main/docs/vignette_example.ipynb).


## Official Documentation

The official documentation is hosted on Read the Docs: https://ny-artsy-date.readthedocs.io/en/main/


## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`ny_artsy_date` was created by Connie (Ye) Xu . It is licensed under the terms of the MIT license.

## Credits

`ny_artsy_date` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Contact Info

If you have any questions, concerns, or feedback about this package, please contact me at yx2625@columbia.edu. 
