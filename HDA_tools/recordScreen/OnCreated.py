import hou
import os

n = hou.node('/obj/BG_recordScreen1')
n.setDisplayFlag(0)
n.setUserData('nodeshape', 'circle')
n.setColor(hou.Color(0, 1, 0))
n.parm('picking').set(0)

hip_path = hou.expandString('$HIP')
houdini_path = os.path.dirname(hip_path)
img_path = houdini_path + ('/img')

path_evalParm = hou.evalParm('/obj/BG_recordScreen1/path')
node_parm_path = hou.parm('/obj/BG_recordScreen1/path')

Record = hou.parm('/obj/BG_recordScreen1/Record')
name = ('test')
ext = ('_hd_v001_srgb.ogv')

if not os.path.exists(img_path + '/script'):
    os.mkdir(img_path + '/script')

###

set_path = hou.parm('/obj/BG_recordScreen1/Path').set(img_path)

set_Rec_Name = hou.parm('/obj/BG_recordScreen1/Name').set('screen_record')

set_ExtV = hou.parm('/obj/BG_recordScreen1/Extension').set('_hd_v001_srgb.ogv')

input_text = '// to make this work,you need the "recordmydesktop command/module installed on your Linux machine"'

hou.parm('/obj/BG_recordScreen1/important').set(input_text)