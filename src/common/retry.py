import time
from selenium.common import exceptions


def retry(timeout,timeDelta):
    def retryDecorator(function):
        def wrapper(*args, **kwargs):
            t = timeout
            print "DEBUG : Running %s on webElement : %s,%s " % (function,args,kwargs)
            while t != 0 :
                try :
                    return function(*args,**kwargs)
                except exceptions.WebDriverException :
                    print "Cannot Locate Element. Retrying in %s sec(s)" % timeDelta
                    time.sleep(timeDelta)
                    t -= 1
            raise exceptions.WebDriverException("Element not found Exiting! Element : %s " % args[1].getSelector())
        return wrapper
    return retryDecorator




def decorator(arg1, arg2):

    def real_decorator(function):

        def wrapper(*args, **kwargs):
            print "Congratulations.  You decorated a function that does something with %s and %s" % (arg1, arg2)
            function(*args, **kwargs)
        return wrapper

    return real_decorator