class Guesser():
    """The person guessing the word. 
    
    The responsibility of a Guesser is to keep track of the guessed letters.
    
    Attributes:
        guessed (list) keeps track of the letters that have been guessed.
    """

    def __init__(self):
        """Constructs a new Guesser.
        Args:
            self (Guesser): An instance of Guesser.
        """
        self.guessed = []
       
    def update_guessed(self, letter):
        """Updates the list of guessed characters."""
        if letter not in self.guessed:
            self.guessed.append(letter.upper())