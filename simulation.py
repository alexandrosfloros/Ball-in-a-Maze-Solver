import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from control import *


def animate_model(model):
    control = Algorithm(model)

    fig = plt.figure(num="Simulation")
    ax = fig.add_axes([0, 0, 1, 1])

    def init():
        return model.init_path(ax)

    def update(frame_number):
        control.ball.position[0] += control.ball.velocity[0]
        control.ball.position[1] += control.ball.velocity[1]

        control.ball.velocity[0] += control.ball.acceleration[0]
        control.ball.velocity[1] += control.ball.acceleration[1]

        control.run()

        if control.finished or control.failed:
            animation.event_source.stop()

        return model.update_ball(ax)

    animation = FuncAnimation(
        fig=fig,
        func=update,
        init_func=init,
        blit=True,
        cache_frame_data=False,
        interval=10,
    )

    plt.show()
