# guipoker.py

from graphics import *
from pokerapp import PokerApp
from button import Button
from cdieview import ColorDieView
from U12_Ex01_SplashScreen import SplashScreen
from U12_Ex01_HelpScreen import HelpScreen
from shadowtext import *
from Chapter12.U12_Ex01_DicePoker.U12_Ex01_HighScore import HighScore
from Chapter12.U12_Ex01_DicePoker.shadowtext import ShadowText


class GraphicsInterface:
    """
    GUI for dice poker game
    """

    def __init__(self, hi_scores):
        """
        Set up graphical interface
        :param hi_scores: obj -> HighScore object
        """
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green4")
        banner = Text(Point(300,30), "Python  Poker  Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner_shadow = ShadowText(banner)
        banner_shadow.draw(self.win)
        banner.draw(self.win)
        self.msg = Text(Point(300,380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(300,100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300,170), 75, 30)
        b = Button(self.win, Point(300, 230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(30,375), 40, 30, "Help")
        self.buttons.append(b)
        b = Button(self.win, Point(570,375), 40, 30, "Quit")
        self.buttons.append(b)
        self.money = Text(Point(300,325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)
        self.hi_scores = hi_scores          # added for high score feature

    def createDice(self, center, size):
        """
        Creates five dice (in self.dice[]), each of which is an instance of ColorDieView
        :param center: Point -> center of window (???)
        :param size: int/float -> length of an edge of a die
        """
        center.move(-3*size,0)
        self.dice = []
        for i in range(5):
            view = ColorDieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size,0)

    def addDiceButtons(self, center, width, height):
        """
        Creates a button for each die
        :param center: Point -> center of window (???)
        :param width: int/float -> width of each button
        :param height: int/float -> height of each button
        """
        center.move(-3*width, 0)
        for i in range(1,6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)

    def setMoney(self, amt):
        """
        Changes money text for GUI
        :param amt: int -> amount to display
        """
        self.money.setText("${0}".format(amt))

    def showResult(self, msg, score):
        """
        Show result of latest roll
        :param msg: str -> hand that was rolled
        :param score: int -> score associated with hand, if any
        """
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score)
        else:
            text = "You rolled {0}".format(msg)
        self.msg.setText(text)

    def setDice(self, values):
        """
        Sets values of dice
        :param values: list -> integer values for each die
        """
        for i in range(5):
            self.dice[i].setValue(values[i])

    def wantToPlay(self):
        """
        Queries if user wants to keep playing
        :return: boolean -> true if wants to play; false otherwise
        """
        while True:
            # added choice for Help
            ans = self.choose(["Roll Dice", "Quit", "Help"])
            if ans == "Help":
                self.show_help()
            else:
                self.msg.setText("")
                return ans == "Roll Dice"

    def close(self):
        """
        Close-up shop...app exit
        """
        self.win.close()

    def chooseDice(self):
        """
        Allows individual dice to be chosen for re-roll
        :return: list -> integer list of dice to re-roll
        """
        # choices is a list of the indexes of the selected dice
        choices = []                   # No dice chosen yet
        while True: 
            # wait for user to click a valid button
            # added choice for Help
            b = self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5",
                             "Roll Dice", "Score", "Help"])

            if b[0] == "D":            # User clicked a die button
                i = int(b[4]) - 1      # Translate label to die index
                if i in choices:       # Currently selected, unselect it
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:                  # Currently unselected, select it
                    choices.append(i)
                    self.dice[i].setColor("gray")
            elif b == "Help":          # choice added for Help
                self.show_help()
            else:                      # User clicked Roll or Score
                for d in self.dice:    # Revert appearance of all dice
                    d.setColor("black")
                if b == "Score":       # Score clicked, ignore choices
                    return []
                elif choices != []:    # Don't accept Roll unless some
                    return choices     #   dice are actually selected

    
    def choose(self, choices):
        """
        Modal method to get user choice from choices parameter
        :param choices: list -> str label values for buttons to activate
        :return: str -> label of chosen button
        """
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()  # function exit here.

    def show_help(self):
        """
        Creates HelpScreen object (which displays help screen) and waits for response.
        :return:
        """
        help_screen = HelpScreen([
            ["Rules of the Game", 24],
            ["Click the 'Roll Dice' button to start. ", 12],
            ["The goal is to make the best poker hand", 12],
            ["with five dice. Up to two re-rolls are ", 12],
            ["allowed per turn. Click on the 'Die #' ", 12],
            ["button below each die you wish to re-  ", 12],
            ["roll. Then click 'Roll Dice' to re-roll", 12],
            ["only those dice. If you like your hand ", 12],
            ["before using both re-rolls, click the  ", 12],
            ["'Score' button to end the turn. If all ", 12],
            ["re-rolls are used, the score is updated", 12],
            ["automatically. Good Luck!", 12],
            ["", 12],
            ["Payout Table", 18],
            ["Hand\t\tPayout", 14],
            ["Five of a Kind\t\t$30", 12],
            ["Straight (1-5 or 2-6)\t$20", 12],
            ["Four of a Kind\t\t$15", 12],
            ["Full House\t\t$12", 12],
            ["Three of a Kind\t\t$8", 12],
            ["Two Pairs\t\t$5", 12],
        ]
        )
        help_screen.get_response()

    def enter_score(self, amt):
        """
        Screen for user to enter their name when their score is in the top ten.
        :param amt: int -> score (amount of money)
        """
        winW = 600
        winH = 300
        win = GraphWin("High Score!", winW, winH)                   # creates a separate window
        win.setBackground(color_rgb(80, 0, 0))

        sep_shadow = Line(Point(300, 21), Point(300, 279))          # vertical separator line
        sep_shadow.setFill('darkgrey')
        sep_shadow.draw(win)
        sep_pt1 = Point(300, 20)
        sep_pt1.setFill('white')
        sep_pt1.setOutline('white')
        sep_pt1.draw(win)
        separator = Line(Point(301, 20), Point(301, 280))
        separator.setFill('white')
        separator.draw(win)
        sep_pt2 = Point(300, 180)
        sep_pt2.setFill('white')
        sep_pt2.setOutline('white')
        sep_pt2.draw(win)

        self.display_msg(win, 150, 30, "Congratulations!", 18)      # left side of screen for name entry
        self.display_msg(win, 150, 54, "You're TOP TEN!", 14)
        self.display_msg(win, 150, 119, "Enter your name.", 14)
        name_entry = Entry(Point(150, 150), 20)
        name_entry.setSize(14)
        name_entry.setTextColor(color_rgb(80, 0, 0))

        self.display_msg(win, 450, 30, "High Scorers", 18)          # right side of screen for high scores list
        if len(hi_scores.scores) == 0:                              # no high scores, yet
            self.display_msg(win, 450, 150, "You're the first!", 14)
        else:
            # display scores

            line_pos = 30
            hi_scores.set_pointer(0)
            while True:
                score_info = hi_scores.get_next_score()
                name = score_info[0]
                hi_score = score_info[1]
                if name == None:
                    break
                line_pos += hi_scores.get_scores_fontsize() * 1.3
                self.display_msg(win, 450, line_pos+hi_scores.get_scores_fontsize() * 1.3,
                                 '{}\t{}'.format(name, hi_score),
                                 hi_scores.get_scores_fontsize())

        name_entry.draw(win)
        self.button_ok = Button(win, Point(95, 260), 75, 35, "OK")
        self.button_cancel = Button(win, Point(207, 260), 75, 35, "Cancel")
        self.button_ok.activate()
        self.button_cancel.activate()

        response = self.get_response(win)
        if response:
            hi_scores.set_score(name_entry.getText(), amt)

        win.close()

    def display_msg(self, win, x, y, m, s, c='white', o='white'):
        """
        Helper method to display a message
        :param win: obj -> GraphWin object in which to display message
        :param x: int/float -> x coordinate for center point of message
        :param y: int/float -> y coordinate for center point of message
        :param m: str -> message to display
        :param s: int -> size of message text
        :param c: str -> fill color of message (default: white)
        :param o: str -> outline color of message (default: white)
        """
        msg = Text(Point(x, y), m)
        msg.setFill(c)
        msg.setOutline(o)
        msg.setSize(s)
        msg_shadow = ShadowText(msg, offset_x=2, offset_y=2)
        msg_shadow.draw(win)
        msg.draw(win)

    def get_response(self, win):
        """
        Event loop to get response from user (clicking a button or pressing Return or Escape)
        :return: boolean -> True if OK is selected; otherwise False
        """
        while True:
            p = win.checkMouse()
            k = win.checkKey()
            if p and self.button_ok.clicked(p) or k == "Return":
                win.close()
                return True
            if p and self.button_cancel.clicked(p) or k == "Escape":
                win.close()
                return False


hi_scores = HighScore()                     # create HighScore object for application
splash = SplashScreen(hi_scores)            # display splash screen
if splash.get_response():
    inter = GraphicsInterface(hi_scores)    # create interface object for application
    app = PokerApp(inter, hi_scores)        # create app object
    app.run()                               # Play!
