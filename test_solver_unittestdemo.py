"""
Usage:  python -m unittest test_solver_unittestdemo
"""

from unittest import TestCase
from solver_unittestdemo import Solver

__author__ = 'df'

class TestSolver(TestCase):
    def test_negative_discr(self):
        s = Solver
        self.assertRaises(Exception, s.demo, 2, 1, 2)
