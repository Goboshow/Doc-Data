#GUI

print("Program Started")
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
    "Perforated Eardrum": {"symptoms": ["ear infection", "loud noise", "sudden change in air pressure", "hearing loss", "earache", "bleeding", "dizziness"], "description":"A hole or tear in the eardrum", "treatment":"usually heals within 2 months, however may need antibiotics"},
    "Ehlers-Danlos Syndrome": {"symptoms": ["hypermobility", "stretchy skin", "fragile skin", "joint pain"], "description":"Rare inherited conditions that affect tissues", "treatment":"physiotherapists and occupational therapists can help, however there is no specific cure due to the many different types of EDS there are"},
    "Epilepsy": {"symptoms": ["seizures", "fainting", "becoming limp", "unusual behaviour", "fidgeting", "unawareness"], "description":"A condition that affects the brain and causes seizures", "treatment":"check-ups, talk to your local doctor-dude (not Doc. D) and ask for a care plan"},
    "Eye Cancer": {"symptoms": ["bulging", "blurred vision", "floaters", "loss of vision", "irritation"], "description":"Mutated cells in the tissues of the eyes", "treatment":"Chop out the eye, blast it with radiation, or have a pricey surgery"}
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

#here we can see me start to get sloppy, as I have been doing this for a few hours too many. Excuse me for a minute while I scream at the top of my lungs into a pineapple.

def find_matches(selected):
    return[
        illness for illness, data in illness_db.items()
        if all(symptom in data["symptoms"] for symptom in selected)
    ]

#fun fact! on the last tk.Button, I accidentally wrote it as gk.button, and it took me over half an hour to find! If there's a god of coding, he sure hates me! I COULD HAVE SWORN I SAW IT BEFORE I SWEAR TO GOD AAAAAAAAAAHHHHHHHHHHH anyways-

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

#Can't remember where I saw it but I find it pretty funny haha. 
#Anyways, Hope you enjoyed glaring at the unimportant part of this project, and I will continue adding more and more and more different illnesses!
