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
}
all_symptoms = sorted ({s for i in illness_db.values() for s in i["symptoms"]})

#Logic

def find_matches(selected):
    return[
        illness for illness, data in illness_db.items()
        if all(symptom in data["symptoms"] for symptom in selected)
    ]

#GUI

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Doctor D")
root.geometry("800x600")
root.resizable(True, True)

#Load Image

bg_image = None
try:
    bg_image = tk.PhotoImage(file="Doc Dat.png")
except Exception as e:
    print("Image cannot load, so here's an analogue smiley face instead:  :)", e)

#util

def clear():
    for w in root.winfo_children():
        w.destroy
    
#title screen thingy, ya know?

def title_screen():
    clear()
    canvas = tk.Canvas(root)
    canvas.pack(fill="both", expand=True)
    if bg_image:
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.create_text(400, 100, text="Doctor D",
                       font=("Comic Sans MS", 40), fill="tomato")
#disclaimer
    canvas.create_text(
        400, 180,
        text="DISCLAIMER:\nNot medically accurate.\nAlways consult a professional doctor!",
        font=("Arial", 12, "bold"),
        fill="red"
    )
    tk.Button(root, text="START", bg="lime",
            command=symptom_screen).place(x=350, y=250)
    tk.Button(root, text="EXIT", bg="red",
            command=root.quit).place(x=350, y=320)

#symptom screen (YIPPEEEEEE I'M ALMOST DONE WITH THIS PROJECT oh wait nevermind I still have thousands of illnesses to add OH GOD I DARE IMAGINE THE FILE SIZE)

symptom_vars = {}
def symptom_screen():
    clear()
    tk.Label(root, text="Select Symptoms",
             bg="yellow", font=("Comic Sans MS", 20)).pack()
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)
    symptom_vars.clear()
    for s in all_symptoms:
        var=tk.IntVar()
        tk.CheckButton(frame, text=s, variable=var).pack(anchor="w")
        symptom_vars[s] = var
        #here we can see me start to get sloppy, as I have been doing this for a few hours too many. Excuse me for a minute while I scream at the top of my lungs into a pineapple.
        tk.Button(root, text="ENTER", bg="lime",
                  command=results_screen).pack(pady=10)
        tk.Button(root, text="BACK", bg="orange",
                  command=title_screen).pack()
#fun fact! on the last tk.Button, I accidentally wrote it as gk.button, and it took me over half an hour to find! If there's a god of coding, he sure hates me! I COULD HAVE SWORN I SAW IT BEFORE I SWEAR TO GOD AAAAAAAAAAHHHHHHHHHHH anyways-

#result screen (finally)

def results_screen():
    clear()
    selected = [s for s, v in symptom_vars.items() if v.get() == 1]
    matches = find_matches(selected)
    tk.Label(root, text="Possible illnesses",
             font=("Arial", 16)).pack()
    listbox = tk.Listbox(root)
    listbox.pack(fill="both", expand=True)
    for m in matches:
        listbox.insert(tk.END, m)
    def show_info(event):
        sel = listbox.curselection()
        if sel:
            name = listbox.get(sel[0])
            info = illness_db[name]
            messagebox.showinfo(
                name,
                f"{info['description']}\n\nTreatment:\n{info['treatment']}"
            )
    listbox.bind("<<ListboxSelect>>", show_info)
    tk.Button(root, text="BACK", command=symptom_screen).pack()

#the actual program working as it cannot start without starting. That reminds me of a funny image I saw once. I'll probably put what it said at the end.

title_screen()
root.mainloop()

#alright now that's done, here's that funny thing I mentioned like ten minutes ago:

#               if running == True:
#                   notrunning == False

#Can't remember where I saw it but I find it pretty funny haha. 
#Anyways, Hope you enjoyed glaring at the unimportant part of this project, and I will continue adding more and more and more different illnesses!
