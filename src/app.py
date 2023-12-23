import pygame as pg
import pymunk as pm
from pymunk.pygame_util import DrawOptions
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False
import random
random.seed(1)


WIDTH, HEIGHT = 600, 400
FPS = 60
RADIUS = 25 
def main():
    ball_radius = RADIUS
    ball_mass = 10
    ball_moment = pm.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pm.Body(ball_mass, ball_moment)
    ball_body.position = (WIDTH//4, 0)
    ball_shape = pm.Circle(ball_body, ball_radius)
    fixed_point_body = pm.Body(body_type=pm.Body.STATIC)
    fixed_point_body.position = (WIDTH//2,HEIGHT//4)
    ball_fixed_joint = pm.PinJoint(ball_body, fixed_point_body)

    space = pm.Space()
    space.gravity = (0, 900)
    space.add(ball_body, ball_shape, fixed_point_body, ball_fixed_joint)
    pg.init()
    surface = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption('Animation')
    clock = pg.time.Clock()
    draw_options = DrawOptions(surface)

    tick = 10

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return

        surface.fill((255,255,255))
        print(f'ball: pymunk = {ball_body.position}')
        print(f'ball: pymunk = {ball_body.position}')

        tick -= 1
        if tick == 0:
            new_ball_mass = 10
            new_ball_moment = pm.moment_for_circle(new_ball_mass, 0, RADIUS/1.5)
            new_ball_body = pm.Body(new_ball_mass, new_ball_moment)
            new_ball_shape = pm.Circle(new_ball_body, RADIUS/1.5)
            new_ball_body.position = (random.uniform(30, WIDTH-30), 0)
            space.add(new_ball_body, new_ball_shape)
            tick = 10

        space.step(1/FPS)
        space.debug_draw(draw_options)
        pg.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
