from taipy.gui import Gui, notify
from backend.py import diagnose

text = "no "
newline = "\n"
pages = [("/", "Home")]
images = ("side.png", "topbottom.png")
image = 0
spot_names = [["Plantar fascia", "Ligaments", "Achilles tendon", "Muscles",  "Sesamoid bone", "Fibula", "Talus", "Tibia"], ["Nail body", "Growth plate", "Proximal inter-phalangeal joint", "Metatarsales", "Tendons", "Phalanges", "Calcaneus", "Interdigit spaces", "Digitoplantar fold", "Anterior longitudinal sulcus", "Plantar region"]]


# {''.join([f'<| |button|class_name={part}|on_action=info|>' for part in parts])}

def changeImage(state, id, action):
    state.image = int(id[-1])
    # state.spots = newline.join([f'<| |button|class_name={images[int(id[-1])][0]}{i}|on_action=info|>' for i in range(len(spot_names[int(id[-1])]))])
    # print(newline.join([f'<| |button|class_name={images[int(id[-1])][0]}{i}|on_action=info|>' for i in range(len(spot_names[int(id[-1])]))]))
    return

def changeSpots(state, value):
    return

def on_change(state, var_name, var_value):
    if var_name == "image":
        print(var_value)
        # state.spots = newline.join([f'<| |button|class_name={images[var_value][0]}{i}|on_action=info|>' for i in range(len(spot_names[var_value]))])
        # changeSpots(state, var_value)
        return

def info(state, id, action):
    state.text = id
    return 


page = f"""
<|layout|columns=1fr 1fr|class_name=container align_columns_center|width=100%|height=10vh|
<|part|class_name=title|
<|title.png|image|>
|>
<|part|class_name=slogan-container|
<|expedite your recovery!|text|class_name=slogan|>
|>
|>

<|d-block|
<|part|class_name=section|id=section-1|
<|The Problem|text|class_name=heading|>
<|Athletes invest immense passion and dedication into their sports endeavors, yet the risk of injuries remains a prevalent concern. For individuals new to a sport, identifying the specific body part that has been injured can be challenging. Without a clear understanding of medical terminology, it becomes difficult to accurately search for relevant information online, hindering the ability to find appropriate guidance. Moreover, seeking professional help from physiologists can be expensive and the vast array of information available online often proves overwhelming. All these barriers make it difficult for individuals to find a suitable and reassuring solution.|text|class_name=paragraph|>
|>

<|part|class_name=section|id=section-2|
<|Our Mission|text|class_name=heading|>
<|At InjuryInspect, we provide an interface that ensures that everyone, irrespective of their anatomical knowledge, can seamlessly access vital information. Visualize a human body with interactive points spanning every inch—each representing a potential site of discomfort. By pinpointing the precise area of their body in distress, users can access a list of potential injuries, as well as a list of recovery tips. We firmly believe that sports are an essential component of people's communities and identities, and through this interface, we can support athletes in their pursuit of a fulfilling and healthy lifestyle.|text|class_name=paragraph|>
|>

<|part|class_name=section|id=section-3|
<|Instructions|text|class_name=heading|>
<|Click on the corresponding area of the image below that corresponds to where you are experiencing pain. Our intuitive design ensures that you can swiftly find the information you need to start your path to recovery.|text|class_name=paragraph|>
|>

|>
<|layout|columns=1.5fr 6fr 4fr|class_name=injury|
<|part|class_name=select|
<|side.png|image|width=100%|class_name=small_image|id=img-0|on_action=changeImage|>
<|topbottom.png|image|width=100%|class_name=small_image|id=img-1|on_action=changeImage|>
|>
<|part|class_name=diagram|
<|{{images[image]}}|image|width=100%|class_name=big_image|>
<|{{images[image]}}|button|class_name={{images[image][0]}}0|class_name={{images[image][0]}}0|on_action=info|>
<|{{images[image]}}|button|class_name={{images[image][0]}}1|class_name={{images[image][0]}}1|on_action=info|>
<|{{images[image]}}|button|class_name={{images[image][0]}}2|class_name={{images[image][0]}}2|on_action=info|>
<|{{images[image]}}|button|class_name={{images[image][0]}}3|class_name={{images[image][0]}}3|on_action=info|>
<|{{images[image]}}|button|class_name={{images[image][0]}}4|class_name={{images[image][0]}}4|on_action=info|>
<|{{images[image]}}|button|class_name={{images[image][0]}}5|class_name={{images[image][0]}}5|on_action=info|>
<|{{images[image]}}|button|class_name={{images[image][0]}}6|class_name={{images[image][0]}}6|on_action=info|>
<|{{images[image]}}|button|class_name={{images[image][0]}}7|class_name={{images[image][0]}}7|on_action=info|>
<|{{images[image]}}|button|class_name={{images[image][0]}}8|class_name={{images[image][0]}}8|on_action=info|>
<|{{images[image]}}|button|class_name={{images[image][0]}}9|class_name={{images[image][0]}}9|on_action=info|>
<|{{images[image]}}|button|class_name={{images[image][0]}}10|class_name={{images[image][0]}}10|on_action=info|>
|>
<|part|class_name=info|
# idk
|>
|>
    
"""

Gui(page=page, css_file="main.css").run(use_reloader=True)