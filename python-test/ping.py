import os
import sys

def ping():
    response = os.system('nc -vz localhost 9090')
    if response == 0:
        sys.exit(0)
    else:
        raise Exception('unable to connect')

def main():
    print ("trying to connect..")
    ping()

if __name__ == '__main__':
    main()