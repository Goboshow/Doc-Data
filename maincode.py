#GUI - I can already tell I'm going to have fun on this project         :D

#first, here's a quick print thing to make sure it actually works as it should.

print("Program Started")

#alright, here's the actual GUI
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Doctor D")
root.geometry("800x600")
root.resizable(True, True)

#Database
illness_db = {
    "Common Cold": {"symptoms": ["cough", "runny nose", "sore throat"],"description":"Mild viral infection","treatment":"Rest and fluids"},
    "Flu": {"symptoms": ["fever", "cough", "fatigue", "headache"], "description": "Viral respiratory illness","treatment":"Rest and hydration"},
    "Asthma": {"symptoms": ["shortness of breath", "cough", "chest tightness"], "description": "Airway inflammation","treatment":"Inhalers"},
    "Pneumonia": {"symptoms": ["fever", "cough", "chest pain"], "description":"Lung infection", "treatment":"Antibiotics"},
    "Bronchitis": {"symptoms": ["cough", "fatigue", "shortness of breath"], "description":"Inflamed airways", "treatment":"Rest"},
    "COVID-19": {"symptoms": ["fever", "cough", "fatigue", "loss of taste"], "description":"Coronavirus Infection", "treatment":"Supportive care"},
    "Diabetes": {"symptoms": ["thirst", "fatigue", "frequent urination"], "description":"Blood sugar disorder", "treatment":"Insulin"},
    "Migraine": {"symptoms": ["headache", "nausea", "light sensitivity"], "description":"Severe headaches", "treatment":"Pray to your gods"},
    "Depression": {"symptoms": ["low mood", "fatigue", "sleep problems"], "description":"Emotional Disorder","treatment":"Therapy"},
    "Anxiety": {"symptoms": ["restlessness", "fast heart rate", "sweating"], "description":"Excessive worrying", "treatment":"Take a break from coding"},
    "Food Poisoning": {"symptoms": ["nausea", "vomiting", "diarrhea"], "description":"Contaminated food illness","treatment":"Hydration"},
    "Appendicitis": {"symptoms": ["abdominal pain", "fever", "nausea"], "description":"Inflamed appendix","treatment":"Surgery"},
    "Meningitis": {"symptoms": ["fever", "stiff neck", "headache"], "description":"Brain inflammation","treatment":"Emergency care"},
    "Arthritis": {"symptoms": ["joint pain", "stiffness"], "description":"Joint inflammation", "treatment":"Pain relief"},
    "Eczema": {"symptoms": ["itchy skin", "rash"], "description":"Skin irritation", "treatment":"Cream"},
    "Anemia": {"symptoms": ["fatigue", "pale skin"], "description":"Low red blood cells", "treatment":"Iron"},
    "Allergy": {"symptoms": ["sneezing", "itchy eyes"], "description":"Immune reaction", "treatment":"Antihistamines"},
    "Heatstroke": {"symptoms": ["high temperature", "confusion"], "description":"Overheating", "treatment":"Cooling"},
    "Bite Wound": {"symptoms": ["deep wound"], "description":"A wound caused by the mouth of an animal or human", "treatment":"Clean the bite as much as possible and seek medical attention"},
    "Asbestosis": {"symptoms": ["shortness of breath", "cough"], "description":"Lung condition caused by Asbestos", "treatment":"Pray to whichever god you believe in"},
    "Brain Death": {"symptoms": ["minor death"], "description":"Brain not working. I have a feeling you don't have this", "treatment":"You're cooked ong"},
    "Chronic Fatigue Syndrome": {"symptoms": ["fatigue", "insomnia", "brain fog"], "description":"Extreme tiredness across the body", "treatment":"Rest and relaxation"},
    "Dehydration": {"symptoms": ["fatigue", "dry mouth", "dry mouth"], "description":"Lack of hydration, very much not good", "treatment": "sippie sips on your drinkie drinks"},
    "Detached Retina": {"symptoms": ["floaters", "blurred vision"], "description}":"A retina detached from the eye lining", "treatment":"Get medical attention else you may become blind"},
    "Dislocated Kneecap": {"symptoms": ["pain", "swelling", "bruising", "cannot stand", "moving unnaturally"], "description":"Kneecap (patella) moves out of place because of injury", "treatment":"seek medical attention"},
    "Dislocated Shoulder": {"symptoms": ["pain", "swelling", "bruising", "moving unnaturally"], "description":"Upper arm bone comes out of place from shoulder socket", "treatment":"Seek medical treatment, unless you feel brave and want to push"},
    "Perforated Eardrum": {"symptoms": ["ear infection", "loud noise", "pressure change", "hearing loss", "earache", "bleeding", "dizziness"], "description":"A hole or tear in the eardrum", "treatment":"usually heals within 2 months, however may need antibiotics"},
    "Ehlers-Danlos Syndrome": {"symptoms": ["hypermobility", "stretchy skin", "fragile skin", "joint pain"], "description":"Rare inherited conditions that affect tissues", "treatment":"physiotherapists and occupational therapists can help, however there is no specific cure due to the many different types of EDS there are"},
    "Epilepsy": {"symptoms": ["seizures", "fainting", "becoming limp", "unusual behaviour", "fidgeting", "unawareness"], "description":"A condition that affects the brain and causes seizures", "treatment":"check-ups, talk to your local doctor-dude (not Doc. D) and ask for a care plan"},
    "Eye Cancer": {"symptoms": ["bulging", "blurred vision", "floaters", "loss of vision", "irritation"], "description":"Mutated cells in the tissues of the eyes", "treatment":"Chop out the eye, blast it with radiation, or have a pricey surgery"},
    "Pregnancy": {"symptoms": ["bulging", "fainting", "unusual behaviour", "minor death", "sleep problems", "low mood", "moving unnaturally", "joint pain", "fatigue", "confusion"], "description":"A parasite inside a stomach", "treatment":"Do you wanna keep it? Yes? Just wait for a few months. If not, just grab a box cutter or something"},
    "Psychotic Depression": {"symptoms": ["fatigue", "sleep problems", "unusual behaviour", "low mood"], "description":"Severe depression alongside hallucinations and whatnot", "treatment":"Therapy, and take a break from coding"},
    "Rabies": {"symptoms": ["numbness", "restlessness", "sleep problems", "pale skin", "deep wound"], "description":"A dangerous infection "},
    "Decapitation": {"symptoms": ["minor death", "sleep problems", "pale skin", "fainting", "numbness", "deep wound", "joint pain", "low mood", "cannot stand", "hearing loss", "bleeding"], "description":"Head go bye bye", "treatment":"Hope there's a doctor that's good at sewing"},
    "Spontaneous Human Combustion": {"symptoms": ["minor death", "becoming limp", "unusual behaviour", "loss of vision", "moving unnaturally", "confusion", "bleeding", "unawareness"], "description":"When the Human Body Combusts Spontaneously", "treatment":"You might be extremely doomed ngl"},
    "Schizophrenia": {"symptoms": ["hallucinations", "delusions", "confusion", "low mood", "fatigue", "sleep problems"], "description":"Seeing, hearing or believing things that are not real", "treatment":"Therapy if you want. Or just look at all the pretty shapes and colours"},
    "Scoliosis": {"symptoms": ["bulging", "pain"], "description":"When the ribs don't rib well, and you end up with the wrong sizes", "treatment":"Sometimes surgery, but mostly a back brace."},
    "Scurvy": {"symptoms": ["fatigue", "low mood", "pain", "joint pain", "bulging", "rash", "fragile skin"], "description":"Not enough vitamin C in your diet over a long period of time", "treatment":"EAT. YOUR. VEGETABLES"},
    "Myopia": {"symptoms": ["blurred vision", "itchy eyes"], "description":"Being able to see close up, but not far away. Just short sightedness", "treatment":"Glasses, or laser eye surgery if you're rich and lucky"},
    "Insomnia": {"symptoms": ["sleep problems", "fatigue"], "description":"The inability to sleep", "treatment":"Just sleep it off. Or just go to therapy"},
    "Stomach Ulcer": {"symptoms": ["pain", "bulging"], "description":"A literal ulcer in the stomach", "treatment":"Laxatives. A lot of Laxatives. Or sugar free gummy bears!"},
    "Stroke": {"symptoms": ["minor death", "pain", "blurred vision", "confusion", "pale skin", "becoming limp", "moving unnaturally", "cannot stand", "loss of vision", "confusion"], "description":"A blocked blood supply to the brain", "treatment":"See a medical professional or call an ambulance as soon as physically possible"},
    "Tetanus": {"symptoms": ["pain", "sweating", "fast heart rate", "restlessness", "moving unnaturally", "confusion"], "description":"A bacteria that enters the body through wounds. Can be fatal OwO", "treatment":"seek medical attention before you experience the fuzzies"},
    "Tics": {"symptoms": ["moving unnaturally", "restlessness", "loud noise", "sleep problems", "cough", "confusion"], "description":"A neurological disorder that results in unnatural movements of the body, along with unnatural sounds", "treatment":"There is no currently known treatment, apart from some expensive tech that helps slightly"},
    "Kharaa": {"symptoms": ["confusion", "unusual behaviour", "pale skin"], "description":"Green clusters formed on the skin, caused by ocean bacteria", "treatment":"Some cool enzyme"},
    "Nausea": {"symptoms": ["nausea"], "description":"Nausea", "treatment":"Sleep"},
    "Chemical Burns": {"symptoms": ["confusion", "pain", "deep wound", "bulging"], "description":"A burn caused by chemicals or acid on the skin", "treatment":"Avoid drinking acid for the time being, and be sure to take intibiotics. Or surgery if it is severe"},
    "Acid Reflux": {"symptoms": ["cough", "bulging", "pain", "heartburn", "numbness"], "description":"A burning feeling in the chest caused by stomach acid travelling up towards the throat", "treatment":"Eat smaller, more frequent meals, and find ways to relax"},
    "Alcohol Misuse": {"symptoms": ["unusual behaviour", "fainting", "fatigue", "becoming limp", "irritation", "cough", "sleep problems"], "description":"When you drink in a way that's harmful, or are dependent on alcohol", "treatment":"Attempt to abstain from drinking, and DO NOT DRIVE (unless you wanna have a good time)"},
    "Alcohol Poisoning": {"symptoms": ["confusion", "unusual behaviour", "fatigue", "becoming limp", "numbness", "fainting"], "description":"When you drink alcohol faster than your body can process it", "treatment":"Abstain from drinking, and go to the hospital if serious (DO NOT DRIVE YOURSELF)"},
    "Alzheimer's Disease": {"symptoms": ["confusion", "unusual behaviour", "fatigue", "delusions", "loss of vision", "brain fog"], "description":"A group of symptoms associated with a decline of brain functioning. It is the most common cause of dementia", "treatment": "Nobody can remember (seriously. This isn't a joke this time.)"},
    "Aneurysm": {"symptoms": ["pain", "headache", "blurred vision", "unusual behaviour", "nausea", "confusion"], "description": "A swelling in a blood vessel in your brain, can sometimes burst", "treatment":"possibly surgery, usually surgical clipping or endovascular surgery"},
    "Bipolar Disorder": {"symptoms": ["low mood", "unusual behaviour", "fatigue", "fainting"], "description":"mental health condition that causes extreme mood changes, to the point where you're practically a different person", "treatment":"medicines and therapy. If not, you're doomed in another"},
    "Carpal Tunnel Syndrome": {"symptoms": ["pain", "numbness", "fatigue"], "descripyion":"Pressure on a nerve in your wrist. Causes tingling, numbness and pain in hands and fingers", "treatment":"Usually goes away in a span of 1 day to 9 months. Like an unborn baby"},
    "Crohn's Disease": {"symptoms": ["diarrhea", "pain", "fatigue", "unusual behaviour"], "description":"Inflamed Bowels / Guts", "treatment":"Just trust your gut. Or, don't. Instead, arrange blood tests with a medical professional (not Dr. D, although I know he's a true professional)"},
    "Cancer": {"symptoms": ["bulging", "fatigue", "unusual behaviour", "frequent urination", "pain"], "description":"Cells in the body growing in an uncontrolled way", "treatment":"Radiation blasting or surgery are most common, however chemotharapy and radiotherapy are the posh terms"},
    "Cirrhosis": {"symptoms": ["fatigue", "pain", "sickness", "pale skin"], "description":"The liver is severely damaged", "treatment":"While it cannot be cured, laxative medicine or beta blockers and antibiotics can work to slow it down / stop it getting worse"},
    "Constipation": {"symptoms": ["pain", "unusual behaviour", "pale skin", "bulging", "sweating", "confusion", "low mood"], "description":"When stools be too hard to stool", "treatment":"Eat a bowl of laxatives (or two). Or, you could probably just get sucker-punched so hard it flies out"},
    "Cystic Fibrosis": {"symptoms": ["cough", "shortness of breath", "pain", "bulging", "confusion"], "description":"A rare inherited genetic condition that causes breathing and digestive problems", "treatment":"While there is no current cure for it, some medicines and therapies can offer support to postpone the effects"},
    "Cytomegalovirus": {"symptoms": ["fatigue", "cough", "shortness of breath", "irritation"], "description":"A common virus that's usually harmless. Often affects babies and people with weak immune systems", "treatment":"Usually get better without treatment within about 3 weeks"},
    "Flat Feet": {"symptoms": ["pain", "fatigue", "bulging"], "description":"A usually harmless genetic condition causing the arch in the feet to disappear", "treatment":"It is usually harmless, however in some cases insoles for shoes can be purchased to reduce pain"},
    "Glaucoma": {"symptoms": ["pain", "bulging", "fragile skin", "headache"], "description":"An eye condition where the main nerve that connects the eye and brain becomes damaged", "treatment":"Eye drops can help decrease the fluid in the eye, laser treatment does the same. Surgery is also an option although pricey"},
    "Haemochromatosis": {"symptoms": ["fatigue", "pain", "low mood", "unusual behaviour", "pale skin"], "description":"The build up of iron in the body (an iron overload)", "treatment":"Diet management and medicines"},
    "High Blood Pressure": {"symptoms": ["headache", "pain", "blurred vision"], "description": "Hypertension can lead to heart attacks or strokes, and is literally what it says on the cover", "treatment": "Diet management, daily exercise, and do not drink too much alcohol (no more than 14 units a week)"}
}

all_symptoms = sorted({symptom for data in illness_db.values() for symptom in data ["symptoms"]})

def clear():
    for w in root.winfo_children():
        w.destroy()

#Logic

def find_matches(selected):
    return[
        illness for illness, data in illness_db.items()
        if all(symptom in data["symptoms"] for symptom in selected)
    ]

#Load Image

bg_image = None
try:
    bg_image = tk.PhotoImage(file="Doc Dat.png")
except Exception as e:
    print("Image cannot load, so here's an analogue smiley face instead:  :)", e)

#title screen thingy, ya know?

original_image = Image.open("Doc Dat.png")
bg_image = None
    
def title_screen():
    clear()
    
    canvas = tk.Canvas(root)
    canvas.pack(fill="both", expand=True)
    
    def resize_image(event):
        global bg_image
        width = event.width
        height = event.height
        
        resized = original_image.resize((width, height))
        bg_image = ImageTk.PhotoImage(resized)
        
        canvas.delete("all")
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        
        canvas.create_text(
            width // 2,
            height // 6,
            text="Doctor D",
            font=("Comic Sans MS", 40),
            fill="black"
        )
        
        canvas.create_text(
            width // 2,
            height // 3,
            text="DISCLAIMER!\nNot Medically Accurate! \nAlways consult a professional (excluding Doc. D)",
            font=("Comic Sans MS", 12, "bold"),
            fill="red"
        )
        
        start_btn.place(x=width // 2 - 50, y=height // 2)
        exit_btn.place(x=width // 2 - 50, y=height // 2 + 60)
        
    start_btn = tk.Button(root, text="START", bg="lime", command=symptom_screen)
    exit_btn = tk.Button(root, text=" EXIT ", bg="red", command=root.quit)
    
    canvas.bind("<Configure>", resize_image)
    root.update_idletasks()
    canvas.event_generate("<Configure>", width=root.winfo_width(), height=root.winfo_height())
    
#symptom screen (YIPPEEEEEE I'M ALMOST DONE WITH THIS PROJECT oh wait nevermind I still have thousands of illnesses to add OH GOD I DARE IMAGINE THE FILE SIZE)

symptom_vars = {}

def symptom_screen():
    columns = 4
    row = 0
    col = 0
    font_size = 12
    clear()
    tk.Label(root, text="Select Symptoms", bg="tomato", font=("Comic Sans MS", 20)).pack()
    
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)
    
    symptom_vars.clear()
    for s in all_symptoms:
        var = tk.IntVar()
        
        cb = tk.Checkbutton(
            frame,
            text=s.lower(),
            variable=var,
            font=("Comic Sans MS", font_size)
        )
        
        cb.grid(row=row, column=col, sticky="w", padx=5, pady=2)
        
        symptom_vars[s] = var
        
        col += 1
        if col >= columns:
            col = 0
            row += 1
    
    tk.Button(root, text="ENTER", bg="lime", font=("Comic Sans MS", 12), command=results_screen).pack(pady=10)
    tk.Button(root, text=" BACK ", bg="orange", font=("Comic Sans MS", 12), command=title_screen).pack()

#here we can see me start to get sloppy, as I have been doing this for a few hours too many. Excuse me for a minute while I scream at the top of my lungs into a pineapple. Meant to say pillow. Why am I not just changing pineapple into pillow instead of writing this? I don't know. Am I crazy? I'll ask Doctor D.

def find_matches(selected):
    return[
        illness for illness, data in illness_db.items()
        if all(symptom in data["symptoms"] for symptom in selected)
    ]

#fun fact! on the last tk.Button, I accidentally wrote it as gk.button, and it took me over half an hour to find! If there's a god of coding, they sure hate me! I COULD HAVE SWORN I SAW IT BEFORE I SWEAR TO GOD AAAAAAAAAAHHHHHHHHHHH anyways-

#result screen (finally)

def results_screen():
    clear()
    selected = [s for s, v in symptom_vars.items() if v.get() ==1]
    matches = find_matches(selected)
    
    tk.Label(root, text="Possible Illnesses", font=("Comic Sans MS", 16)).pack()
    listbox = tk.Listbox(root, font=("Comic Sans MS", 12))
    listbox.pack(fill="both", expand=True)
    
    for m in matches:
        listbox.insert(tk.END, m.lower())
    
    def show_info(event):
        sel = listbox.curselection()
        if sel:
            name = listbox.get(sel[0]).title()
            info = illness_db[name]
            messagebox.showinfo(name,
                                f"{info['description']}\n\nTreatment:\n{info['treatment']}")
    
    listbox.bind("<<ListboxSelect>>", show_info)
    tk.Button(root, text=" BACK ", bg="orange", font=("Comic Sans MS", 12), command=symptom_screen).pack(pady=5)

#the actual program working as it cannot start without starting. That reminds me of a funny image I saw once. I'll probably put what it said at the end.

title_screen()
root.mainloop()

#alright now that's done, here's that funny thing I mentioned like ten minutes ago:

#               if running == True:
#                   notrunning == False
#
#Can't remember where I saw it but I find it pretty funny haha. 
#Anyways, Hope you enjoyed glaring at the unimportant part of this project, and I will continue adding more and more and more different illnesses! Don't worry though, as I will not include the added illnesses as extra time for devlogs, because it would be cheating to add more and more time by just adding illnesses. Whenever I need to add illnesses, I will just write out the code in a seperate area, where time isn't tracked, and then copy and paste it. After all, there are thousands of illnesses I could add, and it would be unfair if I spent hundreds of hours doing things which do next to nothing. I have morals, ya' know.
#What am I even doing anymore. I'm writing this instead of revising for my GCSEs. But then if I know what I'm doing, why did I ask what I'm doing? Am I just a madman stumbling my way through a cave of code? I wrote this and I still have no idea how it works. My mind is in pieces.
