from taipy.gui import Gui, notify

parts = ["part-1", "part-2", "part-3", "part-4", "part-5"]

text = "no "
newline = "\n"

page = f"""
# hiiii # {{: .header}}

<|{{text}}|>

{newline.join([f'<| |button|id={part}|on_action=info|>' for part in parts])}

"""

# {''.join([f'<| |button|id={part}|on_action=info|>' for part in parts])}

def info(state, id, action):
    state.text = id
    return 

Gui(page=page, css_file="main.css").run(use_reloader=True)