class Graphics:
    def __init__(self, ball, nodes, holes):
        self.ball = ball
        self.nodes = nodes
        self.holes = holes
    
    def update_ball(self, ax):
        patches = self.init_path(ax)

        self.ball_pos.set_data([self.ball.position[0]], [self.ball.position[1]])

        return patches

    def init_path(self, ax):
        ax.set_xlim([-2, 30])
        ax.set_ylim([-2, 25])

        xn = [n[0] for n in self.nodes]
        yn = [n[1] for n in self.nodes]
        nodes = ax.plot(xn, yn, "b-o")

        xh = [h[0] for h in self.holes]
        yh = [h[1] for h in self.holes]
        holes = ax.plot(xh, yh, "ko", markersize = 23)
        
        self.ball_pos, = ax.plot([self.ball.position[0]], [self.ball.position[1]], "go", markersize = 20)
        
        return nodes + holes + [self.ball_pos]