import hou
import os
from datetime import datetime





#get path from shot, if home dir then it will give an error and run the below code instead
try:

    n = hou.node('/obj/recordScreen1')
    n.setDisplayFlag(0)
    n.setUserData('nodeshape', 'circle')
    n.setColor(hou.Color(0, 1, 0))
    n.parm('picking').set(0)
    
    
    hip_path = hou.expandString('$HIP')
    houdini_path = os.path.dirname(hip_path)
    img_path = houdini_path + ('/img') 
    
    path_evalParm = hou.evalParm('/obj/recordScreen1/path')
    node_parm_path = hou.parm('/obj/recordScreen1/path')
    
    Record = hou.parm('/obj/recordScreen1/Record')
    name = ('test')
    ext = ('_hd_v001_srgb.ogv')
    
    
    if not os.path.exists(img_path + '/script'):
        os.mkdir(img_path + '/script')
    
    ####
    
    set_path = hou.parm('/obj/recordScreen1/path').set(img_path)
    set_Rec_Name = hou.parm('/obj/recordScreen1/Name').set('screen_record')
    set_ExtV = hou.parm('/obj/recordScreen1/Extension').set('_hd_v001_srgb.ogv')
    
    input_text = '// to make this tool work, you need 2 things:\n\n-----------------------------------------------\n\n- you need the "recordmydesktop" command/module to be installed on your machine - ask @IT to install\n\n- make sure your .py files on your computer opens by default with PYTHON and not Kwrite etc, otherwise it wont execute:\n\n  iv tried multiple ways of running the recordmydesktop inside a Houdini session but they all end up running on the\n  same houdini session process, which means Houdini will freeze until the process has ended,\n  in this case it will never end because there is no way to stop it,\n  so instead i made the tool write out an external .py file (houdini/hip/img/script/record_start.py) that gets executed\n  as an outside process from houdini .. \n\n-----------------------------------------------\n- current issues: \n  * tool does not work in the home directory, - i need to update this'
       
    hou.parm('/obj/recordScreen1/important').set(input_text)
    
    
    ###################
    
    usr = hou.expandString('$USER')
    pc = hou.expandString('$HOSTNAME')
    now = datetime.now()
    date_format = now.strftime('%d/%m/%Y %H:%M')
           
    Feedback_path = '/mnt/resources/pose_library/Feedback/recordScreen/'
    file_name = 'Chocolate_Log'
    
    log = str(date_format) + ' || from recordScreen tool - Created  - | user = '
    
    file = open(Feedback_path + file_name, 'a+')
    file.write('\n' + log + usr)
    file.close()
    
    
    if usr == 'louis':
    
        hou.parm('/obj/recordScreen1/access').set(1)
        
    else:
    
        hou.parm('/obj/recordScreen1/access').set(0)
        

        
#when error occures from home dir, it will then run this code instead        
except OSError as e:

    #hou.ui.displayMessage('because this is home directory, some things might not work')

    
    n = hou.node('/obj/recordScreen1')
    n.setDisplayFlag(0)
    n.setUserData('nodeshape', 'circle')
    n.setColor(hou.Color(0, 1, 0))
    n.parm('picking').set(0)
    
    
    hip_path = hou.expandString('$USR')
    houdini_path = os.path.dirname(hip_path)
    img_path = houdini_path 
    
    path_evalParm = hou.evalParm('/obj/recordScreen1/path')
    node_parm_path = hou.parm('/obj/recordScreen1/path')
    
    Record = hou.parm('/obj/recordScreen1/Record')
    name = ('test')
    ext = ('_hd_v001_srgb.ogv')
    
    
    if not os.path.exists(img_path + '/script'):
        os.mkdir(img_path + '/script')
    
    ####
    
    set_path = hou.parm('/obj/recordScreen1/path').set(img_path)
    set_Rec_Name = hou.parm('/obj/recordScreen1/Name').set('screen_record')
    set_ExtV = hou.parm('/obj/recordScreen1/Extension').set('_hd_v001_srgb.ogv')
    
    input_text = '// to make this tool work, you need 2 things:\n\n-----------------------------------------------\n\n- you need the "recordmydesktop" command/module to be installed on your machine - ask @IT to install\n\n- make sure your .py files on your computer opens by default with PYTHON and not Kwrite etc, otherwise it wont execute:\n\n  iv tried multiple ways of running the recordmydesktop inside a Houdini session but they all end up running on the\n  same houdini session process, which means Houdini will freeze until the process has ended,\n  in this case it will never end because there is no way to stop it,\n  so instead i made the tool write out an external .py file (houdini/hip/img/script/record_start.py) that gets executed\n  as an outside process from houdini .. \n\n-----------------------------------------------\n- current issues: \n  * tool does not work in the home directory, - i need to update this'
       
    hou.parm('/obj/recordScreen1/important').set(input_text)
    
    
    ###################
    
    usr = hou.expandString('$USER')
    pc = hou.expandString('$HOSTNAME')
    now = datetime.now()
    date_format = now.strftime('%d/%m/%Y %H:%M')
           
    Feedback_path = '/mnt/resources/pose_library/Feedback/recordScreen/'
    file_name = 'Chocolate_Log'
    
    log = str(date_format) + ' || from recordScreen tool - Created  - | user = '
    
    file = open(Feedback_path + file_name, 'a+')
    file.write('\n' + log + usr)
    file.close()
    
    
    if usr == 'louis':
    
        hou.parm('/obj/recordScreen1/access').set(1)
        
    else:
    
        hou.parm('/obj/recordScreen1/access').set(0)





