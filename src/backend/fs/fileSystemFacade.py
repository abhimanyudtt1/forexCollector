import subprocess
from src.common.ShellCommands import shellCommand
import time
import operator
from pprint import pprint

class FileSystemFacade(object):
    def __init__(self):
        # Nothing to do yet
        pass

    def getFullData(self,dataDir='./data'):
        info = {}
        output = subprocess.Popen(shellCommand.LIST +' %s' % dataDir,stderr=subprocess
                                           .PIPE,stdout=subprocess.PIPE,shell=True).communicate()[0].split('\n')
        output = map(lambda x : x.rstrip('\n'),output)
        output = filter(lambda x : not x == '',output)
        for dir in output:
            info[dir] = []
        for dir in output:
            out = subprocess.Popen(shellCommand.LIST+ " "+"/".join([dataDir,dir]),
                                      stderr=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      shell=True).communicate()[0].split('\n')
            out = map(lambda x: x.rstrip('\n'), out)
            out = filter(lambda x: not x == '', out)
            for eachFile in out :
                timeStamp = '_'.join(eachFile.split('.')[0].split('_')[1:])
                pattern = '%Y_%m_%d_%H_%M_%S'
                epoch = int(time.mktime(time.strptime(timeStamp, pattern)))
                info[dir].append((eachFile,epoch))

        for dir in info :
            info[dir].sort(key=operator.itemgetter(1))
            info[dir] = info[dir][-1][0]

        for dir in info :
            output = subprocess.Popen(shellCommand.CAT+" %s" % '/'.join((dataDir,dir,info[dir])),
                                      stderr=subprocess.PIPE,
                                      stdout=subprocess.PIPE,shell=True).communicate()[0].split('\n')
            output = map(lambda x: x.rstrip('\n'), output)
            output = filter(lambda x: not x == '', output)
            info[dir] = output

        for x,y in info.items():
            info[x] = map(lambda m : m.split('->'),y)


        pprint(info)
        return info