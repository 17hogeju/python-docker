import socket
import os

from os import path
from enum import Enum

DATADIR = "/home/data/"
OUTDIR = "/home/output/"
OUTNAME = "result.txt"

class PrintFormat(Enum):
    CONSOLE = 1
    FILE = 2
    NONE = 3

class DockerScript:
    def print_help(self):
        print('****************************** Operations ***********************************')
        print('run: Runs all of the operations and puts the output in home/output/result.txt')
        print('list: List the names of all the files')
        print('count: Count the total number of words in all files')
        print('count-max: List the file name with the most words')
        print('find-ip: List the ip of your machine')
        print('*****************************************************************************')

    def dir_exists(self, dir_path):
        if not path.isdir(dir_path):
            print("Directory %s does not exist. Creating one now." % dir_path)
            try:
                os.mkdir(dir_path)
            except OSError:
                print ("Creation of the directory %s failed" % dir_path)
            else:
                print ("Successfully created the directory %s " % dir_path)


    def print_list(self, print_var):
        self.dir_exists(DATADIR)
        self.dir_exists(OUTDIR)
        files = os.listdir(DATADIR)
        if print_var == PrintFormat.FILE:
            fd = open(OUTDIR + OUTNAME, "w")
        if len(files) == 0:
            if print_var == PrintFormat.CONSOLE:
                print("No files exist in the data directory")
            else:
                fd.write("No files exist in the data directory\n")
        else:
            if print_var == PrintFormat.CONSOLE:
                print("File Names:")
            else:
                fd.write("File Names:\n")
        for file in files:
            if print_var == PrintFormat.CONSOLE:
                print(file)
            else:
                fd.write("%s\n" % file)
        if print_var == PrintFormat.FILE:
            fd.close()

    def count_all_files(self, print_var):
        self.dir_exists(DATADIR)
        self.dir_exists(OUTDIR)
        files = os.listdir(DATADIR)
        file_counts = {}
        total = 0

        if print_var == PrintFormat.FILE:
            fd = open(OUTDIR + OUTNAME, "a")
        if len(files) == 0:
            if print_var == PrintFormat.CONSOLE:
                print("No files exist in the data directory")
            elif print_var == PrintFormat.FILE:
                fd.write("No files exist in the data directory\n")
        for file in files:
            try:
                tmpfile = open(DATADIR + file, "rt")
                data = tmpfile.read()
                words = data.split()
                file_counts[file] = len(words)
                total += len(words)
            except IOError:
                if print_var == PrintFormat.CONSOLE:
                    print("Error opening and reading file: %s" % file)
                elif print_var == PrintFormat.FILE:
                    fd.write("Error opening and reading file: %s\n" % file)
        if print_var == PrintFormat.CONSOLE:
            print("Total words in all files: %s" % total)
        elif print_var == PrintFormat.FILE:
            fd.write("Total words in all files: %s\n" % total)
            fd.close
        return file_counts

    def get_max_file_count(self, print_var, file_counts):
        if file_counts:
            key = max(file_counts, key=file_counts.get)
            if print_var == PrintFormat.CONSOLE:
                print("Max file: %s - %s words" % (key, file_counts[key]))
            else:
                fd = open(OUTDIR + OUTNAME, "a")
                fd.write("Max file: %s - %s words\n" % (key, file_counts[key]))
                fd.close
        else:
            if print_var == PrintFormat.CONSOLE:
                print("No files exist in the data directory")
            else:
                fd = open(OUTDIR + OUTNAME, "a")
                fd.write("No files exist in the data directory\n")
                fd.close
    
    def find_ip(self, print_var):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        if print_var == PrintFormat.CONSOLE:
            print("ip: %s" % ip)
        else:
            fd = open(OUTDIR + OUTNAME, "a")
            fd.write("ip: %s\n" % ip)
            fd.close

def main():
    exit_status = False
    file_counts = {}
    ds = DockerScript()
    # print('Welcome to PyDock!')
    # print('This program allows you to execute file operations within the folder: home/data')
    # print("To get a list of available operations, type 'help'")
    # print("To exit this program, type 'exit'")
    # while(exit_status == False):
    #     usr_response = input('>> ')
    #     if usr_response == 'exit':
    #         exit_status = True
    #     elif usr_response == 'help':
    #         ds.print_help()
    #     elif usr_response == 'list':
    #         ds.print_list(PrintFormat.CONSOLE)
    #     elif usr_response == 'run':
    ds.print_list(PrintFormat.FILE)
    file_counts = ds.count_all_files(PrintFormat.FILE)
    ds.get_max_file_count(PrintFormat.FILE, file_counts)
    ds.find_ip(PrintFormat.FILE)
    read_file = open (OUTDIR + OUTNAME,"r")
    strings = read_file.read()
    print (strings)
        # elif usr_response == 'count':
        #     file_counts = ds.count_all_files(PrintFormat.CONSOLE)
        # elif usr_response == 'count-max':
        #     if file_counts:
        #         ds.get_max_file_count(PrintFormat.CONSOLE, file_counts)
        #     else:
        #         file_counts = ds.count_all_files(PrintFormat.NONE)
        #         ds.get_max_file_count(PrintFormat.CONSOLE, file_counts)
        # elif usr_response == 'find-ip':
        #     ds.find_ip(PrintFormat.CONSOLE)
        # else:
        #     print("Operation not found. Type 'help' for a list of available operations.")

if __name__ == "__main__":
    main()