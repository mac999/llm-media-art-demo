# pygame으로 100개의 원을 그려주고, 각 원은 시간에 따라 크기와 색상이 시간에 따라 천천히 변화되어야 해. 해당 값이 변화되는 함수는 sine을 사용해. 
import pygame
import math

# 초기 설정
pygame.init()

# 화면 크기 및 색상 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sine Wave Circles")

BLACK = (0, 0, 0)

# 원 데이터 초기화
NUM_CIRCLES = 100
circles = []
for i in range(NUM_CIRCLES):
    circle = {
        "x": WIDTH // 2 + math.sin(i) * 200,  # 초기 x 위치
        "y": HEIGHT // 2 + math.cos(i) * 200,  # 초기 y 위치
        "radius": 10 + 5 * math.sin(i),  # 초기 반지름
        "color": (255, 255, 255),  # 초기 색상
        "phase": i * 0.1  # 각 원의 위상 차이
    }
    circles.append(circle)

# 프레임 속도 설정
clock = pygame.time.Clock()
running = True

def update_circle(circle, time):
    # 반지름과 색상 업데이트 (사인파 기반)
    new_radius = 10 + 5 * math.sin(time + circle["phase"])
    new_color = (
        127 + 127 * math.sin(time + circle["phase"]),
        127 + 127 * math.sin(time + circle["phase"] + 2 * math.pi / 3),
        127 + 127 * math.sin(time + circle["phase"] + 4 * math.pi / 3),
    )
    circle["radius"] = new_radius
    circle["color"] = new_color

# 메인 루프
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 현재 시간 계산
    current_time = pygame.time.get_ticks() / 1000.0

    # 원 업데이트 및 그리기
    for circle in circles:
        update_circle(circle, current_time)
        pygame.draw.circle(screen, circle["color"], (int(circle["x"]), int(circle["y"])), int(circle["radius"]))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
