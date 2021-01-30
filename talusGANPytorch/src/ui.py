import PySimpleGUI as sg
import os.path

from PySimpleGUI.PySimpleGUI import Button
import voxelize

import numpy as np

file_list_column = [
    [
        sg.Text("3D Talus tools"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
        sg.Button('Run', disabled=True),
        sg.Checkbox('Plot', default=True, key="-PLOT-"),
        sg.Checkbox('Save file', default=True, key="-SAVE-"),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

console_output = [
    [sg.Text("Choose a stl file from the list on the left:")],
    [sg.Output(size=(60,15))],
]

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(console_output),
    ]
]

window = sg.Window("3D Talus", layout)

# Run the Event Loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    # Folder name was filled in, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".stl"))
        ]
        window["-FILE LIST-"].update(fnames)
        if (len(fnames) > 0):
            window.Element("Run").Update(disabled = False)
        else:
            window.Element("Run").Update(disabled = True)
    elif event == "Run":
        filename = os.path.join(
            values["-FOLDER-"], values["-FILE LIST-"][0]
        )
        print("Processing " + filename)
        vox = voxelize.voxelize(file_path=filename, resolution=30)
        print("Finished processing " + filename)

        if (values["-PLOT-"] == True):
            voxelize.Ploat_Voxels(vox)

        if (values["-SAVE-"] == True):
            np.save(filename.split(".stl")[0], vox)
            print("File saved to " + filename.split(".stl")[0] + ".npy")
    
    #elif event == "-FILE LIST-":  # A file was chosen from the listbox

window.close()