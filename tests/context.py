import os
import sys

# Add the project root path to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import project so that other tests can access it
import dotlink
