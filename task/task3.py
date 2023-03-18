import sys
import argparse
import task2

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-p', '--path', default='C:/Users/TEMP')
    return parser 
 
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    task2.file_structure(namespace.path)