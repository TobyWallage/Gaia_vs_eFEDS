from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
from astropy.table import Table
from astropy.visualization import simple_norm
import astropy.units as u
import numpy as np
import matplotlib.pyplot as plt


def add_marker(wcs: WCS, ra: float, dec: float, ax, colour: str = 'red') -> None:
    x, y = wcs.world_to_pixel(SkyCoord(ra, dec, unit='deg'))
    ax.scatter(x, y, c='None', edgecolors=colour, s=100, alpha=0.8, lw=1)
    return


def mark_image(cluster_id: int, matches_table: Table, fits_path: str = 'OldStuff/eSASS images/Image_fits/') -> None:
    # get specific cluster data
    cluster = matches_table[matches_table['Cluster_ID_SRC'] == cluster_id]
    # read image fits file
    image, header = fits.getdata(
        fits_path+"image_"+str(cluster_id)+".fits", header=True)
    # get world coordinate info from fits header
    w = WCS(header)
    plt.figure(dpi=200)
    # create subplot with world coordinate system
    ax = plt.subplot(projection=w)
    # set units to degrees
    ax.coords[0].set_format_unit(u.deg)
    # label axis
    ax.coords[0].set_axislabel('Right Ascension')
    ax.coords[1].set_axislabel('Declination')
    # show image with log normalization
    ax.imshow(image, origin='lower', norm=simple_norm(image, 'log'))
    # title
    plt.title("eFEDS {ID} with quasars and eFEDS sources marked".format(
        ID=str(cluster["Cluster_ID_SRC"][0])))

    # crosshair on cluster location
    cx, cy = w.world_to_pixel(
        SkyCoord(cluster['Cluster_RA'][0], cluster['Cluster_DEC'][0], unit='deg'))
    ax.axvline(cx, c='white', alpha=0.4, lw=1.5)
    ax.axhline(cy, c='white', alpha=0.4, lw=1.5)

    # marker each source for cluster
    for source in cluster:
        add_marker(w, source['source_ra'], source['source_dec'], ax)
    # save image
    plt.savefig('cluster569.png', dpi=400,
                facecolor='white', bbox_inches='tight')
    plt.show()
    ...


if __name__ == '__main__':
    matches_table_path = 'Source_Data\eFEDS_gaia_match.csv'
    matches_table = Table.read(matches_table_path)
    mark_image(569, matches_table)
