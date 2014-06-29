"""
A very basic progress bar with no external library dependencies.
"""
import sys
from string import Formatter

class SimpleBar(object):
    """A minimal progress bar widget for stdout.

    Displays a custom message to sys.stdout, and updates it in-place on demand.
    """

    def __init__(self, message_str=None, max_width=80):
        """Create a SimpleBar with an optional message string.

        Args:
        message_str(str): An optional format string that is displayed and formatted
        in every update operation.
        max_width(int): The maximum width of the progress bar, message and all.

        """
        self.formatter = Formatter()
        if message_str:
            self.message_str = message_str
        self.max_width = max_width


    def update_args(self, *args):
        """Display the appropriately updated progress message.

        Args:
        args: Formatter-style arguments for the format string.
        """
        self.__restart_line()
        print self.__pad_string(self.formatter.format(self.message_str, *args),
                              self.max_width),

    def update(self, string, *args):
        """Update progress message and display with appropriate updates.

        Args:
        string (str): The format string for the message to be displayed.
        args (optional arguments): Formatter-style arguments for the format string.
        """
        self.message_str = string
        self.update_args(*args)

        
    def __restart_line(self):
        """Move cursor to the start of the current line immediately.
        """
        sys.stdout.write('\r')
        sys.stdout.flush()

    def __pad_string(self, s, length):
        """Pad a string with trailing spaces to the given length.
        """
        return s.ljust(length)
        


        
