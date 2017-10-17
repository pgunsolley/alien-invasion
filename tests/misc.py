# Because I happen to be a python newbie, I'm using this script for learning the
# behavior of Python and the CPython runtime as needed during my journey. :3


# In python, use kwargs (keyword args) as you would pass an object literal in JS.
def pass_kwarg(**kwargs):
    """
    Output the kwarg

    :param kwargs:
    :return:
    """
    print(kwargs)


pass_kwarg(greeting="Hello")
