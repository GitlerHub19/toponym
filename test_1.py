from mygeocoder import *
from mymapapi import *
import sys


def main():
    to_find = ' '.join(sys.argv[1:])
    if to_find:
        ll, spn = get_spn(to_find)
        the_coolest_one = '{}&spn={}'.format(ll, spn)
        c = get_coordinates(to_find)
        the_garden = 'pt={},{},pmwtm1'.format(c[0], c[1])
        show_map(the_coolest_one, 'sat', the_garden)
    

if __name__ == '__main__':
    main()