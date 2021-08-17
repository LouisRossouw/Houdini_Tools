import hou

def crane_rig(kwargs):
    node = kwargs['node']

    button = node.evalParm('crane_rig')
    custom = node.parm('nulls')
    null_master = hou.node('/obj/' + str(node) + '/cam_rig_02')
    z = hou.node('/obj/' + str(node) + '/z1')
    
    
    if button == 1:
    
        custom.set(0)
        null_master.setFirstInput(z)
        
        #cranerig
        hou.node('/obj/' + str(node) + '/subnet1').setDisplayFlag(1)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_004').setDisplayFlag(1)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_003').setDisplayFlag(1)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_011').setDisplayFlag(1)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_005').setDisplayFlag(1)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo').setDisplayFlag(1)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_006').setDisplayFlag(1)
        
        
        #custom_nulls
        
        try:
            hou.node('/obj/cam_SRT').destroy()
            hou.node('/obj/cam_rot_Y').destroy()
            hou.node('/obj/cam_tran_Z').destroy()
            hou.node('/obj/cam_tran').destroy()
            hou.node('/obj/cam_rot').destroy()
            hou.node('/obj/cam_noise').destroy()
        
        except AttributeError:
            pass        
        
        
        
        
    else:
        hou.node('/obj/' + str(node) + '/subnet1').setDisplayFlag(0)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_004').setDisplayFlag(0)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_003').setDisplayFlag(0)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_011').setDisplayFlag(0)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_005').setDisplayFlag(0)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo').setDisplayFlag(0)
        hou.node('/obj/' + str(node) + '/geo_cam_a_geo_006').setDisplayFlag(0)
        null_master.setFirstInput(None)