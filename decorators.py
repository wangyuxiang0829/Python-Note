'''
Decorators is just a function that takes another function as an
argument and adds some kind of functionality and then returns
another function. All of this without altering the source code
of the original function that passed in.
'''


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_function
def display():
    '''
    This function has been decorated by function 'decorator_function', it's actually a
    syntactic sugar of 'display = decorator_function(display)', and thus now 'display'
    function is equals to 'wrapper_function'.
    '''
    print('display function ran')


@decorator_class
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('John', 25)

display()
