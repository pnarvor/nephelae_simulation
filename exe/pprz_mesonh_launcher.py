#! /usr/bin/python3

import os
import sys
sys.path.append('../')
import signal
import argparse
from mesonh_probe import PPRZMesoNHLauncher

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mesonh-variables", nargs='+',
                    help="String id of variable to read in the mesonh files")
parser.add_argument("-f", "--mesonh-files", nargs='+',
                    help="MesoNH files to fly the simulated UAV into")
args = parser.parse_args()
print("MesoNH variables : ", args.mesonh_variables)
print("MesoNH files     : ", args.mesonh_files)

if args.mesonh_variables is None:
    raise Exception("Argument error : Mush give at leat one mesonh variable. "
                     "See \"--help\" for details.")
if args.mesonh_files is None:
    raise Exception("Argument error : Mush give at leat one mesonh file. "
                     "See \"--help\" for details.")

launcher = PPRZMesoNHLauncher(args.mesonh_files, args.mesonh_variables)


def signal_handler(signal, frame):
    launcher.stop()
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)

signal.pause()
