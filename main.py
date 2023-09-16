from taipy.gui import Gui, notify

parts = ["part-1", "part-2", "part-3", "part-4", "part-5"]

text = "no "
newline = "\n"
pages = [("/", "Home")]

page = f"""
<|layout|columns=1fr auto 1fr|class_name=container align_columns_center|width=100%|height=10vh|
<|part|class_name=title|
<|InjuryInspect|text|width=30px|height=30px|>
|>
|>

<|layout|columns=1fr 6fr 3fr|class_name=injury|
<|part|class_name=select|
<|side.png|image|width=80%|class_name=small_image|>
<|side.png|image|width=80%|class_name=small_image|>
<|side.png|image|width=80%|class_name=small_image|>
|>
<|part|class_name=diagram|
<|side.png|image|width=100%|class_name=big_image|>
{newline.join([f'<| |button|id={part}|on_action=info|>' for part in parts])}
|>
|>
    
"""

# {''.join([f'<| |button|id={part}|on_action=info|>' for part in parts])}

def info(state, id, action):
    state.text = id
    return 

Gui(page=page, css_file="main.css").run(use_reloader=True)