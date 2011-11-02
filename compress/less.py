# LESS Compile wrapper for Django-Compress
#
# Copyright 2011, GNF
# Authors: Marc Leglise
#
# This file is invoked from compress.utils.filter_css
# It relies on having the binary executable 'lessc' available on the PATH

import os

from django.conf import settings
from compress.utils import compress_root, save_file

BINARY = getattr(settings, 'LESS_BINARY', 'lessc')
ARGUMENTS = getattr(settings, 'LESS_ARGUMENTS', '')

def compile_less(infile, outfile, verbosity=0):
    command = '%s %s %s > %s' % (BINARY, ARGUMENTS, compress_root(infile), compress_root(outfile))
    if verbosity >= 1:
        print command
    command_output = os.popen(command).read()
    
    return
    