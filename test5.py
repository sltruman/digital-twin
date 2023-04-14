import time
from digitaltwin import Scene,Editor, Workflow

scene = Scene(1024, 768)
scene.load('./data/scenes/空.json')
editor = Editor(scene)
workflow = Workflow(scene)

editor.add('ActiveObject','data/objects/default/box.urdf',[0,0,0],[0,0,0],[1,0,0])
editor.add('ActiveObject','data/objects/default/cylinder.urdf',[0,1,0],[0,0,0],[1,0,0])

print(scene.active_objs_by_name)

print(editor.select('11'))

while True:
    scene.update_for_tick(1/180.)
    time.sleep(1/180.)
