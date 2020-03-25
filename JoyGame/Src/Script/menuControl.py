from JoyGame.Src.System.global_variable import get_value


class MenuControl:
    def __init__(self, controller, timer):
        # Initialize class
        self.controller = controller
        self.timer = timer

        # Initialize variable
        self.layer = 0
        self.layer_name = ""
        self.index = 0
        self.enter = False
        self.pause = False
        self.numButton = {}
        self.add2menuList("homepage", get_value('homepage_menu_config'))
        self.add2menuList("play", get_value('play_menu_config'))
        self.add2menuList("setting", get_value('setting_menu_config'))
        self.add2menuList("tutorial", get_value('tutorial_menu_config'))
        self.add2menuList("start", get_value('game_pause_menu_config'))
        self.add2menuList("create", get_value('game_pause_menu_config'))
        self.add2menuList("load", get_value('game_pause_menu_config'))

    def add2menuList(self, layer_name, layer_config):
        self.numButton[layer_name] = len(layer_config)

    def rear(self):
        self.index += 1
        if self.index >= self.numButton[self.layer_name]:
            self.index -= self.numButton[self.layer_name]

    def front(self):
        self.index -= 1
        if self.index < 0:
            self.index += self.numButton[self.layer_name]

    def enter_menu(self):
        self.enter = True

    def next(self):
        self.layer += 1
        self.index = 0
        self.enter = False

    def previous(self):
        self.index = 0
        self.layer -= 1
        if self.layer < 1:
            self.layer = 1

    def set_pause(self):
        if self.pause is True:
            self.pause = False
        else:
            self.pause = True

    def horizontal_control(self):
        if self.controller.LS_down and self.timer.elapse() > 0.15:
            self.rear()
            self.timer.set_timer()
        elif self.controller.LS_up and self.timer.elapse() > 0.15:
            self.front()
            self.timer.set_timer()

        if self.controller.A and self.timer.elapse() > 0.3:
            self.enter_menu()
            self.timer.set_timer()

        elif self.controller.B and self.timer.elapse() > 0.3:
            self.previous()
            self.timer.set_timer()

        if self.controller.hats_up and self.timer.elapse() > 0.15:
            self.front()
            self.timer.set_timer()
        elif self.controller.hats_down and self.timer.elapse() > 0.15:
            self.rear()
            self.timer.set_timer()

    def vertical_control(self):
        if self.controller.LS_left and self.timer.elapse() > 0.15:
            self.front()
            self.timer.set_timer()
        elif self.controller.LS_right and self.timer.elapse() > 0.15:
            self.rear()
            self.timer.set_timer()

        if self.controller.A and self.timer.elapse() > 0.3:
            self.enter_menu()
            self.timer.set_timer()

        elif self.controller.B and self.timer.elapse() > 0.3:
            self.previous()
            self.timer.set_timer()

        elif self.controller.hats_right and self.timer.elapse() > 0.15:
            self.front()
            self.timer.set_timer()
        elif self.controller.hats_left and self.timer.elapse() > 0.15:
            self.rear()
            self.timer.set_timer()

    def game_menu(self):
        if (self.controller.LS_up or self.controller.hats_up) and self.timer.elapse() > 0.3:
            self.front()
            self.timer.set_timer()
        elif (self.controller.LS_down or self.controller.hats_down) and self.timer.elapse() > 0.3:
            self.rear()
            self.timer.set_timer()
        elif self.controller.A and self.timer.elapse() > 0.3:
            self.enter_menu()
            self.timer.set_timer()
        elif self.controller.Start and self.timer.elapse() > 0.3:
            self.pause = False
            self.timer.set_timer()

    def game_control(self, character):
        if self.controller.LS_right and self.controller.LS_up:
            character.move_upper_right()
        elif self.controller.LS_left and self.controller.LS_up:
            character.move_upper_left()
        elif self.controller.LS_right and self.controller.LS_down:
            character.move_lower_right()
        elif self.controller.LS_left and self.controller.LS_down:
            character.move_lower_left()
        elif self.controller.LS_up or self.controller.hats_up:
            character.move_up()
        elif self.controller.LS_down:
            character.move_down()
        elif self.controller.LS_left:
            character.move_left()
        elif self.controller.LS_right:
            character.move_right()
        elif self.controller.A and not character.physics.jump_flag and self.timer.elapse() > 0.5:
            character.move_sliding()
        elif self.controller.B:
            character.move_kicking()
        elif self.controller.X:
            character.move_slashing()
        elif self.controller.Y:
            character.move_throwing()
        elif self.controller.Menu and self.timer.elapse() > 0.3:
            self.pause = True
            self.timer.set_timer()
        elif self.controller.Start and self.timer.elapse() > 0.3:
            self.pause = False
            self.timer.set_timer()
        else:
            character.move_idle()


if __name__ == "__main__":
    pass
