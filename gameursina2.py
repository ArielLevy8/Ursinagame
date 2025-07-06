from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()

window.fullscreen = True

player = FirstPersonController()
Sky(texture='sky_sunset.jpg')
block_types = {
    # if the player clicks 1,2,3 etc. blocks get selected: comment by Ariel
    '1': ('grass.png', color.white),
    '2': ('brick.png', color.brown),
    '3': ('brick.png', color.red),
    '4': ('brick.png', color.blue),
    '5': ('brick.png', color.green),
    '6': ('brick.png', color.orange),
    '7': ('brick.png', color.yellow),
    '8': ('brick.png', color.gray),
    '9': ('brick.png', color.cyan),
    'b': ('brick.png', color.black),
    '0': ('brick.png', color.white),
    'p': ('brick.png', color.pink),
    'm': ('brick.png', color.magenta),
    't': ('white_cube', color.turquoise),
    'v': ('brick.png', color.violet),
    'l': ('brick.png', color.lime),
    'g': ('white_cube', color.gold),
}


selected_block_type = '1' # player starts with the grass block because the key '1' corresponds with the grass.png block: comment by Ariel



boxes = []
for i in range(25):
    for j in range(25):
        box = Button(color=color.white, model='cube', position=(j,0,i),
                     texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(box)

def input(key):
    global selected_block_type

    if key == 'f':
        player.gravity = 0 if key == 'f' else 2000
    if key == 'down arrow':
        player.gravity += 1
    if key == 'up arrow':
        player.gravity -= 0.1

    if key == 'escape':
        application.quit() # The player will exit the application when the 'esc' button is pressed: comment by Ariel


    if key in block_types:
        selected_block_type = key
        print(f'selected block type: {selected_block_type}')

    hit_info = mouse.hovered_entity
    if hit_info and hit_info in boxes:
        if key == 'left mouse down':
            texture, color = block_types[selected_block_type]
            new = Button(color=color, model='cube', position=hit_info.position + mouse.normal,
                         texture=texture, parent=scene, origin_y=0.5)
            boxes.append(new)
        if key == 'right mouse down':
            boxes.remove(hit_info)
            destroy(hit_info)

app.run()