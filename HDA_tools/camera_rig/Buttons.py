import hou

def crops(kwargs):
    node = kwargs['node']

    crop_button = node.evalParm('crops')
    Mask_Aspect = node.parm('maskaspect')
    HUD_a = node.parm('t3y')
    grid_line_01 = hou.parm('/obj/' + str(node) + '/grid_lines_02/transform1/ty')
    grid_line_01_scale = hou.parm('/obj/' + str(node) + '/grid_lines_02/transform1/scale')
    grid_line_02 = hou.parm('/obj/' + str(node) + '/grid_lines_02/transform2/ty')
    grid_line_02_scale = hou.parm('/obj/' + str(node) + '/grid_lines_02/transform2/scale')
    HUD_b = hou.parm('/obj/' + str(node) + '/grid_lines_02/transform5/ty')
    
    if crop_button == 1:
        
        Res_eval_x = node.evalParm('resx')
        Res_eval_y = node.evalParm('resy')
        
        if Res_eval_x == 1920 and Res_eval_y == 1080:
        
            scale_y = hou.parm('/obj/' + str(node) + '/grid_lines_02/transform5/sy')
            scale_uni = hou.parm('/obj/' + str(node) + '/grid_lines_02/transform5/scale')
            
            node.parm('s2x').set(0.5)
            node.parm('s2y').set(1)
            node.parm('s2z').set(1)
                  
            Mask_Aspect.set(2.35)
            HUD_a.set(0.86)
            HUD_b.set(0.136)            
            grid_line_01.set(-0.1)
            grid_line_01_scale.set(1)
            grid_line_02.set(-0.1)
            grid_line_02_scale.set(1)
            scale_y.set(1)
            scale_uni.set(0.0166)            
            
        elif Res_eval_x == 1080 and Res_eval_y == 1920:
        
            scale_y = hou.parm('/obj/' + str(node) + '/grid_lines_02/transform5/sy')
            scale_uni = hou.parm('/obj/' + str(node) + '/grid_lines_02/transform5/scale')
            
            node.parm('s2x').set(0.9)
            node.parm('s2y').set(0.9)
            node.parm('s2z').set(1.4)
            
            Mask_Aspect.set(0.563)
            HUD_a.set(0.985)
            HUD_b.set(0.013)            
            grid_line_01.set(-0.1)
            grid_line_01_scale.set(1)
            grid_line_02.set(-0.1)
            grid_line_02_scale.set(1)  
            scale_y.set(0.43)
            scale_uni.set(0.0236)

            
        elif Res_eval_x == 1280 and Res_eval_y == 720:  
            print('need to set this up')
            
        elif Res_eval_x == 1920 and Res_eval_y == 820:  
            hou.ui.displayMessage('use the crops feature for 1920x1080 to achieve the same look as 1920x820')
            
        else:
            hou.ui.displayMessage('cant evaluate this resolution: ' + str(Res_eval_x) + 'x' + str(Res_eval_y) )
    
        
        
    else:
        Mask_Aspect.set(1.78)
        HUD_a.set(0.98)
        grid_line_01.set(-0.2936)
        grid_line_01_scale.set(1.3252)
        grid_line_02.set(-0.2936)
        grid_line_02_scale.set(1.3252)
        HUD_b.set(0.015)
        
def gridlines(kwargs):

    node = kwargs['node']

    gridline_button = node.evalParm('gridlines')
    hide_by_scale  = hou.parm('/obj/' + str(node) + '/grid_lines_02/transform7/scale')
    
    if gridline_button == 1:
        hide_by_scale.set(0)
    else:
        hide_by_scale.set(1)
        
def camera_notes(kwargs):

    node = kwargs['node']
    
    HUD_text = hou.parm('/obj/' + str(node) + '/artist_input_text/font1/text')
    camera_notes_button = node.evalParm('camera_notes')
    
    if camera_notes_button == 1:
        hou.node('/obj/' + str(node) + '/artist_input_text1/python1').setDisplayFlag(1)
    else:       
        hou.node('/obj/' + str(node) + '/artist_input_text1/process_off').setDisplayFlag(1)
        HUD_text.set('')
        
        
    
    
   
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        