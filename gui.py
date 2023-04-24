import functions
import PySimpleGUI as sg
import time
import os 

sg.theme("Black")

if not os.path.exists("todos_items.txt"):
    with open("todos_items.txt", "w") as file:
        pass

clock_label = sg.Text("", key="clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_btn = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='items', 
                 enable_events=True, size=[45,10])
edit_btn = sg.Button("Edit")
delete_btn = sg.Button("Delete")
exit_btn = sg.Button("Exit")


window = sg.Window('MY To-Do App', 
                   layout=[[clock_label], 
                           [label], 
                           [input_box, add_btn], 
                           [list_box,edit_btn,delete_btn], 
                           [exit_btn]], 
                   font=('Helvetica', 15)
                   )

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['items'].update(values=todos)

        case "Edit":

            try:        
                todo_edit = values['items'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['items'].update(values=todos)
            except IndexError:
                sg.popup("Please select an items first.", font=("Helvetica", 20))
        
        case "Delete":

            try:
                delete_item = values['items'][0]
                todos = functions.get_todos()
                todos.remove(delete_item)
                functions.write_todos(todos)
                window['items'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an items first.", font=("Helvetica", 20))
                
        case "Exit":
            break

        case "items":
            window["todo"].update(value=values['items'][0])
        case sg.WIN_CLOSED:
            break


window.close()

