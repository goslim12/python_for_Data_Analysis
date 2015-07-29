def works_fine():
    a = 5
    b = 6
    assert(a + b == 11)

def throws_an_exception():
    a = 5
    b = 6
    assert(a + b == 10)

def calling_things():
    works_fine()
#    set_trace() 
    throws_an_exception()

calling_things()
