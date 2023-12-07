#!/usr/bin/env python3
# lib/a_type_error.py
try:
    wrong_type = int('abc') + 123  
except ValueError as e:
    print(f"ValueError: {e}")

