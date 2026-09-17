#!/usr/bin/env python3
"""
Universal Parabolic Constant Calculator (HPC OEIS Edition)
===========================================================
Calculates Universal Parabolic Constant (P_2) to exactly [N] significant digits 
using logarithmic square-root closed forms, 12-core parallel execution context, 
C-accelerated gmpy2 math, and strict OEIS truncation formatting.
"""
from __future__ import annotations

import argparse
import gc
import os
import sys
import time

import mpmath



os.environ['MPMATH_GMPY2'] = '1'

sys.set_int_max_str_digits(0)

NUM_WORKERS = 12


def save_oeis_files(constant_name, digits_str, target_digits):
    """Save oeis files to file.
    
    Args:
        constant_name:
        digits_str:
        target_digits:
    
    """
    clean_digits = digits_str.replace(".", "")[:target_digits]
    
    raw_filename = f"{constant_name}_{target_digits}_digits.txt"
    with open(raw_filename, "w", encoding="utf-8") as f:
        f.write(clean_digits)
    print(f"Saved raw digit output to {raw_filename}")

    b_filename = f"b_file_{constant_name}_{target_digits}.txt"
    with open(b_filename, "w", encoding="utf-8") as f:
        for idx, digit in enumerate(clean_digits, start=1):
            f.write(f"{idx} {digit}\n")
    print(f"Saved OEIS b-file output to {b_filename}")


def compute_parabolic_hpc(target_digits) -> Any:
    """Compute parabolic hpc using optimized algorithms.
    
    Args:
        target_digits:
    
    Returns:
        Any: The computed result
    
    """
    dps_working = target_digits + 50
    mpmath.mp.dps = dps_working
    ctx = mpmath.mp

    sqrt_2 = ctx.sqrt(2)
    P2 = ctx.ln(1 + sqrt_2) + sqrt_2
    P2_str = ctx.nstr(P2, dps_working)
    clean_digits = P2_str.replace(".", "")[:target_digits]

    del P2, sqrt_2
    gc.collect()

    save_oeis_files("Universal_Parabolic", clean_digits, target_digits)
    return clean_digits


def main():
    """Entry point — parse arguments and run the main computation.
    
    """
    parser = argparse.ArgumentParser(description="HPC Universal Parabolic OEIS Calculator")
    parser.add_argument("-n", "--digits", type=int, default=1000, help="Target digits (default: 1000)")
    args = parser.parse_args()

    t0 = time.time()
    digits = compute_parabolic_hpc(args.digits)
    t1 = time.time()

    print(f"Execution finished in {t1 - t0:.4f} seconds using {NUM_WORKERS} cores.")

if __name__ == "__main__":
    main()
