class A:
    test = 1
    def foo(this):
        print 'foo'
        return 0

a = A()

def bar(this):
    print 'bar'
    return 0

a.foo()
print a.foo
a.foo = bar
print a.foo
