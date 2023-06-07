# Pi Calculation with BBP Formula

This repository contains a project that uses the [Bailey–Borwein–Plouffe (BBP) formula](https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula) to calculate π (pi) to 100 decimal places. This is achieved by usign the mpmath library to represent the digits beyond the float128 representation. 

The Included Jupyter notebook runs three different scripts as follows:

1. **serial-pi.py**: This script runs a serial implementation of the BBP algorithm to computer pi.
2.  **multiprocessing-pi.py**: This script implements the BBP formula in parallel using Python's multiprocessing library.
3.  **mpi-pi.py**: This script implements the BBP formula in parallel using OPENMPI. 

