# test_consoleraft.py
"""
Tests for ConsoleRaft module.
"""

import unittest
from consoleraft import ConsoleRaft

class TestConsoleRaft(unittest.TestCase):
    """Test cases for ConsoleRaft class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ConsoleRaft()
        self.assertIsInstance(instance, ConsoleRaft)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ConsoleRaft()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
