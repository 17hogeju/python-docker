import socket
import sys
import os

from os import path

DATADIR = "/home/data/"
OUTDIR = "/home/output/"
OUTNAME = "result.txt"


class DockerScript:
    def print_help(self):
        print('****************************** Operations ***********************************')
        print('run: Runs all of the operations and puts the output in home/output/result.txt')
        print('list: List the names of all the files')
        print('count: Count the total number of words in all files')
        print('file-max: List the file name with the most words')
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
        if print_var:
            if len(files) == 0:
                print("No files exist in the data directory")
            for file in files:
                print(file)
        else:
            fd = os.open(OUTDIR + OUTNAME, "w")
            if len(files) == 0:
                fd.write("No files exist in the data directory")
            for file in files:
                fd.write(file + "\n")
            fd.close()

def main():
    exit_status = False
    usr_path = os.getcwd()
    in_path = usr_path + "/home/data/"
    out_path = usr_path + "/home/output/"
    ds = DockerScript()
    print('Welcome to PyDock!')
    print('This program allows you to execute file operations within the folder: home/data')
    print("To get a list of available operations, type 'help'")
    print("To exit this program, type 'exit'")
    while(exit_status == False):
        usr_response = input('>> ')
        if usr_response == 'exit':
            exit_status = True
        elif usr_response == 'help':
            ds.print_help()
        elif usr_response == 'list':
            ds.print_list(True)
        elif usr_response == 'run':
            ds.print_list(False)
        else:
            print("Operation not found. Type 'help' for a list of available operations.")

if __name__ == "__main__":
    main()