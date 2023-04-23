import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_btn = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='items', 
                 enable_events=True, size=[45,10])
edit_btn = sg.Button("Edit")

window = sg.Window('MY To-Do App', 
                   layout=[[label],[input_box, add_btn],[list_box,edit_btn]], 
                   font=('Helvetica', 15)
                   )

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['items'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['items'].update(values=todos)

        case "Edit":
            todo_edit = values['items'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['items'].update(values=todos)


        case "items":
            window["todo"].update(value=values['items'][0])
        case sg.WIN_CLOSED:
            break


window.close()

