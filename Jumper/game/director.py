from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.guesser import Guesser


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._guesser = Guesser()
        self._terminal_service = TerminalService()
        self.current_guess = ""
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # sets things up for first guess
        self._jumper.update_words([])
        self._terminal_service.write_text(self._jumper.revealed_letters)
        self._jumper.draw_jumper([])
        self._terminal_service.write_text("\n^^^^^^")


        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """gets single letter input from user.

        Args:
            self (Director): An instance of Director.
        """
        
        self._current_guess = self._terminal_service.read_letter("\nEnter a letter [A-Z]: ")

        
        
    
    def _do_updates(self):
        """updates guessed letters list, 

        Args:
            self (Director): An instance of Director.
        """
        # updates the guessed letters list
        self._guesser.update_guessed(self._current_guess)
        # updates underscores based on guessed letters
        self._jumper.update_words(self._guesser.guessed)



        
    def _do_outputs(self):
        """Fills in guessed letters.

        Args:
            self (Director): An instance of Director.
        """
        # draw guessed letters
        print(self._jumper.revealed_letters)
        # draw jumper
        self._jumper.draw_jumper(self._guesser.guessed)

        
        if self._jumper.has_concluded():
            self._is_playing = False
        else: self._terminal_service.write_text("\n^^^^^^")