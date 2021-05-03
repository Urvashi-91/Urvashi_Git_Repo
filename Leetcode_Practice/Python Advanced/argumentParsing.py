'''
Argument: Argument is input that you feed to the program or command to respond.
Parsing: When you hit ls -l the OS parses it in a certain way under the hood.
Reference Link: https://www.datacamp.com/community/tutorials/argument-parsing-in-python

'''
# arg_demo.py

import argparse


def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )
    return parser.parse_args()

if __name__ == '__main__':
    get_args()


'''
Adding More Arguments
'''
# arg_demo2.py

import argparse


def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    # required argument
    parser.add_argument('-x', action="store", required=True,
                        help='Help text for option X')
    # optional arguments
    parser.add_argument('-y', help='Help text for option Y', default=False)
    parser.add_argument('-z', help='Help text for option Z', type=int)
    print(parser.parse_args())

if __name__ == '__main__':
    get_args()


'''
Adding a Long Option '--execute'
'''
parser.add_argument('-x', '--execute', action='store', required=True,
                    help='Help text for option X')


'''
Adding constraint where one option cannot be passed with another option
group = parser.add_mutually_exclusive_group()
'''
import argparse


def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-x', '--execute', action="store",
                        help='Help text for option X')
    group.add_argument('-y', help='Help text for option Y', default=False)

    parser.add_argument('-z', help='Help text for option Z', type=int)
    print(parser.parse_args())

if __name__ == '__main__':
    get_args()