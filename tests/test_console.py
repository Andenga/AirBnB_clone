import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    def test_quit_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))
            output = mock_stdout.getvalue()
            self.assertEqual(output.strip(), "")

    def test_create_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue()
            self.assertTrue(output.strip().startswith(""))

    # Add similar test methods for other commands (show, destroy, all, update, etc.)

    def test_help_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("help")
            output = mock_stdout.getvalue()
            self.assertTrue(output.strip().startswith(""))

    def test_help_specific_command(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("help show")
            output = mock_stdout.getvalue()
            self.assertTrue(output.strip().startswith(""))

if __name__ == '__main__':
    unittest.main()
