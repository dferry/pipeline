class Color:
    def __init__( self, value ):
        self.red = 0
        self.blue = 0
        self.green = 0
        self.add( value )

        
    def add( self, value ):
        if value == "white":
            self.red = 1
            self.blue = 1
            self.green = 1
            return
        if value == "black":
            return
        if value == "red":
            self.red = 1
            return
        if value == "green":
            self.green = 1
            return
        if value == "blue":
            self.blue = 1
            return
        if value == "cyan":
            self.blue = 1
            self.green = 1
            return
        if value == "magenta":
            self.red = 1
            self.blue = 1
            return
        if value == "yellow":
            self.red = 1
            self.green = 1
            return


    def __add__(self, other):
        pass

    def toString(self):
        if self.red == 1 and self.green == 1 and self.blue == 1:
            return "white"
        if self.red == 0 and self.green == 0 and self.blue == 0:
            return "black"
        if self.red == 1 and self.green == 0 and self.blue == 0:
            return "red"
        if self.red == 0 and self.green == 1 and self.blue == 0:
            return "green"
        if self.red == 0 and self.green == 0 and self.blue == 1:
            return "blue"
        if self.red == 0 and self.green == 1 and self.blue == 1:
            return "cyan"
        if self.red == 1 and self.green == 0 and self.blue == 1:
            return "magenta"
        if self.red == 1 and self.green == 1 and self.blue == 0:
            return "yellow"