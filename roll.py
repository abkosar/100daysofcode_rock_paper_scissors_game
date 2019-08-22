
class Roll:
    def __init__(self, name):
        self.name = name

    def can_defeat(self, roll_name):
        if self.name == 'rock':
            if roll_name == 'paper':
                return False
            elif roll_name == 'scissors':
                return True

        elif self.name == 'paper':
            if roll_name == 'rock':
                return True
            elif roll_name == 'scissors':
                return False

        elif self.name == 'scissors':
            if roll_name == 'paper':
                return True
            elif roll_name == 'rock':
                return False
