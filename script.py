import socket
import sys
import os

from os import path


class DockerScript:
    def print_help(self):
        print('****************************** Operations ***********************************')
        print('run: Runs all of the operations and puts the output in home/output/result.txt')
        print('list: List the names of all the files')
        print('count: Count the total number of words in all files')
        print('file-max: List the file name with the most words')
        print('find-ip: List the ip of your machine')
        print('*****************************************************************************')

    def data_dir_exists(self):
        if not path.isdir("/home/data/"):
            print("Path: /home/data/ does not exist. Creating one now.")
            os.mkdir("/home/data/")
            print("Data directory created")


    def print_list(self, in_path, out_path):
        self.data_dir_exists()


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
        usr_response = input('')
        if usr_response == 'exit':
            exit_status = True
        elif usr_response == 'help':
            ds.print_help()
        elif usr_response == 'list':
            ds.print_list(in_path, out_path)
        else:
            print("Operation not found. Type 'help' for a list of available operations.")

if __name__ == "__main__":
    main()