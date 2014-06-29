import sys

from string import Formatter


class SimpleBar(object):

    def __init__(self, message_str=None):
        self.formatter = Formatter()
        if message_str:
            self.message_str = message_str

    def restart_line(self):
        sys.stdout.write('\r')
        sys.stdout.flush()


    def update(self, message_args):
        print self.formatter.format(self.message_str, message_args),
        self.restart_line()

        
