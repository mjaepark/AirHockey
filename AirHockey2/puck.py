import pygame
import random as rand
import math
import constants as const
import globals as glob
from random import randint


class Puck:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = const.PUCK_SIZE
        self.speed = const.PUCK_SPEED
        self.mass = const.PUCK_MASS
        self.angle = 0
        self.dec = True
        self.color = const.WHITE

    def move(self, time_delta):
        self.x += math.sin(self.angle) * self.speed * time_delta
        self.y -= math.cos(self.angle) * self.speed * time_delta

        self.speed *= const.FRICTION


    def check_boundary(self, width, height):
        # right side
        if self.x + self.radius > width:
            self.x = 2 * (width - self.radius) - self.x
            self.angle = -self.angle

        # left side
        elif self.x - self.radius < 0:
            self.x = 2 * self.radius - self.x
            self.angle = -self.angle

        # bottom
        if self.y + self.radius > height:
            self.y = 2 * (height - self.radius) - self.y
            self.angle = math.pi - self.angle

        # top
        elif self.y - self.radius < 0:
            self.y = 2 * self.radius - self.y
            self.angle = math.pi - self.angle

    def add_vectors(self, p1, p2):
        x = math.sin(p1[0]) * p1[1] + math.sin(p2[0]) * p2[1]
        y = math.cos(p1[0]) * p1[1] + math.cos(p2[0]) * p2[1]

        length = math.hypot(x, y)
        angle = math.pi / 2 - math.atan2(y, x)
        return angle, length

    def collision_paddle(self, paddle):
        """
        Checks collision between circles using the distance formula:
        distance = sqrt(dx**2 + dy**2)
        """
        dx = self.x - paddle.x
        dy = self.y - paddle.y

        # distance between the centers of the circle
        distance = math.hypot(dx, dy)

        # no collision takes place.
        if distance > self.radius + paddle.radius:
            return False

        # calculates angle of projection.
        tangent = math.atan2(dy, dx)
        temp_angle = math.pi / 2 + tangent
        total_mass = self.mass + paddle.mass

        # The new vector for puck formed after collision.
        vec_a = (self.angle, self.speed * (self.mass - paddle.mass) / total_mass)
        vec_b = (temp_angle, 2 * paddle.speed * paddle.mass / total_mass)

        (self.angle, self.speed) = self.add_vectors(vec_a, vec_b)

        # speed should never exceed a certain limit.
        if self.speed > const.MAX_SPEED:
            self.speed = const.MAX_SPEED

        # new vector for paddle without changing the speed.
        vec_a = (paddle.angle, paddle.speed * (paddle.mass - self.mass) / total_mass)
        vec_b = (temp_angle + math.pi, 2 * self.speed * self.mass / total_mass)

        temp_speed = paddle.speed
        (paddle.angle, paddle.speed) = self.add_vectors(vec_a, vec_b)
        paddle.speed = temp_speed

        # To prevent puck and paddle from sticking.
        offset = 0.5 * (self.radius + paddle.radius - distance + 1)
        self.x += math.sin(temp_angle) * offset
        self.y -= math.cos(temp_angle) * offset
        paddle.x -= math.sin(temp_angle) * offset
        paddle.y += math.cos(temp_angle) * offset
        return True

    def round_reset(self, player):
        if player == 1:
            self.x = 3*const.WIDTH/4
        if player == 2:
            self.x = const.WIDTH/4
        self.y = const.HEIGHT/2
        self.angle = 0
        self.speed = 0

    def reset(self, speed, player):
        if player == 1:
            self.angle = rand.uniform(-math.pi, 0)
        elif player == 2:
            self.angle = rand.uniform(0, math.pi)
        self.speed = speed
        self.x = const.WIDTH / 2
        self.y = const.HEIGHT / 2

    def end_reset(self, speed):
        self.angle = 0
        self.speed = speed
        self.x = const.WIDTH / 2
        self.y = const.HEIGHT / 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def puckChange(self):
        if self.radius > 34:
            self.dec = True
            self.color = glob.WnB[1]
        if self.radius < 27:
            self.dec = False
            self.color = glob.WnB[0]

    def draw_crazy(self, screen):
        if self.dec:
            self.radius -= 1
        else:
            self.radius += 1
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)


    def get_pos(self):
        print(self.x, self.y)