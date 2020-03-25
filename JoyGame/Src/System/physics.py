from JoyGame.Src.Include.vector import Vector2


class Physics:
    def __init__(self):
        # init variable
        self.last_Position = Vector2(0, 0)
        self.Position = Vector2(0, 0)
        self.position = Vector2(0, 0)
        self.altitude = Vector2(0, 0)

        self.jumpSpeed = Vector2(0, 0)
        self.Speed = Vector2(0, 0)

        # initialize variable
        self.jump_flag = 0
        self.maxJumpSpeed = 20
        self.maxSpeed = 10
        self.maxHeight = 40
        self.changePosition = False

    def set_position(self, position: Vector2):
        self.Position = position

    def updata_position(self):
        return self.Speed

    # time_passed = self.clock.tick()
    # time_passed_second = time_passed / 10.
    def update_altitude(self):
        return self.jumpSpeed

    def update_position(self):
        self.update_altitude()
        self.altitude = self.altitude.__add__(self.update_altitude())
        self.position = self.position.__add__(self.updata_position())
        self.Position = Vector2.__add__(self.altitude, self.position)
        self.changePosition = self.is_position()
        self.last_Position = self.Position

    def is_position(self):
        return self.last_Position.__tuple__() != self.Position.__tuple__()

    def leap(self):
        if not self.jump_flag:
            self.jumpSpeed = Vector2(0, -self.maxJumpSpeed)
        elif self.altitude.getMagnitude() == self.maxHeight:
            self.jump_flag = True
        elif self.altitude.getMagnitude() == Vector2(0, 0):
            self.jump_flag = False
        if self.jump_flag and self.altitude != Vector2(0, 0):
            self.jumpSpeed = Vector2(0, self.maxJumpSpeed)
