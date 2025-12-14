from moduls import *
from loader import *
import player_module,pipe_module

###
dims = (288*2,512)
config = load_setting()
###
def main(win_con=20, health=3, max_health=9, next_heal=10):
    # set up pygame
    pg.init()
    pg.mixer.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode(dims)
    pg.font.init()

    # load all assets
    assets = load_assets()


    # initialize player and pipe
    player = player_module.Player(1.5, dims[1] / 2 - 40, dims[0]/2 - 40, 1.2, assets.birds, health)
    pipes = [pipe_module.Pipe(300),pipe_module.Pipe(150),pipe_module.Pipe(10)]

    # start screen
    pg.display.set_caption("Flappy Bird")
    pg.display.set_icon(assets.icon)

    start_screen(screen, assets.backgrounds.day,dims)


    # declaring necessities
    bg = assets.backgrounds.cycle[0]
    scroll = 0
    frame_count = 1
    # main loop
    running = True
    while running:
        # background scroll
        scroll = scroll_bg(scroll,bg,screen,dims)

        # update player
        player_upd(player, screen)

        for pipe in pipes:
            # update pipes
            pipe_upd(pipe, assets.pipes.upper, assets.pipes.lower, screen)

            # collision detection
            collider(pipe,player,assets.sounds.hit)
            # scoring
            score(player,pipe,assets.sounds.point)
            # health and background cycles
            next_heal = heal(player, pipe, next_heal, max_health)

        # cycle time
        bg,frame_count = change_time(frame_count,assets.backgrounds.cycle)

        # draw base
        screen.blit(assets.base, (0, dims[1] - 112))
        screen.blit(assets.base, (336, dims[1] - 112))

        # display points and health
        show_stat(player,screen,assets.numbers)

        # event handling
        running = handle_event()

        # game over conditions
        running = end_game(player, screen, assets.sounds.death, assets.game_over, win_con, running,dims)

        clock.tick(200)
        pg.display.flip()

    pg.quit()


if __name__ == '__main__':
    main(**config)