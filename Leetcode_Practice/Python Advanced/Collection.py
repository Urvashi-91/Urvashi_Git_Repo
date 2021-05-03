'''
ChainMap: A ChainMap is a class that provides the ability to link multiple mappings together such that they end up being a single unit.

'''
import argparse
import os

from collections import ChainMap


def main():
    app_defaults = {'username':'admin', 'password':'admin'}

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    command_line_arguments = {key:value for key, value
                              in vars(args).items() if value} #vars(args) equals args.__dict__.

    chain = ChainMap(command_line_arguments, os.environ,
                     app_defaults)
    print(chain['username'])

if __name__ == '__main__':
    main()
    os.environ['username'] = 'test'
    main()