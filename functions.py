FILEPATH = "todos_items.txt"

def get_todos(filepath=FILEPATH):

    # (this is dotstring = define the document of function)
    """ Read a text file and return the listof      
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):

    # (this is dotstring = define the document of function)
    """ Write the to-do items list in the text file."""

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
