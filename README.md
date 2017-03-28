# WATPLANET?!

***Dude what's that planet in my image?!***


### Installation
If you have a working installation of Python on your system,
you can download and install the latest version as follows:
```
$ git clone https://github.com/barentsen/watplanet.git
$ cd watplanet
$ python setup.py install
```


### Usage
```
$ watplanet --help
usage: watplanet [-h] [-r [degrees]] fitsfile x y timestamp

WATPLANET?!

positional arguments:
  fitsfile              Path to a FITS file.
  x                     FITS pixel x coordinate.
  y                     FITS pixel y coordinate.
  timestamp             ISO timestamp, example 2017-01-01T12:00:00.

optional arguments:
  -h, --help            show this help message and exit
  -r [degrees], --radius [degrees]
                        Search radius (degrees).
```
