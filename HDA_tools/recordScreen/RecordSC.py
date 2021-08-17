import hou
import os
import subprocess
from time import sleep

obj = ('/obj')

n = hou.node('/obj/recordScreen1')
hip_path = hou.expandString('$HIP')
houdini_path = os.path.dirname(hip_path)
img_path = houdini_path + ('/img') 

def open_path():

    open_path = hou.evalParm('/obj/recordScreen1/path')
    os.system('xdg-open ' + open_path)
       
def plus():

    Record = hou.parm('/obj/recordScreen1/Record')
    name = hou.evalParm('/obj/recordScreen1/Name')
    ext = hou.evalParm('/obj/recordScreen1/Extension')

    eval_ext = hou.evalParm('/obj/recordScreen1/Extension')

    ext_length = len(eval_ext)
    
    lens = eval_ext[5:]
    len2 = lens[:3]
    
    num =  int(len2)
    add = ('{:03d}'.format(num + 1))
    
    hou.parm('/obj/recordScreen1/Extension').set('_hd_v' + add + '_srgb.ogv')
    
def minus():

    Record = hou.parm('/obj/recordScreen1/Record')
    name = hou.evalParm('/obj/recordScreen1/Name')
    ext = hou.evalParm('/obj/recordScreen1/Extension')

    eval_ext = hou.evalParm('/obj/recordScreen1/Extension')

    ext_length = len(eval_ext)
    
    lens = eval_ext[5:]
    len2 = lens[:3]
    
    num =  int(len2)
    subtract = ('{:03d}'.format(num - 1))
    
    hou.parm('/obj/recordScreen1/Extension').set('_hd_v' + subtract + '_srgb.ogv')

    

def reset_paths():

    Record = hou.parm('/obj/recordScreen1/Record')
    name = hou.evalParm('/obj/recordScreen1/Name')
    ext = hou.evalParm('/obj/recordScreen1/Extension')

    hou.parm('/obj/recordScreen1/path').set(img_path)

    hou.parm('/obj/recordScreen1/Name').set('screen_record')

    hou.parm('/obj/recordScreen1/Extension').set('_hd_v001_srgb.ogv')

    
    
def add_directory():

    path_evalParm = hou.evalParm('/obj/recordScreen1/path')
            
    os.mkdir(path_evalParm)
    
def Set_path():

    path_evalParm = hou.evalParm('/obj/recordScreen1/path')    
    
    name = hou.evalParm('/obj/recordScreen1/Name')
    ext = hou.evalParm('/obj/recordScreen1/Extension')

    file_name = 'record_start.py'
    path = (path_evalParm + '/script/')
    
    text = ('import os \nos.system("recordmydesktop -x 1920 --width 1920 --height 1080 --no-sound -o ' + path_evalParm + '/' +  name + ext + '")')
    test = ("import os \nprint('hello')")
    
    file = open(path + file_name, 'w')
    file.write(text)
    
    
def Record():

    path = hou.evalParm('/obj/recordScreen1/path')

    n = hou.node('/obj/recordScreen1')
    n.setColor(hou.Color(1, 0, 0))
    n.setUserData('nodeshape', 'circle')

    
    Set_path_button = hou.parm('/obj/recordScreen1/Set_path')
    Set_path_button.pressButton()

    os.system('xdg-open ' + path + '/script/record_start.py')
        
    
def Stop():

    n = hou.node('/obj/recordScreen1')
    usr = hou.expandString('$USER')
    
    n.setUserData('nodeshape', 'circle')
    n.setColor(hou.Color(0, 1, 0))
       
    cmd = "kill -15 `ps aux | grep recordmydes[k]top |awk '{print $2}'`"
    
    subprocess.Popen(cmd, shell=True)  
    
def Dailies():

    hou.parm('/obj/recordScreen1/Refresh').pressButton()

    os.system('dailies')
    
def Refresh():

    Record = hou.parm('/obj/recordScreen1/Record')
    name = hou.evalParm('/obj/recordScreen1/Name')
    ext = hou.evalParm('/obj/recordScreen1/Extension')

    path_evalParm = hou.evalParm('/obj/recordScreen1/path')

    size_parm = hou.parm('/obj/recordScreen1/size')
    size_eval = hou.evalParm('/obj/recordScreen1/size')
    

    try:
    
        File_path = os.path.getsize(path_evalParm + '/' +  name + ext )    
        convert = float(File_path)/ 1024 / 1024    
        format = '{:.3f}'.format(convert)    
        size_parm.set(str(format) + ' MIB')
    
        ##    

        eval_ext = hou.evalParm('/obj/recordScreen1/Extension')
        ext_length = len(eval_ext)
        
        lens = eval_ext[5:]
        len2 = lens[:3]
        
        num =  int(len2)
        format_v_num = ('{:03d}'.format(num))
        
        hou.parm('/obj/recordScreen1/version').set('v' + str(format_v_num))
        

    except OSError as e:
    
        size_parm.set('// no file/directory created yet')
        hou.parm('/obj/recordScreen1/version').set('// no file/directory created yet')       
        
        
                    
def Play():

    

    path_evalParm = hou.evalParm('/obj/recordScreen1/path')
    node_parm_path = hou.parm('/obj/BG_screenRecorder1/path')
    
    Record = hou.parm('/obj/recordScreen1/Record')
    name = hou.evalParm('/obj/recordScreen1/Name')
    ext = hou.evalParm('/obj/recordScreen1/Extension')
    
    
    os.system('xdg-open ' + path_evalParm + '/' + name + ext)
    
    

def dev():
    print ('test')
    
    
    
    
    




    
    

    

    

    
    
    
    
    

    
    
