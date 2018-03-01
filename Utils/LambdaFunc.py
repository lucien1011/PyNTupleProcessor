class LambdaFunc(object):
    """A class to define a lambda function given a string. This is because lambda functions are not picklable"""

    def __init__(self,inputStr):
        self.inputStr = inputStr

    def begin(self):
        self.func = eval( 'lambda ' + self.inputStr )

    def __call__(self,*event):
        if not hasattr(self,"func"):
            self.begin()
        return self.func(*event)
