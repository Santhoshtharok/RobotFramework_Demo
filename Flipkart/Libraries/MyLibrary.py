class MyLibrary:

    def __init__(self, greeting="Hello!"):
        self._greeting = greeting

    def get_greeting(self):
        return self._greeting