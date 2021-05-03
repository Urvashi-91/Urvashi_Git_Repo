#!/usr/bin/env python
#A System Information Gathering Script
import subprocess

#Command 1
def uname_func():

    uname = "uname"
    uname_arg = "-a"
    print "Gathering system information with %s command:\n" % uname
    subprocess.call([uname, uname_arg])

#Command 2
def disk_func():

    diskspace = "df"
    diskspace_arg = "-h"
    print "Gathering diskspace information %s command:\n" % diskspace
    subprocess.call([diskspace, diskspace_arg])

#Command 3
def ls():
    subprocess.call(["ls", "-l"])

#Command 4
def dir_space():
    tmp_usage = "du"
    tmp_arg = "-h"
    print "Enter directory name "
    path = str.(input())
    print "Space used in /tmp directory"
    subprocess.call([tmp_usage, tmp_arg, path])

#Main function that call other functions
def main():
    uname_func()
    disk_func()
    ls()
    tmp_space()

main()