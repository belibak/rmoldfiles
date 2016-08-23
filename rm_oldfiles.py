#!/usr/bin/env python3
import os, sys, time, shutil, argparse

Dir = '/home/white/tmp/'
oldest = 30

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="Directory to clear")
parser.add_argument('-a', "--age", help = "Files will be removed oldest than -a days")
args = parser.parse_args()

if args.directory:
    print(args.directory)
    Dir = args.directory
if args.age:
    try:
        oldest = int(args.age)
    except ValueError:
        print("Option -a must be integer") 
    
    
if Dir[-1] != '/':
    Dir = Dir + '/'
dirs = [Dir]

for cat in dirs:
    print(cat)
    lst = os.listdir(cat)
    nowtime = round(time.time(), 1)
    print(nowtime)
    for i in lst:
        ctime=os.stat(cat+i)
        file = cat+i
        howold = nowtime - int(ctime[9])
        howold = round(howold/60/60/24, 1)
        if howold > oldest:
            if os.path.isdir(cat+i):
                try:
                    shutil.rmtree(cat+i)
                    print('Directory Removed: %s -- age: %s days' %(cat+i, howold))
                except:
                    print('%s Ошибка удаления, отказано в доступе!' %(file))
            else:
                os.remove(cat+i)
                print('File Removed: %s -- age: %s days' %(cat+i, howold))
        else:
            print('NOT removed %s . Age: %s' %(file, howold))
        #print(ctime[9])
#input('Закончено, жми enter: ')

