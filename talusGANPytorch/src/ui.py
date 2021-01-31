import PySimpleGUI as sg
import os.path

from PySimpleGUI.PySimpleGUI import Button
import voxelize

import numpy as np


'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles


file_list_column = [
    [
        sg.Text("Source directory"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
        sg.Button('Run', disabled=True),
        sg.Checkbox('Plot', default=True, key="-PLOT-"),
        sg.Checkbox('Save file', default=True, key="-SAVE-"),
    ],
    [
        sg.Text("Output directory"),
        sg.In(size=(25, 1), enable_events=True, key="-OUT_FOLDER-"),
        sg.FolderBrowse(),
        sg.Text("Bone"), sg.Input(key="-BONE-", default_text="talus")
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(80, 20), key="-FILE LIST-"
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
            file_list = getListOfFiles(folder) # os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((values["-BONE-"] + ".stl"))
        ]

        fnames.append("All")

        window["-FILE LIST-"].update(fnames)
        if (len(fnames) > 0):
            window.Element("Run").Update(disabled = False)
        else:
            window.Element("Run").Update(disabled = True)
    elif event == "Run":
        if (len(values["-FILE LIST-"]) == 0 or values["-FILE LIST-"][0] == "All"):
            for file in fnames:
                if (file == "All"):
                    continue
                filename = file
                print("Processing " + filename)
                vox = voxelize.voxelize(file_path=filename, resolution=30)
                print("Finished processing " + filename)

                if (values["-PLOT-"] == True):
                    voxelize.Ploat_Voxels(vox)

                if (values["-SAVE-"] == True):
                    outdir = ""
                    if (values["-OUT_FOLDER-"] == ""):
                        outdir = filename.split(".stl")[0]
                    else:
                        outdir = values["-OUT_FOLDER-"] + "/" + filename.split(".stl")[0].split("/")[-2] + "_" + filename.split(".stl")[0].split("/")[-1]

                    np.save(outdir, vox)
                    print("File saved to " + outdir)
        else:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            print("Processing " + filename)
            vox = voxelize.voxelize(file_path=filename, resolution=30)
            print("Finished processing " + filename)

            if (values["-PLOT-"] == True):
                voxelize.Ploat_Voxels(vox)

            if (values["-SAVE-"] == True):
                outdir = ""
                if (values["-OUT_FOLDER-"] == ""):
                    outdir = filename.split(".stl")[0]
                else:
                    outdir = values["-OUT_FOLDER-"] + "/" + filename.split(".stl")[0].split("/")[-2] + "_" + filename.split(".stl")[0].split("/")[-1]

                np.save(outdir, vox)
                print("File saved to " + outdir)
    
    #elif event == "-FILE LIST-":  # A file was chosen from the listbox

window.close()