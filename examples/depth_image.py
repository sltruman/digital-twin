from time import time
import os
from practistyle import Scene,Workflow

scene = Scene(1024,768)
workflow = Workflow(scene)

data_dir = data.get_data_path()
scene.load(os.path.join(data_dir,'scenes/深度图.json'))
workflow.start()

import time
while True:
    scene.update_for_tick(1/180.)
    time.sleep(1/180.)