from astropy.io import fits
from astropy.wcs import WCS
from astropy.table import Table
import argparse
import urllib

INPUT_FN = '../sandbox/f242_e0_c98.fits'
TIMESTAMP = '2015-01-01T00:00:00'
X = 50
Y = 60
SR = 0.1


def skybot_url(ra, dec, epoch, sr):
    url = "http://vo.imcce.fr/webservices/skybot/skybotconesearch_query.php?EPOCH={}&RA={}&DEC={}&SR={}".format(epoch, ra, dec, sr)
    return url


def identify_body(ra, dec, epoch, radius):
    """Returns name and number if a body is known."""
    url = skybot_url(ra, dec, epoch, radius)
    try:
        t = Table.read(url)
        return t[0]['name'].decode("utf-8"), t[0]['num'].decode("utf-8")
    except ValueError:
        return "NOTFOUND", "NOTFOUND"
    except urllib.error.URLError:
        return "URLERROR", "URLERROR"
    except:
        return "ERROR", "ERROR"


def watplanet_main(args=None):
    parser = argparse.ArgumentParser(description="WATPLANET?!")
    parser.add_argument("-r", "--radius", metavar='degrees',
                        nargs="?", type=float, default=0.01,
                        help="Search radius (degrees).")
    parser.add_argument('fitsfile', nargs=1,
                        help="Path to a FITS file.")
    parser.add_argument('x', nargs=1, type=float,
                        help="FITS pixel x coordinate.")
    parser.add_argument('y', nargs=1, type=float,
                        help="FITS pixel y coordinate.")
    parser.add_argument('timestamp', nargs=1,
                        help="ISO timestamp, example 2017-01-01T12:00:00.")
    args = parser.parse_args(args)

    x, y = float(args.x[0]), float(args.y[0])
    f = fits.open(INPUT_FN)
    mywcs = WCS(f[0].header)
    ra, dec = mywcs.all_pix2world([[x, y]], 0)[0]
    name, num = identify_body(ra, dec, args.timestamp, args.radius)
    print('(ra, dec) = ({}, {})'.format(ra, dec))
    print('Search radius: {:.0f} arcsec'.format(args.radius * 3600))
    print('Object name: {}  (number: {})'.format(name, num))


if __name__ == '__main__':
    watplanet_main()
