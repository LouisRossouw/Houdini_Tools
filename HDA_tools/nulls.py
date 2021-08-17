import hou
import os

def nulls(kwargs):
    node = kwargs['node']

    
    crane_rig = node.parm('crane_rig')
    button = node.evalParm('nulls')
    
    if button == 1:
    
        crane_rig.set(0)
        custom = hou.node('/obj/' + str(node) + '/custom')
        null_master = hou.node('/obj/' + str(node) + '/cam_rig_02').setFirstInput(custom)

        obj = hou.node('/obj')
        cam_nullShape = 'chevron_down' 
        camera = node
        camera.move((0, -1))
        
        #cam_SRT
        SRT = obj.createNode('null', 'cam_SRT')
        
        SRT.setDisplayFlag(0)
        SRT.parm('picking').set(0)
        SRT.setUserData('nodeshape', cam_nullShape)
        SRT.setColor(hou.Color(1, 1, 1))     
        SRT.setFirstInput(camera)
        SRT.moveToGoodPosition(relative_to_inputs=True, move_inputs=True, move_outputs=False, move_unconnected=False)
        SRT.setFirstInput(None)
        SRT.move((0, 2))
        
        #cam_rot_Y
        Y = obj.createNode('null', 'cam_rot_Y')
        
        Y.setDisplayFlag(0)
        Y.parm('picking').set(0)
        Y.setUserData('nodeshape', cam_nullShape)
        Y.setColor(hou.Color(0.839, 0.839, 0.839))
        Y.setFirstInput(SRT)
        Y.moveToGoodPosition(relative_to_inputs=True, move_inputs=True, move_outputs=False, move_unconnected=False)
        
        #cam_tran_z
        Z = obj.createNode('null', 'cam_tran_Z')
        
        Z.setDisplayFlag(0)
        Z.parm('picking').set(0)
        Z.setUserData('nodeshape', cam_nullShape)
        Z.setColor(hou.Color(0.6, 0.6, 0.6))
        Z.setFirstInput(Y)
        Z.moveToGoodPosition(relative_to_inputs=True, move_inputs=True, move_outputs=False, move_unconnected=False)
        
        #cam_trans_XYZ
        TR = obj.createNode('null', 'cam_tran')
        
        TR.setDisplayFlag(0)
        TR.parm('picking').set(0)
        TR.setUserData('nodeshape', cam_nullShape)
        TR.setColor(hou.Color(0.478, 0.478, 0.478))
        TR.setFirstInput(Z)
        TR.moveToGoodPosition(relative_to_inputs=True, move_inputs=True, move_outputs=False, move_unconnected=False)
        
        #cam_rot_XYZ
        R = obj.createNode('null', 'cam_rot')
        
        R.setDisplayFlag(0)
        R.parm('picking').set(0)
        R.setUserData('nodeshape', cam_nullShape)
        R.setColor(hou.Color(0.306, 0.306, 0.306))
        R.setFirstInput(TR)
        R.moveToGoodPosition(relative_to_inputs=True, move_inputs=True, move_outputs=False, move_unconnected=False)
        
        #cam_noise
        NS = obj.createNode('null', 'cam_noise')
        
        NS.setDisplayFlag(0)
        NS.parm('picking').set(0)
        NS.setUserData('nodeshape', cam_nullShape)
        NS.setColor(hou.Color(0, 0, 0))
        NS.setFirstInput(R)
        NS.moveToGoodPosition(relative_to_inputs=True, move_inputs=True, move_outputs=False, move_unconnected=False)
        
            
        camera = node
        camera.setFirstInput(NS)
        #camera.moveToGoodPosition(relative_to_inputs=True, move_inputs=True, move_outputs=False, move_unconnected=False)
        
        #cranerig
        hou.node('/obj/' + str(node) + '/subnet1').setDisplayFlag(0)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_004').setDisplayFlag(0)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_003').setDisplayFlag(0)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_011').setDisplayFlag(0)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_005').setDisplayFlag(0)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo').setDisplayFlag(0)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_006').setDisplayFlag(0)
        

        
    else:
        try:
            hou.node('/obj/cam_SRT').destroy()
            hou.node('/obj/cam_rot_Y').destroy()
            hou.node('/obj/cam_tran_Z').destroy()
            hou.node('/obj/cam_tran').destroy()
            hou.node('/obj/cam_rot').destroy()
            hou.node('/obj/cam_noise').destroy()
            
        except AttributeError:
            pass
        
        
        
        
        