import curses
import random
import time
import sys
import random

from my_modules import sfx
import pygame
from pygame import mixer


num_denials = 3
# placeholder
def node_hacking_minigame():

    # how many times alarm can sound
    def get_equation():
        """
        Returns a math equation string as well as the answer
        """

        operator = random.randint(1, 4)

        if operator == 1:
            # addition
            first_number = random.randint(10, 30)
            second_number = random.randint(10, 30)
            answer = first_number + second_number
            return "{} + {} =".format(first_number, second_number), answer

        elif operator == 2:
            # subtraction
            first_number = random.randint(30, 50)
            second_number = random.randint(10, 20)
            answer = first_number - second_number
            return "{} - {} =".format(first_number, second_number), answer
        elif operator == 3:
            # multiplication
            first_number = random.randint(3, 12)
            second_number = random.randint(3, 12)
            answer = first_number * second_number
            return "{} * {} =".format(first_number, second_number), answer
        else:
            # addition with three numbers
            first_number = random.randint(1, 9)
            second_number = random.randint(1, 9)
            third_number = random.randint(1, 9)
            answer = first_number + second_number + third_number
            return (
                "{} + {} + {} =".format(
                    first_number, second_number, third_number
                ),
                answer,
            )

    def play(stdscr):
        """
        Play function
        """

        stdscr.clear()
        sfx.alarm_loop(6)
        # Get window height & width
        height, width = stdscr.getmaxyx()
        title = "NODE COUNTERMEASURES IN PROGRESS"

        # get various x,y coordinates according to user's window size
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_y_title = int((height // 4) - 2)

        start_x_problem = int((width // 2) - 4)
        start_y_problem = int((3 * height // 4))

        enemy_x = int(width // 8)
        enemy_y = int((height // 2) - 1)

        x = int(width // 8)
        y = int((height // 2) + 1)

        x_finish = int((width // 8) * 7)

        finished = False

        winner = False

        while finished == False:  # iterate until user finishes game
            stdscr.addstr(start_y_title, start_x_title, title)

            stdscr.addstr(enemy_y + -2, x_finish - 3, "NODE")
            stdscr.addstr(enemy_y + -1, x_finish, "|")
            stdscr.addstr(enemy_y, x_finish, "|")
            stdscr.addstr(enemy_y + 1, x_finish, "|")
            stdscr.addstr(enemy_y + 2, x_finish, "|")
            stdscr.addstr(enemy_y + 3, x_finish, "|")

            # get initial equation
            problem, actual_answer = get_equation()

            stdscr.addstr(start_y_problem, start_x_problem, problem)

            counter = 1

            stdscr.nodelay(True)  # make sure it doesnt stop to get a character

            user_answer = ""
            alarm_limit = 1

            while enemy_x < x_finish - 4 and x < x_finish - 4:

                key = stdscr.getch()

                stdscr.addstr(enemy_y, enemy_x, ">[XX]>")

                stdscr.addstr(y, x, ">[~~]>")

                # the number after counter mod increases enemy speed
                if counter % 1600 == 0:
                    enemy_x = enemy_x + 1

                counter = counter + 1

                stdscr.refresh()

                if key == 10:  # user presses enter
                    if user_answer == str(actual_answer):  # correct answer
                        sfx.burst_sound()
                        # sound
                        stdscr.addstr(y, x, ">" * 25)
                        x = x + 25
                        stdscr.addstr(y, x, ">[~~]>")  # moves user forward

                        (
                            problem,
                            actual_answer,
                        ) = get_equation()  # get new equation
                        stdscr.addstr(
                            start_y_problem, start_x_problem, "          "
                        )
                        stdscr.addstr(
                            start_y_problem, start_x_problem, problem
                        )  # overwrite old equation
                        stdscr.addstr(
                            start_y_problem,
                            start_x_problem + 10,
                            "          ",
                        )
                        user_answer = ""

                    else:  # incorrect answer
                        user_answer = ""
                        stdscr.addstr(
                            start_y_problem,
                            start_x_problem + 10,
                            "          ",
                        )
                        enemy_x = enemy_x + 5
                        sfx.bad_sound_hack.play()

                        if alarm_limit == 1:
                            sfx.alarm_loop(random.randint(1, 5))
                            alarm_limit += 1

                elif key == 127:  # user presses backspace
                    user_answer = user_answer[:-1]
                    stdscr.addstr(
                        start_y_problem, start_x_problem + 10, "          "
                    )

                elif key != -1:  # user adds character to their answer
                    user_answer = user_answer + str(chr(key))

                stdscr.addstr(
                    start_y_problem, start_x_problem + 10, user_answer
                )  # update user answer

            finished = True

            if x >= x_finish - 4:  # check if user won or lost
                winner = True

        stdscr.clear()

        if winner == True:
            title = "NODE ENTRY GAINED"
            subtitle = "Press any key to unlock contents."
            pygame.mixer.stop()
            curses.endwin()

        else:
            title = "NODE ENTRY DENIED"
            subtitle = (
                "You may be denied "
                + str(num_denials)
                + " more time(s) before you are locked out."
            )
            # nexus_main.num_denials -=1
            pygame.mixer.stop()
            curses.endwin()

        height, width = stdscr.getmaxyx()

        stdscr.addstr(
            int((height // 2) - 2) - 1,
            int((width // 2) - (len(title) // 2) - len(title) % 2),
            title,
        )
        stdscr.addstr(
            int((height // 2) - 2) + 2,
            int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2),
            subtitle,
        )

        stdscr.nodelay(False)  # pause until user enters a character

        stdscr.getch()

        # curses.wrapper(main)  # back to main function

    def main(stdscr):

        k = 0  # user input

        # clear and refresh
        stdscr.clear()
        stdscr.refresh()

        while k not in [
            ord("q"),
        ]:  # repeat until user enters an option

            # Get window height & width
            height, width = stdscr.getmaxyx()

            # Decorate main menu
            title = "FIREWALL DETECTED"
            subtitle1 = ""
            subtitle2 = "PRESS Q TO BEGIN HACK."
            pygame.mixer.unpause()

            start_x_title = int(
                (width // 2) - (len(title) // 2) - len(title) % 2
            )
            start_x_subtitle = int(
                (width // 2) - (len(subtitle1) // 2) - len(subtitle1) % 2
            )
            start_y = int((height // 2) - 2)

            stdscr.addstr(start_y - 1, start_x_title, title)
            stdscr.addstr(start_y + 3, start_x_subtitle, subtitle1)
            stdscr.addstr(start_y + 4, start_x_subtitle, subtitle2)

            # Wait for next input
            k = stdscr.getch()

        if k == ord("q"):
            play(stdscr)

    curses.wrapper(main)
