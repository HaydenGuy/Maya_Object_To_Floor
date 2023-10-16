import maya.cmds as cmds

def get_selected_items():
    selected_items = cmds.ls(selection=True)

    if selected_items:
        for item in selected_items:
            print(item)
    else:
        print("Nothing selected")

if __name__ == '__main__':
    get_selected_items()