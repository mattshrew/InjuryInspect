from taipy.gui import Gui, notify
from backend import diagnose

text = "no "
newline = "\n"
pages = [("/", "Home")]
images = ("side.png", "topbottom.png")
image = 0
spot_names = [["Plantar fascia", "Ligaments", "Achilles tendon", "Muscles",  "Sesamoid bone", "Fibula", "Talus", "Tibia"], ["Nail body", "Growth plate", "Proximal inter-phalangeal joint", "Metatarsales", "Tendons", "Phalanges", "Calcaneus", "Interdigit spaces", "Digitoplantar fold", "Anterior longitudinal sulcus", "Plantar region"]]
part, purpose = "", ("", "")
injuries = False
injury1, injury2, injury3, injury4 = ("", "", ""), ("", "", ""), ("", "", ""), ("", "", "")

def changeImage(state, id, action):
    state.image = int(id[-1])
    return

def info(state, id, action):
    part = spot_names[int(id[0])][int(id[2])]
    new_data = diagnose(part)
    state.part = part
    state.purpose = ("Purpose: ", new_data['partPurpose'])
    if len(new_data['injuries']): state.injuries = True
    else: state.injuries = False
    if len(new_data['injuries']): state.injury1 = (new_data['injuries'][0], ": ", new_data[new_data['injuries'][0]])
    else: state.injury1 = ("", "", "")
    if len(new_data['injuries']) > 1: state.injury2 = (new_data['injuries'][1], ": ", new_data[new_data['injuries'][1]])
    else: state.injury2 = ("", "", "")
    if len(new_data['injuries']) > 2: state.injury3 = (new_data['injuries'][2], ": ", new_data[new_data['injuries'][2]])
    else: state.injury3 = ("", "", "")
    if len(new_data['injuries']) > 3: state.injury4 = (new_data['injuries'][3], ": ", new_data[new_data['injuries'][3]])
    else: state.injury4 = ("", "", "")
    print(new_data)
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
<|{{images[image]}}|button|id={{image}}-0|class_name={{images[image][0]}}0|on_action=info|>
<|{{images[image]}}|button|id={{image}}-1|class_name={{images[image][0]}}1|on_action=info|>
<|{{images[image]}}|button|id={{image}}-2|class_name={{images[image][0]}}2|on_action=info|>
<|{{images[image]}}|button|id={{image}}-3|class_name={{images[image][0]}}3|on_action=info|>
<|{{images[image]}}|button|id={{image}}-4|class_name={{images[image][0]}}4|on_action=info|>
<|{{images[image]}}|button|id={{image}}-5|class_name={{images[image][0]}}5|on_action=info|>
<|{{images[image]}}|button|id={{image}}-6|class_name={{images[image][0]}}6|on_action=info|>
<|{{images[image]}}|button|id={{image}}-7|class_name={{images[image][0]}}7|on_action=info|>
<|{{images[image]}}|button|id={{image}}-8|class_name={{images[image][0]}}8|on_action=info|>
<|{{images[image]}}|button|id={{image}}-9|class_name={{images[image][0]}}9|on_action=info|>
<|{{images[image]}}|button|id={{image}}-10|class_name={{images[image][0]}}10|on_action=info|>
|>
<|part|class_name=info|
<|{{part}}|>    

<|{{purpose[0]}}|>
<|{{purpose[1]}}|>

<|{"Injuries" if {injuries}==True else " "}|>

<|{{injury1[0]}}{{injury1[1]}}|>

<|{{injury1[2]}}|>

<|{{injury2[0]}}{{injury2[1]}}|>

<|{{injury2[2]}}|>

<|{{injury3[0]}}{{injury3[1]}}|>

<|{{injury3[2]}}|>

<|{{injury4[0]}}{{injury4[1]}}|>

<|{{injury4[2]}}|>
|>
|>
    
"""

Gui(page=page, css_file="main.css").run(use_reloader=True)