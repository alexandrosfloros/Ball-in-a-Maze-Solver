import math


class Ball:
    def __init__(self, position):
        self.position = position
        self.velocity = [0.0, 0.0]
        self.acceleration = [0.0, 0.0]

        self.max_speed = 0.1
        self.min_speed = 0.01

        self.moving_x = True
        self.progress = 0

    def board_zero_x(self):
        self.acceleration[0] = 0.0

    def board_zero_y(self):
        self.acceleration[1] = 0.0

    def board_pos_x(self):
        self.acceleration[0] = 0.007

    def board_neg_x(self):
        self.acceleration[0] = -0.007

    def board_pos_y(self):
        self.acceleration[1] = 0.007

    def board_neg_y(self):
        self.acceleration[1] = -0.007

    def balance_x(self):
        if self.velocity[0] > self.min_speed:
            self.board_neg_x()

        elif self.velocity[0] < -self.min_speed:
            self.board_pos_x()

        else:
            self.board_zero_x()
            self.stop_x()

    def balance_y(self):
        if self.velocity[1] > self.min_speed:
            self.board_neg_y()

        elif self.velocity[1] < -self.min_speed:
            self.board_pos_y()

        else:
            self.board_zero_y()
            self.stop_y()

    def stop_x(self):
        self.moving_x = False

    def stop_y(self):
        self.moving_x = True
        self.progress += 1


class Algorithm:
    def __init__(self, model):
        self.ball = model.ball
        self.nodes = model.nodes
        self.holes = model.holes

        self.limit = len(self.nodes)

        self.node_tolerance = 1.0
        self.hole_tolerance = 0.75

        self.finished = False
        self.failed = False

    def run(self):
        self.ball.next_node = self.nodes[self.ball.progress]
        xn, yn = self.ball.next_node

        xb, yb = self.ball.position

        if self.ball.moving_x:
            if xb < xn:
                if self.ball.velocity[0] > self.ball.max_speed:
                    self.ball.board_zero_x()

                else:
                    self.ball.board_pos_x()
            else:
                if self.ball.velocity[0] < -self.ball.max_speed:
                    self.ball.board_zero_x()

                else:
                    self.ball.board_neg_x()

            if abs(xb - xn) < self.node_tolerance:
                self.ball.balance_x()
        else:
            if yb < yn:
                if self.ball.velocity[1] > self.ball.max_speed:
                    self.ball.board_zero_y()

                else:
                    self.ball.board_pos_y()
            else:
                if self.ball.velocity[1] < -self.ball.max_speed:
                    self.ball.board_zero_y()

                else:
                    self.ball.board_neg_y()

            if abs(yb - yn) < self.node_tolerance:
                self.ball.balance_y()

                if self.ball.progress == self.limit:
                    self.finished = True

        if any(
            math.dist(self.ball.position, h) < self.hole_tolerance for h in self.holes
        ):
            self.failed = True
