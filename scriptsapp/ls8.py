#!/usr/bin/env python3
import getopt, sys

"""Main."""
from cpu import *

#cpu.load()
#cpu.run()

# all_command_args = sys.argv
#
# arg_list = all_command_args[1:]
#
# unixOptions = "f:h"
# gnuOptions = ["file=", "help"]
#
# try:
#     args, values = getopt.getopt(arg_list, unixOptions, gnuOptions)
#
# except getopt.error as err:
#         print(str(err))
#         sys.exit(2)
#
# for curr_arg, curr_val in args:
#     if curr_arg in ("-f", "--file"):
#         print(f'File to Load, {curr_val}')
#         cpu.load(curr_val)
#         cpu.run()
#     elif curr_arg in ("-h", "--help"):
#         print("Displaying the Help Information")

class Ls8:
    def __init__(self, program):
        self.cpu = CPU()
        self.program = program
        self.answer = None

    def run(self):
        self.cpu.load(self.program)
        self.cpu.run()
        self.answer = self.cpu.answer
        print(self.answer)




