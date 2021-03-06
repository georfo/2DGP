import random
import gfw
from pico2d import *
from enemy import Enemy

next_wave = 0
wave_index = 0

def update():
    global next_wave
    next_wave -= gfw.delta_time
    if next_wave < 0:
        generate_wave()

def generate_wave():
    global wave_index, next_wave
    level = enemy_level()
    e = Enemy(wave_index, level)
    gfw.world.add(gfw.layer.enemy, e)
    print("적 생성,", wave_index, "번 웨이브, 레벨: ", level)
    wave_index += 1
    next_wave = random.uniform(2, 4)

def enemy_level():
    global wave_index
    level =  wave_index // 5 + 1
    if wave_index % 5 == 0:
         level += 1
    if level < 1: level = 1
    if level > 40: level = 40
    return level
