import maya.cmds as cmds
import maya.OpenMaya as om

# Moves the selected objects to the floor (will not go below the grid)
def drop_to_floor():
    # Creates a list of the selected objects
    selected_objects = cmds.ls(selection=True)

    # If an object is selected
    if selected_objects:
        for object in selected_objects:
            # Gets the coordinates of the bounding box for each object
            bbox = cmds.exactWorldBoundingBox(object)

            # Gets the minimum Y coordinate of the object
            minimum_y = bbox[1]

            # Gets the objects position in world space. Format: (0, 0, 0)
            object_positon = cmds.xform(object, q=True, t=True, ws=True)

            # Calculates the difference between the objects position and its minimum Y
            distance_to_floor = object_positon[1] - minimum_y

            # Sets the objects Y position value to be the distance to floor
            object_positon[1] = distance_to_floor

            # Moves the object to the floor
            cmds.xform(object, translation=object_positon, ws=True)            
    else:
        # Display an error if nothing is selected
        om.MGlobal.displayError('No objects selected')

if __name__ == '__main__':
    drop_to_floor()