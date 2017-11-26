#!/usr/bin/env python
import argparse
import numpy

class StatsTool(object):
    def __init__(self):
        self._parse_args()
        
    def _parse_args(self):
        parser = argparse.ArgumentParser()
        
        
        parser.add_argument('--load-from-file', required=False, dest='datafile",
                            default=None,
                            help="Load data from the specified file. Data should be "
                                 "formatted in columns (ASCII format). The number of "
                                 "columns should match the required number of datasets "
                                 "for the specified analysis.  See analysis options "
                                 "for details."
                           )
        parser.add_argument('--
