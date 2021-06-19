class DockerScript:
    def print_help(self):
        print('run: Runs all of the operations and puts the output in home/output/result.txt')
        print('list: List the names of all the files')
        print('count: Count the total number of words in all files')
        print('file-max: List the file name with the most words')
        print('find-ip: List the ip of your machine')

def main():
    exit_status = False
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

if __name__ == "__main__":
    main()