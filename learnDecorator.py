import functools
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

def logs(text):
    def decorator(func):
        @functools.wraps(func)
        def wrappers(*args, **kw):
            print '%s call %s():' %(text, func.__name__)
            return func(*args, **kw)
        return wrappers
    return decorator

@logs('excute')
def now():
    print '2017-08-25'

f = now
f()

print "================="
now = logs('excute')(now)

now()