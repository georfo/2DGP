from pico2d import *

open_canvas()

gra = load_image('grass.png')
ch = load_image('character.png')



x = 0

while x < 800:
	clear_canvas_now()
	gra.draw(400, 30)
	ch.draw(x, 85)
	update_canvas()
	# page_fliping
	evts = get_events()
	# for e i in evnt:
	#	print(e)

	x += 2
	delay(0.02)

close_canvas()

#game loop
#- logic = update()
# - logic
# - event handring
# - render = draw()