#%remove when creating exe


import wmi
import tkinter
import tkinter.filedialog
import os


def show_running_processes():                                                       #show process list
    running_processes = []
    for process in f.Win32_Process():
    
        running_processes.append(process.name)

    running_processes = list(dict.fromkeys(running_processes))      #removing dublicates from list

    # remove previous IntVars
    intvar_dict.clear()

    # remove previous Checkboxes
    for cb in checkbutton_list:
        cb.destroy()
    checkbutton_list.clear() 

    for process_name in running_processes:
        # create IntVar for filename and keep in dictionary
        intvar_dict[process_name] = tkinter.IntVar()

        # create Checkbutton for filename and keep on list
        c = tkinter.Checkbutton(window, text=process_name, variable=intvar_dict[process_name])
        c.pack()
        text.window_create("end", window=c)
        text.insert("end", "\n") 
        checkbutton_list.append(c)

def kill_selected():                                        
    for key, value in intvar_dict.items():
        if value.get() > 0:
            for process in f.Win32_Process():
                if process.name == key:
                    process.Terminate()

def save_txt():
     for key, value in intvar_dict.items():
        if value.get() > 0:
            try: 
                f = open("kill_list.txt")
                word_found = False

                for word in f:
                    if word == key:
                        word_found = True
                        print("word already exists")                #%
                    
                if word_found is False:
                    f = open("kill_list.txt","a")
                    key = "\n"+key
                    f.write(key)
                    print("word appened")                           #%
            except: 
                f =open("kill_list.txt","w")  #creating file if doesnt exist
                f.write(key)
                print("word appened in new file")                   #%

    
def view_kill_list():                           
    # saved_list = open("kill_list.json").read()
    # saved_list = json.loads(saved_list)
    saved_list = []
    try:
        data = open("kill_list.txt")
        for process_name in data:
            saved_list.append(process_name.rstrip())
        
        # remove previous IntVars
        intvar_dict.clear()

        # remove previous Checkboxes
        for cb in checkbutton_list:
            cb.destroy()
        checkbutton_list.clear() 
        
        for process_name in saved_list:
            # create IntVar for filename and keep in dictionary
            intvar_dict[process_name] = tkinter.IntVar()

            # create Checkbutton for filename and keep on list
            c = tkinter.Checkbutton(window, text=process_name, variable=intvar_dict[process_name])
            c.pack()
            text.window_create("end", window=c)
            text.insert("end", "\n") 
            checkbutton_list.append(c)
    except:
        print("No Existing Saved File!")                    #%



def saved_list_kill():                                             
    try:
        fhandle = open("kill_list.txt")
        for item in fhandle:
            item = item.rstrip()
            for process in f.Win32_Process():
                    if process.name == item:
                        process.Terminate()
    except:
        print("No Existing Saved File!")                    #%

# --- main ---
# to keep all IntVars for all filenames
intvar_dict = {}
 # to keep all Checkbuttons for all filenames
checkbutton_list = []
window = tkinter.Tk()
f = wmi.WMI()
sb = tkinter.Scrollbar(orient="vertical")
text = tkinter.Text(window, width=40, height=20, yscrollcommand=sb.set)
sb.config(command=text.yview)
sb.pack(side="right",fill="y")
text.pack(side="top",fill="both",expand=True)

kill_list = []
# lbl = tkinter.Label(window, text="Path")
# lbl.pack()

# ent1 = tkinter.Entry(window)
# ent1.pack()
btn1 = tkinter.Button(window, text="Show Processes", command=show_running_processes)
btn1.pack()
btn1 = tkinter.Button(window, text="Kill Selected Processes", command=kill_selected)
btn1.pack()
btn1 = tkinter.Button(window, text="Save Selected Items To List", command= save_txt)
btn1.pack()
btn1 = tkinter.Button(window, text="View Saved Kill List", command= view_kill_list)
btn1.pack()
btn1 = tkinter.Button(window, text="Kill From Saved List", command= saved_list_kill)
btn1.pack()
window.mainloop()