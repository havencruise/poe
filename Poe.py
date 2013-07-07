#!/usr/bin/env python
import sys, os, re, random
from subprocess import call

NAME = sys.argv[0]

def usage(name):
    print 'Usage:'
    print '  %s <command> (<arg1>, <arg2> ...)' % name
    print '\n'
    print 'Example:'
    print '  > %s help' % name
    print '  > %s setup ext' % name
    print '\n'


def mkdir(path):
    if not os.path.exists(path):
        print 'Creating %s' % path
        os.makedirs(path)
    else:
        print('Directory %s already exists', path)

AVAILABLE_METHODS = ['setup',]
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.'))

class Poe:
    types = ['ext', 'django']

    @staticmethod
    def help():
        pass

    @staticmethod
    def setup(args):
        if not args:
            usage(NAME)
            sys.exit(2)

        setup_type = args[0]
        if setup_type in Poe.types:
            m = getattr(Poe, 'setup_%s' % setup_type)
            m()

    @staticmethod
    def setup_ext():
        project_dir = BASE_DIR + '/ext-project'
        if os.path.exists(project_dir):
            test_dir = project_dir + '%s' % random.randint(0, 999)
            while os.path.exists(test_dir):
                test_dir = project_dir + '%s' % random.randint(0, 999)
            project_dir = test_dir

        resources_dir = project_dir + '/resources'
        app_dir = project_dir + '/app'

        mkdir(project_dir)
        mkdir(resources_dir)
        mkdir(app_dir)

        try:
            call(['cp', '%s' % (BASE_DIR + '/server.py'), '%s' % project_dir])
            print 'Copied server.py '
        except:
            print 'Error copying server.py to the project folder. Please do so yourself. \n\n'

        try:
            call(['touch', '%s' % (project_dir + '/index.html')])
            print 'Created index.html'
        except:
            print 'Error creating index.html\n'


        print "\nDone setting up your project.\nPlease rename the ext-project folder to your project name."


def exec_method(method, args):
    calleeMethod = getattr(Poe, method)
    calleeMethod(args)
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv[1:]) > 0 and sys.argv[1] in AVAILABLE_METHODS:
        exec_method(sys.argv[1], sys.argv[2:])

    usage(NAME)