from random import randint

class Jumper:
    """The person with the word that needs to be guessed. 
    
    The responsibility of Jumper is to keep track of the answer word, determine correct guesses, and display the jumper.
    
    Attributes:
        guessed: list of guessed words.
        _answer: the answer word.
        _fails: number of incorrect guesses.
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        # all the possible answers
        words = ['Ball', 'Cream', 'Actor', 'Gold', 'Painting', 'Advertisement', 'Grass', 'Parrot', 'Afternoon', 
        'Greece', 'Pencil', 'Airport', 'Guitar', 'Piano', 'Ambulance', 'Hair', 'Pillow', 'Animal', 
        'Hamburger', 'Pizza', 'Answer', 'Helicopter', 'Planet', 'Apple', 'Helmet', 'Plastic', 'Army', 
        'Holiday', 'Portugal', 'Australia', 'Honey', 'Potato', 'Balloon', 'Horse', 'Queen', 'Banana', 
        'Hospital', 'Quill', 'Battery', 'House', 'Rain', 'Beach', 'Hydrogen', 'Rainbow', 'Beard', 'Ice', 
        'Raincoat', 'Bed', 'Insect', 'Refrigerator', 'Belgium', 'Insurance', 'Restaurant', 'Boy', 'Iron', 
        'River', 'Branch', 'Island', 'Rocket', 'Breakfast', 'Jackal', 'Room', 'Brother', 'Jelly', 'Rose', 'Camera', 
        'Jewellery', 'Candle', 'Sandwich', 'Car', 'Juice', 'School', 'Caravan', 'Kangaroo', 
        'Scooter', 'Carpet', 'King', 'Shampoo', 'Cartoon', 'Kitchen', 'Shoe', 'China', 'Kite', 'Soccer',
        'Knife', 'Spoon', 'Crayon', 'Lamp', 'Stone', 'Crowd', 'Lawyer', 'Sugar', 'Daughter', 'Leather', 'Sweden', 'Death', 
        'Library', 'Teacher', 'Denmark', 'Lighter', 'Telephone', 'Diamond', 'Lion', 'Television', 'Dinner', 'Lizard', 
        'Tent', 'Disease', 'Lock', 'Doctor', 'London', 'Tomato', 'Dog', 'Lunch', 'Toothbrush', 'Dream', 'Machine', 
        'Traffic', 'Dress', 'Magazine', 'Train', 'Easter', 'Magician', 'Truck', 'Egg', 'Eggplant', 
        'Market', 'Umbrella', 'Egypt', 'Match', 'Van', 'Elephant', 'Microphone', 'Vase', 'Energy', 'Monkey', 'Vegetable', 'Engine', 
        'Morning', 'Vulture', 'England', 'Motorcycle', 'Wall', 'Evening', 'Nail', 'Whale', 'Eye', 'Napkin', 'Window', 'Family', 'Needle', 
        'Wire', 'Finland', 'Nest', 'Fish', 'Yacht', 'Flag', 'Night', 'Yak', 'Flower', 'Notebook', 'Zebra', 'Football', 
        'Ocean', 'Zoo', 'Forest', 'Oil', 'Garden', 'Fountain', 'Orange', 'Gas', 'France', 'Oxygen', 'Girl', 'Furniture', 'Oyster', 
        'Glass', 'Garage', 'Ghost']

        self.guessed = []
        self._answer = words[randint(0,len(words)-1)]
        self._fails = 0

    def has_concluded(self):
        """Whether or not the jumper has run out of parachute or succeeded.

        Args:
            self (Jumper): An instance of Jumper.
            
        Returns:
            boolean: True if the word was guessed or ran out of guesses; false if otherwise.
        """
        # if lost
        if self._fails == 4:
            print("^^^^^^")
            print("You've run out of parachute... Better luck next time.")
            print(f"The word was: {self._answer}")
            return True
        # if succeeded
        elif "_" not in self.revealed_letters:
            print("^^^^^^")
            print("You finished with your parachute intact! Congratulations!")
            return True

        else: return False
    
    def update_words(self, guessed:list):
        """Updates the underscores with correct letters.
        Arguments:
        self: an instance of Jumper
        guessed: a list of guessed letters.
        """
        temp_correct = []
        self.revealed_letters = "_" * len(self._answer)
        for i in range(len(self._answer)):
            # if the current letter of answer is in the guessed list
            if self._answer[i].upper() in guessed:
                # add index to list
                temp_correct.append(i)
        
        # replace underscores
        for i in range(len(temp_correct)):
            # takes all items in list up to the one we want to change, then fills in the change, then adds the rest the same.
            self.revealed_letters = self.revealed_letters[:temp_correct[i]] + self._answer[temp_correct[i]] + self.revealed_letters[temp_correct[i]+1:]
            # ^^ this system is kind of genius if you ask me

    def draw_jumper(self, guessed:list):
        """Draw the jumper text art.
        Arguments:
        self: an instance of Jumper.
        guessed: a list of guessed letters.
        """
        # list of lines in jumper character
        jumper_lines = [" ___", "/___\\", "\   /", " \ /", "  0", " /|\\", " / \\"]
        
        # runs if no guesses have been made
        if len(guessed) != 0:
            # increase fails if wrong
            if guessed[-1] not in self._answer.upper():
                self._fails += 1
            
                # if no parachute left
                if self._fails == 4:
                    # replace 0 with X
                    jumper_lines = [line.replace("  0", "  X") for line in jumper_lines]

        for i in range(len(jumper_lines)):
            # if fails
            if self._fails < i+1:
                print(jumper_lines[i])
            else: print()
"""
 ___
/___\
\   /
 \ /
  0
 /|\
 / \
"""