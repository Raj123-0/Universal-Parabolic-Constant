[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

===============================================================================
PROJECT: Universal Parabolic Constant Computation Engine
===============================================================================

OVERVIEW:
Calculates the Universal Parabolic Constant (P_2 ≈ 2.295587149392638074034...) to 
arbitrary precision (N digits). P_2 is a fundamental geometric constant analogous to pi 
for circles.

ALGORITHM & MATHEMATICS:
- Closed-Form Logarithmic Square Root Formula:
    P_2 = ln(1 + sqrt(2)) + sqrt(2)
- Evaluates using high-precision logarithmic routines in mpmath + gmpy2.

## Usage

```bash
python "Universal Parabolic Constant.py" --help
```
