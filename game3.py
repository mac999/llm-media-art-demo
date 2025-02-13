# pygame으로 100개의 파티클이 점묘법으로 그려지도록 코딩해. 각 파티클의 원 반경과 색상은 파도치는 듯 하게 보이면 되. 각 파티클의 원과 색상은 랜덤하게 천천히 시간에 따라 변경되어야 해. 
import pygame
import random
import math

# 초기 설정
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Wave Effect")

# 색상과 파티클 설정
BLACK = (0, 0, 0)
PARTICLE_COUNT = 100

# 파티클 데이터 구조
particles = []
for _ in range(PARTICLE_COUNT):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    radius = random.uniform(2, 5)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    speed = random.uniform(0.01, 0.03)
    phase = random.uniform(0, math.pi * 2)
    particles.append({"x": x, "y": y, "radius": radius, "color": color, "speed": speed, "phase": phase})

clock = pygame.time.Clock()
running = True

def update_particles():
    for particle in particles:
        # 반경 변동
        particle["radius"] = 3 + 2 * math.sin(particle["phase"])
        particle["phase"] += particle["speed"]

        # 색상 변동
        r = (particle["color"][0] + random.randint(-2, 2)) % 256
        g = (particle["color"][1] + random.randint(-2, 2)) % 256
        b = (particle["color"][2] + random.randint(-2, 2)) % 256
        particle["color"] = (r, g, b)

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 파티클 업데이트
    update_particles()

    # 파티클 그리기
    for particle in particles:
        pygame.draw.circle(screen, particle["color"], (int(particle["x"]), int(particle["y"])), int(particle["radius"]))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

pygame.quit()