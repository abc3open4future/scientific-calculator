#!/usr/bin/env python3
"""Scientific Calculator CLI"""

import argparse
import math
import sys
from typing import Optional

class Calculator:
    """Scientific Calculator"""
    
    def __init__(self):
        self.operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else None,
            '**': lambda a, b: a ** b,
            'sqrt': lambda a, _: math.sqrt(a),
            'sin': lambda a, _: math.sin(math.radians(a)),
            'cos': lambda a, _: math.cos(math.radians(a)),
            'tan': lambda a, _: math.tan(math.radians(a)),
            'log': lambda a, _: math.log10(a) if a > 0 else None,
            'ln': lambda a, _: math.log(a) if a > 0 else None,
            'factorial': lambda a, _: math.factorial(int(a)) if a >= 0 else None,
        }
    
    def calculate(self, op: str, a: float, b: Optional[float] = None) -> Optional[float]:
        """Perform calculation"""
        if op in self.operators:
            result = self.operators[op](a, b if b is not None else 0)
            if result is None:
                print(f"Error: Invalid operation or domain error")
                return None
            return result
        print(f"Unknown operator: {op}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Scientific Calculator')
    parser.add_argument('operation', help='Operation: +, -, *, /, **, sqrt, sin, cos, tan, log, ln, factorial')
    parser.add_argument('a', type=float, help='First number')
    parser.add_argument('b', type=float, nargs='?', default=None, help='Second number (optional)')
    parser.add_argument('--repl', action='store_true', help='Start interactive REPL')
    
    args = parser.parse_args()
    
    calc = Calculator()
    
    if args.repl:
        print("Scientific Calculator REPL (type 'quit' to exit)")
        while True:
            try:
                expr = input("> ").strip()
                if expr.lower() == 'quit':
                    break
                parts = expr.split()
                if len(parts) >= 2:
                    op, a = parts[0], float(parts[1])
                    b = float(parts[2]) if len(parts) > 2 else None
                    result = calc.calculate(op, a, b)
                    if result is not None:
                        print(f"= {result}")
            except (ValueError, EOFError):
                break
    else:
        result = calc.calculate(args.operation, args.a, args.b)
        if result is not None:
            print(f"Result: {result}")

if __name__ == "__main__":
    main()
