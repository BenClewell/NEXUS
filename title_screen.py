from asciimatics.screen import Screen
from asciimatics.renderers import Plasma, Rainbow, FigletText
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.exceptions import ResizeScreenError

import sfx

# click and begin sound


def title_screen_show():
    class PlasmaScene(Scene):
        """play the title card"""

        _comments = ["THE NEXUS", "PRESS Q"]

        def __init__(self, screen):
            self._screen = screen
            effects = [
                Print(
                    screen,
                    Plasma(screen.height, screen.width, screen.colours),
                    0,
                    speed=1,
                    transparent=False,
                ),
            ]
            super(PlasmaScene, self).__init__(effects, 200, clear=False)

        def add_comment(self):

            msg = FigletText(("NEXUS"), font="big")
            creator = FigletText(
                ("A game by Benjamin Clewell"), font="rectangles"
            )
            self._effects.append(
                Print(
                    self._screen,
                    msg,
                    (self._screen.height // 2) - 4,
                    x=(self._screen.width - msg.max_width) // 2 + 1,
                    colour=Screen.COLOUR_WHITE,
                    stop_frame=30,
                    speed=1,
                )
            )

            self._effects.append(
                Print(
                    self._screen,
                    creator,
                    (self._screen.height // 2) + 5,
                    x=(self._screen.width - msg.max_width) // 2 - 35,
                    colour=Screen.COLOUR_WHITE,
                    start_frame=5,
                    stop_frame=30,
                    speed=1,
                )
            )

            # Changes text to rainbow...

            self._effects.append(
                Print(
                    self._screen,
                    Rainbow(self._screen, msg),
                    (self._screen.height // 2) - 4,
                    x=(self._screen.width - msg.max_width) // 2,
                    colour=Screen.COLOUR_BLACK,
                    stop_frame=30,
                    speed=1,
                )
            )

            # START INSTRUCTIONS

            msg = FigletText(
                ("PRESS   Q"),
                font="big",
            )
            self._effects.append(
                Print(
                    self._screen,
                    msg,
                    (self._screen.height // 2) - 4,
                    x=(self._screen.width - msg.max_width) // 2 + 1,
                    colour=Screen.COLOUR_WHITE,
                    start_frame=30,
                    speed=1,
                )
            )

            # Changes text to rainbow...

            self._effects.append(
                Print(
                    self._screen,
                    Rainbow(self._screen, msg),
                    (self._screen.height // 2) - 4,
                    x=(self._screen.width - msg.max_width) // 2,
                    colour=Screen.COLOUR_BLACK,
                    start_frame=30,
                    speed=1,
                )
            )

        def reset(self, old_scene=None, screen=None):
            super(PlasmaScene, self).reset(old_scene, screen)

            # Make sure that we only have the initial Effect and add a new cheesy
            # comment.
            self._effects = [self._effects[0]]
            self.add_comment()

    def intro_plasma(screen):

        screen.play(
            [PlasmaScene(screen)],
            stop_on_resize=True,
        )

    while True:
        try:
            Screen.wrapper(intro_plasma)
            sfx.click.play()
            sfx.startup.play()
            # force fullscreen keyboard.press_and_release('F11')
            break
        except ResizeScreenError:
            pass
