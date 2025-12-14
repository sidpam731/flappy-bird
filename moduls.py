import pygame as pg
import time

def start_screen(screen, bg,dims):
    start_img = pg.image.load("resources/start_screen.png")
    waiting = True
    while waiting:
        screen.blit(bg, (0, 0))
        screen.blit(bg, (0 + dims[0]/2, 0))
        screen.blit(bg, (0 - dims[0]/2, 0))
        screen.blit(start_img, (dims[0]/2 - 92, dims[1] / 2 - 150))

        pg.display.flip()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

        keys = pg.key.get_pressed()
        waiter_keys = any(keys[k] for k in range(len(keys)) if k != pg.K_q)
        if waiter_keys:
            waiting = False
        elif keys[pg.K_q]:
            pg.quit()
            exit()
        pg.time.Clock().tick(30)

def scroll_bg(i, bg, screen,dims):
    screen.blit(bg, (i, 0))
    screen.blit(bg, (i + (dims[0]/2), 0))
    screen.blit(bg, (i - (dims[0]/2), 0))
    i = (i - 0.2) % (dims[0]/2)
    return i

def pipe_upd(pipe,upper,lower,screen):
    player_cords = pipe.update(1)
    x, y_s = player_cords[0], (player_cords[1], player_cords[2])
    screen.blit(lower, (x, y_s[0]))
    screen.blit(upper, (x, y_s[1]))

def player_upd(player,screen):
    cords = player.update(pg.key.get_pressed()[pg.K_SPACE])
    char = cords[0]
    cords = (int(cords[2]), int(cords[1]))
    screen.blit(char, cords)

def overlap(b1, b2):
    return not (b1[1] < b2[0] or
                b1[0] > b2[1] or
                b1[3] < b2[2] or
                b1[2] > b2[3])

def collider(pipe,player,hit):
    player_box = player.get_box()
    lower_box = pipe.get_box("lower")
    upper_box = pipe.get_box("upper")
    is_overlapping = overlap(player_box, lower_box) or overlap(player_box, upper_box)

    if is_overlapping and not pipe.cool_down:
        player.health -= 1
        hit.play()
        pipe.pointed = True
        pipe.cool_down = True

def score(player,pipe,point):
    if (not pipe.pointed) and (pipe.lower > player.y_lvl > pipe.upper + pipe.width) and (player.x > pipe.x):
        player.points += 1
        point.play()
        pipe.pointed = True

def heal(player,pipe,nxt_heal,m_health):
    if pipe.pointed and player.points == nxt_heal and player.health < m_health:
        nxt_heal += 10
        player.health += 1
    return nxt_heal

def change_time(cycle_time,bgs):
    cycle_time+=1
    if cycle_time==9600:
        cycle_time=1
    index = cycle_time//240
    return bgs[index],cycle_time

def show_stat(player,screen,nums):
    str_point = str(player.points).zfill(2)
    screen.blit(nums[int(str_point[0])], (0, 0))
    screen.blit(nums[int(str_point[1])], (24, 0))
    screen.blit(nums[player.health], (0, 40))

def handle_event(running=True):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    if pg.key.get_pressed()[pg.K_q]:
        running = False
    return running

def end_game(player,screen,death,game_over,win_con,running,dims):
    if player.health == 0 or player.is_touching:
        death.play()
        screen.blit(game_over, (dims[0]/2 - 96, dims[1] / 2 + 10))
        pg.display.flip()
        time.sleep(2)
        running = False

    elif player.points == win_con or player.points == 99:
        screen.blit(game_over, (dims[0]/2 - 96, dims[1] / 2 + 10))
        pg.display.flip()
        time.sleep(2)
        running = False
    return running
