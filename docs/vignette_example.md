# Example Vignette - ny_artsy_date

This vignette goes through some of the functionalities and installation instructions for the `ny_artsy_date` functions:

## Installation 

Make sure you use python 3.9, as this is part of the package dependency. 


```python
!python3.9 -m pip install -i https://test.pypi.org/pypi/ --extra-index-url https://pypi.org/simple/ ny_artsy_date
import sys
sys.path.append('/usr/local/lib/python3.9/site-packages/')
from ny_artsy_date import ny_artsy_date as nydate
```

    Looking in indexes: https://test.pypi.org/pypi/, https://pypi.org/simple/
    Requirement already satisfied: ny_artsy_date in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (0.1.0)
    Requirement already satisfied: pandas<2.0.0,>=1.3.5 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ny_artsy_date) (1.3.5)
    Requirement already satisfied: pytest-cov<4.0.0,>=3.0.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ny_artsy_date) (3.0.0)
    Requirement already satisfied: pytest<7.0.0,>=6.2.5 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ny_artsy_date) (6.2.5)
    Requirement already satisfied: numpy<2.0.0,>=1.21.4 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ny_artsy_date) (1.21.4)
    Requirement already satisfied: googlemaps<5.0.0,>=4.5.3 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ny_artsy_date) (4.5.3)
    Requirement already satisfied: gmaps<0.10.0,>=0.9.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ny_artsy_date) (0.9.0)
    Requirement already satisfied: lxml<5.0.0,>=4.7.1 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ny_artsy_date) (4.7.1)
    Requirement already satisfied: requests<3.0.0,>=2.26.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ny_artsy_date) (2.26.0)
    Requirement already satisfied: six in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from gmaps<0.10.0,>=0.9.0->ny_artsy_date) (1.16.0)
    Requirement already satisfied: geojson>=2.0.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from gmaps<0.10.0,>=0.9.0->ny_artsy_date) (2.5.0)
    Requirement already satisfied: ipython>=5.3.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from gmaps<0.10.0,>=0.9.0->ny_artsy_date) (7.30.1)
    Requirement already satisfied: ipywidgets>=7.0.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from gmaps<0.10.0,>=0.9.0->ny_artsy_date) (7.6.5)
    Requirement already satisfied: traitlets>=4.3.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from gmaps<0.10.0,>=0.9.0->ny_artsy_date) (5.1.1)
    Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (3.0.24)
    Requirement already satisfied: pickleshare in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.7.5)
    Requirement already satisfied: backcall in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.2.0)
    Requirement already satisfied: pygments in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (2.10.0)
    Requirement already satisfied: setuptools>=18.5 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (58.0.4)
    Requirement already satisfied: pexpect>4.3 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (4.8.0)
    Requirement already satisfied: appnope in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.1.2)
    Requirement already satisfied: jedi>=0.16 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.18.1)
    Requirement already satisfied: matplotlib-inline in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.1.3)
    Requirement already satisfied: decorator in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (5.1.0)
    Requirement already satisfied: widgetsnbextension~=3.5.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (3.5.2)
    Requirement already satisfied: ipython-genutils~=0.2.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.2.0)
    Requirement already satisfied: ipykernel>=4.5.1 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (6.6.0)
    Requirement already satisfied: jupyterlab-widgets>=1.0.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (1.0.2)
    Requirement already satisfied: nbformat>=4.2.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (5.1.3)
    Requirement already satisfied: debugpy<2.0,>=1.0.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipykernel>=4.5.1->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (1.5.1)
    Requirement already satisfied: tornado<7.0,>=4.2 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipykernel>=4.5.1->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (6.1)
    Requirement already satisfied: jupyter-client<8.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from ipykernel>=4.5.1->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (7.1.0)
    Requirement already satisfied: parso<0.9.0,>=0.8.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from jedi>=0.16->ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.8.3)
    Requirement already satisfied: pyzmq>=13 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from jupyter-client<8.0->ipykernel>=4.5.1->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (22.3.0)
    Requirement already satisfied: entrypoints in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from jupyter-client<8.0->ipykernel>=4.5.1->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.3)
    Requirement already satisfied: python-dateutil>=2.1 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from jupyter-client<8.0->ipykernel>=4.5.1->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (2.8.2)
    Requirement already satisfied: nest-asyncio>=1.5 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from jupyter-client<8.0->ipykernel>=4.5.1->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (1.5.4)
    Requirement already satisfied: jupyter-core>=4.6.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from jupyter-client<8.0->ipykernel>=4.5.1->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (4.9.1)
    Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from nbformat>=4.2.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (4.3.0)
    Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.2.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.18.0)
    Requirement already satisfied: attrs>=17.4.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.2.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (21.2.0)
    Requirement already satisfied: pytz>=2017.3 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from pandas<2.0.0,>=1.3.5->ny_artsy_date) (2021.3)
    Requirement already satisfied: ptyprocess>=0.5 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from pexpect>4.3->ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.7.0)
    Requirement already satisfied: wcwidth in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=5.3.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.2.5)
    Requirement already satisfied: iniconfig in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from pytest<7.0.0,>=6.2.5->ny_artsy_date) (1.1.1)
    Requirement already satisfied: pluggy<2.0,>=0.12 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from pytest<7.0.0,>=6.2.5->ny_artsy_date) (1.0.0)
    Requirement already satisfied: py>=1.8.2 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from pytest<7.0.0,>=6.2.5->ny_artsy_date) (1.11.0)
    Requirement already satisfied: packaging in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from pytest<7.0.0,>=6.2.5->ny_artsy_date) (21.3)
    Requirement already satisfied: toml in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from pytest<7.0.0,>=6.2.5->ny_artsy_date) (0.10.2)
    Requirement already satisfied: coverage[toml]>=5.2.1 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from pytest-cov<4.0.0,>=3.0.0->ny_artsy_date) (6.2)
    Requirement already satisfied: tomli in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from coverage[toml]>=5.2.1->pytest-cov<4.0.0,>=3.0.0->ny_artsy_date) (2.0.0)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from requests<3.0.0,>=2.26.0->ny_artsy_date) (1.26.7)
    Requirement already satisfied: certifi>=2017.4.17 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from requests<3.0.0,>=2.26.0->ny_artsy_date) (2021.10.8)
    Requirement already satisfied: idna<4,>=2.5 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from requests<3.0.0,>=2.26.0->ny_artsy_date) (3.3)
    Requirement already satisfied: charset-normalizer~=2.0.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from requests<3.0.0,>=2.26.0->ny_artsy_date) (2.0.9)
    Requirement already satisfied: notebook>=4.4.1 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (6.4.6)
    Requirement already satisfied: nbconvert in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (6.3.0)
    Requirement already satisfied: jinja2 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (3.0.3)
    Requirement already satisfied: terminado>=0.8.3 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.12.1)
    Requirement already satisfied: prometheus-client in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.12.0)
    Requirement already satisfied: Send2Trash>=1.8.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (1.8.0)
    Requirement already satisfied: argon2-cffi in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (21.3.0)
    Requirement already satisfied: argon2-cffi-bindings in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (21.2.0)
    Requirement already satisfied: cffi>=1.0.1 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from argon2-cffi-bindings->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (1.15.0)
    Requirement already satisfied: pycparser in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (2.21)
    Requirement already satisfied: MarkupSafe>=2.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from jinja2->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (2.0.1)
    Requirement already satisfied: defusedxml in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.7.1)
    Requirement already satisfied: nbclient<0.6.0,>=0.5.0 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.5.9)
    Requirement already satisfied: pandocfilters>=1.4.1 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (1.5.0)
    Requirement already satisfied: bleach in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (4.1.0)
    Requirement already satisfied: testpath in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.5.0)
    Requirement already satisfied: mistune<2,>=0.8.1 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.8.4)
    Requirement already satisfied: jupyterlab-pygments in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.1.2)
    Requirement already satisfied: webencodings in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.5.0->ipywidgets>=7.0.0->gmaps<0.10.0,>=0.9.0->ny_artsy_date) (0.5.1)
    Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/lib/python3.9/site-packages (from packaging->pytest<7.0.0,>=6.2.5->ny_artsy_date) (3.0.6)
    [33mWARNING: You are using pip version 21.2.4; however, version 21.3.1 is available.
    You should consider upgrading via the '/Users/ConnieXu/Library/Caches/pypoetry/virtualenvs/ny-artsy-date-Bd2ND-kG-py3.9/bin/python3.9 -m pip install --upgrade pip' command.[0m


## General Usage

The functions within (in particular, `find_my_art_events` and `choose_my_art_date`) only work for locations in the New York Metro area. 


```python
import os
API_KEY = os.getenv('POETRY_GMAPS_TOKEN')
```

Each function also includes docstrings, which can be accessed through the use of the `help` function. 


```python
help(nydate.find_my_art_events)
```

    Help on function find_my_art_events in module ny_artsy_date.ny_artsy_date:
    
    find_my_art_events(my_location=None, google_maps_key=None, lat=None, lon=None, free_only=0, max_results=10, search_range='500m', mapping=False)
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
                    Default: 10
                search_range(str/float): distance (in meters) from location for events queried - can be '500m',"1000m","1500m","3000m"
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
    


## Functions 

This section includes a description, discusssion of input variables, and use case examples. **Unless specified otherwise, please follow the syntax within and make sure you are defining the parameters you are inputting** (e.g., `my_location = XYZ`) 

The main functions used are `find_my_art_events`, `find_my_dinner`, and `choose_my_art_date`. 

### General Parameters

The following are the default parameters that are needed for all three functions, as the package functions are primarily based on **location** and closeness. 

* **my_location**: String data for the address of your starting point 
* **google_maps_key**: You will need to have a valid [google maps token](https://developers.google.com/maps) to access the full range of these functions, as this key allows us to: 
    * geocode our data (if you are using locational data)
    * perform reverse geocoding functions  
    * return nearby restaurants with Google Places
    * map the returned points for events 
* **lon** and **lat** data of your starting point (can sometimes be used in lieu of **my_location**) 

### `find_my_art_events`

`find_my_art_events` finds art events within a radius of a starting location using [NY Art Beats API](https://www.nyartbeat.com/resources/doc/api). In order to run this function, you need **either** **my_location** (and **google_maps_key**) or **lat** and **lon**. 


Because you can choose one or the other (or both), these arguments have no default are not required parameters. **However, failure to input eiether of these parameters will prevent this function from working.** 

Below are one basic use case with **my_location** and another with **lat and long**: 


```python
df = nydate.find_my_art_events(my_location = 'Wall Street', google_maps_key = API_KEY)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Event_Name</th>
      <th>Event_Description</th>
      <th>DateEnd</th>
      <th>Distance</th>
      <th>Event_Lat</th>
      <th>Event_Lon</th>
      <th>Event_Price_Adult</th>
      <th>url</th>
      <th>Event_Price_Detailed</th>
      <th>Event_Address</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alteronce Gumby “On Earth as It Is in Heaven” ...</td>
      <td>Art-in-Buildings presents two new exhibitions ...</td>
      <td>2021-12-23</td>
      <td>226.022773</td>
      <td>40.706486</td>
      <td>-74.006211</td>
      <td></td>
      <td>http://www.nyartbeat.com/event/2021/1424</td>
      <td>NaN</td>
      <td>150 Water St, New York, NY 10005, USA</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = nydate.find_my_art_events(lat = 40.7425, lon = -74.0060)
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Event_Name</th>
      <th>Event_Description</th>
      <th>DateEnd</th>
      <th>Distance</th>
      <th>Event_Lat</th>
      <th>Event_Lon</th>
      <th>Event_Price_Adult</th>
      <th>url</th>
      <th>Event_Price_Detailed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Maria Lassnig “The Paris Years, 1960–68”</td>
      <td>Petzel presents Maria Lassnig: The Paris Years...</td>
      <td>2021-12-17</td>
      <td>193.378675</td>
      <td>40.744239</td>
      <td>-74.005967</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/F832</td>
      <td>Free</td>
    </tr>
    <tr>
      <th>1</th>
      <td>“Rested” Exhibition</td>
      <td>Nicola Vassell Gallery presents Rested, a grou...</td>
      <td>2022-01-08</td>
      <td>263.887846</td>
      <td>40.744873</td>
      <td>-74.006051</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/835B</td>
      <td>Free</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rene Ricard “Growing Up in America”</td>
      <td>Vito Schnabel Gallery presents Rene Ricard: Gr...</td>
      <td>2021-12-18</td>
      <td>294.294850</td>
      <td>40.745089</td>
      <td>-74.005274</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/EB40</td>
      <td>Free</td>
    </tr>
    <tr>
      <th>3</th>
      <td>“In Support” Exhibition</td>
      <td>The Kitchen presents In Support, a group exhib...</td>
      <td>2022-03-12</td>
      <td>312.613252</td>
      <td>40.745308</td>
      <td>-74.006186</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/DC0C</td>
      <td>Free</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Neo Rauch “The Signpost”</td>
      <td>David Zwirner presents The Signpost, an exhibi...</td>
      <td>2021-12-18</td>
      <td>331.544540</td>
      <td>40.745461</td>
      <td>-74.006464</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/1EE0</td>
      <td>Free</td>
    </tr>
  </tbody>
</table>
</div>



You can also refine your search, filtering for **free_only**, **search_range**, or **max_results**.
* **free_only**: Boolean logic specifying whether the user wants only to look at free events (incl. events with suggested donations). 
* **search_range**: Specifies how far from your starting point in meters (can be "500m","1000m","1500m","3000m", default at 500m). 
* **max_results**: Specifies maximum number of output you would want returned (can be 5,10,20,50, with default at 10). 

For example, in the case of chelsea market, the default (with the location and key) is as shown below:  


```python
df = nydate.find_my_art_events(my_location = 'Chelsea Market', google_maps_key = API_KEY)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Event_Name</th>
      <th>Event_Description</th>
      <th>DateEnd</th>
      <th>Distance</th>
      <th>Event_Lat</th>
      <th>Event_Lon</th>
      <th>Event_Price_Adult</th>
      <th>url</th>
      <th>Event_Price_Detailed</th>
      <th>Event_Address</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>Neo Rauch “The Signpost”</td>
      <td>David Zwirner presents The Signpost, an exhibi...</td>
      <td>2021-12-18</td>
      <td>337.384190</td>
      <td>40.745461</td>
      <td>-74.006464</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/1EE0</td>
      <td>Free</td>
      <td>456 W 18th St, New York, NY 10011, USA</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Portia Zvavahera “Ndakaoneswa murima”</td>
      <td>David Zwirner presents Ndakaoneswa murima, an ...</td>
      <td>2021-12-18</td>
      <td>337.384190</td>
      <td>40.745461</td>
      <td>-74.006464</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/9D69</td>
      <td>Free</td>
      <td>456 W 18th St, New York, NY 10011, USA</td>
    </tr>
    <tr>
      <th>7</th>
      <td>“The Whitney’s Collection: Selections from 190...</td>
      <td>This exhibition of more than 120 works, drawn ...</td>
      <td>2022-05-07</td>
      <td>395.154089</td>
      <td>40.739653</td>
      <td>-74.008850</td>
      <td>22</td>
      <td>http://www.nyartbeat.com/event/2020/16BE</td>
      <td>General admission: $22; Seniors/Students: $18;...</td>
      <td>456 W 18th St, New York, NY 10011, USA</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Jasper Johns “Mind/Mirror”</td>
      <td>The radical, inventive art of Jasper Johns (b....</td>
      <td>2022-02-13</td>
      <td>395.154089</td>
      <td>40.739653</td>
      <td>-74.008850</td>
      <td>22</td>
      <td>http://www.nyartbeat.com/event/2021/9034</td>
      <td>General admission: $22; Seniors/Students: $18;...</td>
      <td>456 W 18th St, New York, NY 10011, USA</td>
    </tr>
    <tr>
      <th>9</th>
      <td>“Labyrinth of Forms: Women and Abstraction, 19...</td>
      <td>The Whitney Museum of American Art presents La...</td>
      <td>2022-03-09</td>
      <td>395.154089</td>
      <td>40.739653</td>
      <td>-74.008850</td>
      <td>22</td>
      <td>http://www.nyartbeat.com/event/2021/5819</td>
      <td>General admission: $22; Seniors/Students: $18;...</td>
      <td>456 W 18th St, New York, NY 10011, USA</td>
    </tr>
  </tbody>
</table>
</div>



As we can see from the **Event_Price_Adult** and **Event_Price_Detailed** columns, specifying `free_only` as True or as 1 will filter out results that are not free. 


```python
df = nydate.find_my_art_events(my_location = 'Chelsea Market', google_maps_key = API_KEY, free_only = 1)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Event_Name</th>
      <th>Event_Description</th>
      <th>DateEnd</th>
      <th>Distance</th>
      <th>Event_Lat</th>
      <th>Event_Lon</th>
      <th>Event_Price_Adult</th>
      <th>url</th>
      <th>Event_Price_Detailed</th>
      <th>Event_Address</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Maria Lassnig “The Paris Years, 1960–68”</td>
      <td>Petzel presents Maria Lassnig: The Paris Years...</td>
      <td>2021-12-17</td>
      <td>198.808432</td>
      <td>40.744239</td>
      <td>-74.005967</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/F832</td>
      <td>Free</td>
      <td>456 W 18th St, New York, NY 10011, USA</td>
    </tr>
    <tr>
      <th>1</th>
      <td>“Rested” Exhibition</td>
      <td>Nicola Vassell Gallery presents Rested, a grou...</td>
      <td>2022-01-08</td>
      <td>269.415103</td>
      <td>40.744873</td>
      <td>-74.006051</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/835B</td>
      <td>Free</td>
      <td>456 W 18th St, New York, NY 10011, USA</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Rene Ricard “Growing Up in America”</td>
      <td>Vito Schnabel Gallery presents Rene Ricard: Gr...</td>
      <td>2021-12-18</td>
      <td>298.924224</td>
      <td>40.745089</td>
      <td>-74.005274</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/EB40</td>
      <td>Free</td>
      <td>456 W 18th St, New York, NY 10011, USA</td>
    </tr>
    <tr>
      <th>3</th>
      <td>“In Support” Exhibition</td>
      <td>The Kitchen presents In Support, a group exhib...</td>
      <td>2022-03-12</td>
      <td>318.248758</td>
      <td>40.745308</td>
      <td>-74.006186</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/DC0C</td>
      <td>Free</td>
      <td>456 W 18th St, New York, NY 10011, USA</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Neo Rauch “The Signpost”</td>
      <td>David Zwirner presents The Signpost, an exhibi...</td>
      <td>2021-12-18</td>
      <td>337.384190</td>
      <td>40.745461</td>
      <td>-74.006464</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/1EE0</td>
      <td>Free</td>
      <td>456 W 18th St, New York, NY 10011, USA</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Portia Zvavahera “Ndakaoneswa murima”</td>
      <td>David Zwirner presents Ndakaoneswa murima, an ...</td>
      <td>2021-12-18</td>
      <td>337.384190</td>
      <td>40.745461</td>
      <td>-74.006464</td>
      <td>0</td>
      <td>http://www.nyartbeat.com/event/2021/9D69</td>
      <td>Free</td>
      <td>456 W 18th St, New York, NY 10011, USA</td>
    </tr>
  </tbody>
</table>
</div>



Meanwhile, we can see that the max number of results is actually much closer than 20 than 10 with the default radius and address - when setting the max results to 50, we can see far more rows iin the df. 


```python
df = nydate.find_my_art_events(my_location = 'Chelsea Market', google_maps_key = API_KEY, max_results = 50)
df.tail()
```

The number of observations often also increases as we increase the radius or the `search_range` parameter. 


```python
df = nydate.find_my_art_events(my_location = 'Chelsea Market', google_maps_key = API_KEY, search_range = 1000, max_results=50)
df.tail()
```

### `find_my_dinner`

This function can be used alone *or* in tandem with `find_my_art_events`. By inputting a starting point (either your home, a meeting place, or the art event the user went to earlier in the day), the user can return a data table with relevant information about dinner places within a specified search radius from [Google Places (Google Maps API)](https://developers.google.com/maps/documentation/places/web-service/overview)



```python
df = nydate.find_my_dinner(my_location = 'Met Museum', google_maps_key = API_KEY)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Restaurant_Name</th>
      <th>Price_Level</th>
      <th>Restaurant_Rating</th>
      <th>Restaurant_Address</th>
      <th>Restaurant_Lat</th>
      <th>Restaurant_Lon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>Sistina</td>
      <td>$$$</td>
      <td>4.5</td>
      <td>24 E 81st St, New York</td>
      <td>40.777609</td>
      <td>-73.961677</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Due</td>
      <td>$$</td>
      <td>4.4</td>
      <td>1396 3rd Ave #1, New York</td>
      <td>40.774695</td>
      <td>-73.957313</td>
    </tr>
    <tr>
      <th>8</th>
      <td>The Loeb Boathouse Central Park</td>
      <td>$$$</td>
      <td>4.4</td>
      <td>Park Drive North, E 72nd St, New York</td>
      <td>40.775331</td>
      <td>-73.968734</td>
    </tr>
    <tr>
      <th>9</th>
      <td>The Simone</td>
      <td>nan</td>
      <td>4.7</td>
      <td>151 E 82nd St, New York</td>
      <td>40.776866</td>
      <td>-73.956948</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Toloache</td>
      <td>$$$</td>
      <td>4.5</td>
      <td>166 E 82nd St #2b, New York</td>
      <td>40.776482</td>
      <td>-73.956708</td>
    </tr>
  </tbody>
</table>
</div>



This function is similar to the previous one in that one can filter for the search radius (also called the **search_range**); this search_range (if used alone) is less restrictive due to the scope of Google Places. However, one can also filter for the minimum rating of the restaurant (**min_rating**), which is on a five-star scale. 

The default **min_rating** is 4.3. 


```python
df = nydate.find_my_dinner(my_location = 'Met Museum', google_maps_key = API_KEY, min_rating = 4.6)
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Restaurant_Name</th>
      <th>Price_Level</th>
      <th>Restaurant_Rating</th>
      <th>Restaurant_Address</th>
      <th>Restaurant_Lat</th>
      <th>Restaurant_Lon</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HUSO</td>
      <td>nan</td>
      <td>4.9</td>
      <td>1067 Madison Ave, New York</td>
      <td>40.777392</td>
      <td>-73.961169</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Simone</td>
      <td>nan</td>
      <td>4.7</td>
      <td>151 E 82nd St, New York</td>
      <td>40.776866</td>
      <td>-73.956948</td>
    </tr>
  </tbody>
</table>
</div>



### `choose_my_art_date`

This function randomly chooses an 'artsy date' event-restaurant combo based on the user's starting point. The assumption of this function is that one will go to dinner *after* the date, and uses the event location to then reccomend a nearby restaurant.  

To this point, the input parameters include **lat** and **lng** or **my_location**. Similar to the earlier functions, the user can also input **search_range** and **min_rating**. (Once more, **google_maps_key** is necessary). 


```python
df = nydate.choose_my_art_date(my_location = 'Hudson Yards', google_maps_key = API_KEY)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Field</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Event_Name</td>
      <td>Wu Chi-Tsung “jing-atmospheres”</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Event_Description</td>
      <td>Sean Kelly presents jing-atmospheres, Wu Chi-T...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DateEnd</td>
      <td>2021-12-18</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Distance</td>
      <td>450.904862</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Event_Lat</td>
      <td>40.756241</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Event_Lon</td>
      <td>-73.998131</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Event_Price_Adult</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>url</td>
      <td>http://www.nyartbeat.com/event/2021/6620</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Event_Price_Detailed</td>
      <td>Free</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Event_Address</td>
      <td>314 11th Ave, New York, NY 10001, USA</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Restaurant_Name</td>
      <td>At Nine Restaurant &amp; Bar</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Price_Level</td>
      <td>$$</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Restaurant_Rating</td>
      <td>4.4</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Restaurant_Address</td>
      <td>592 9th Ave, New York</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Restaurant_Lat</td>
      <td>40.758694</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Restaurant_Lon</td>
      <td>-73.992056</td>
    </tr>
  </tbody>
</table>
</div>



As we can see, this function returns as a long table with all the information you may be interested in;  
most of the fields returned are delineated by Event details and Restaurant details.

### `mapping` parameter

Within all three functions, one can toggle the **mapping** parameter. This parameter is input as a boolean response (True/False or 0/1) and returns an interactive google map[<sup>1</sup>](#fn1) with places of interest. See below for a couple of use cases of mapping. 


```python
df,maps = nydate.find_my_art_events(my_location = 'Met Museum', \
                                google_maps_key = API_KEY, mapping = 1)
maps
```


    Figure(layout=FigureLayout(height='420px'))



```python
df,maps = nydate.choose_my_art_date(my_location = 'Chelsea Market', \
                                google_maps_key = API_KEY, search_range = 1000,mapping = 1)
```


```python
maps
```


    Figure(layout=FigureLayout(height='420px'))


The interactive maps above include points that show the name of the locations returned by our data. Starting point is indicated in blue, and the markers show the locations of the restaurants and events of interest. 

---
<span id="fn1"> <sup>1</sup> obtained with the [gmaps](https://pypi.org/project/gmaps/) package and using the supporting map_events function of the package) </span>

