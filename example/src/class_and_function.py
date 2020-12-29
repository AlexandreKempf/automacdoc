import numpy as np


def maxi(x: int, y: int = 5):
    """
    Take the max between two numbers

    **Parameters**

    > **x:** `float` -- Description of parameter `x`.

    > **y:** `float` -- Description of parameter `y`.

    **Returns**

    > `float` -- Description of returned object.
    """
    return np.max(x, y)


def maxi2pourvoir(x, y):
    """
    Take the max between two numbers

    **Parameters**

    > **x:** `float` -- Description of parameter `x`.

    > **y:** `float` -- Description of parameter `y`.

    **Returns**

    > `float` -- Description of returned object.
    """
    return np.max(x, y)


class Shark:

    @classmethod
    def swimclass(self, a):
        """
        Teach them how to swim

        **Parameters**

        > **self:** `obj` -- Instance of `Shark`.

        **Returns**

        > `bool` -- Did they succeed.
        """
        print('prout')
        print("The shark is swimming.")
        for i in range(2):
            print("lololo")
        return

    @staticmethod
    def swimstatic(self, a):
        """
        Teach them how to swim

        **Parameters**

        > **self:** `obj` -- Instance of `Shark`.

        **Returns**

        > `bool` -- Did they succeed.
        """
        print('prout')
        print("The shark is swimming.")
        for i in range(2):
            print("lololo")
        return


    def be_awesome(self):
        """
        Take the max between two numbers

        **Parameters**

        > **x:** `float` -- Description of parameter `x`.

        > **y:** `float` -- Description of parameter `y`.

        **Returns**

        > `float` -- Description of returned object.
        """
        print("The shark is being awesome.")
