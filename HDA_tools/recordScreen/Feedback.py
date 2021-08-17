import hou
import os
from datetime import datetime


def Send_Feedback():

    usr = hou.expandString('$USER')
    text_parm = hou.parm('/obj/recordScreen1/feedlablel')
    input = hou.evalParm('/obj/recordScreen1/feedlablel')
    now = datetime.now()
    date_format = now.strftime('%d/%m/%Y %H:%M')

    
    if (bool(input)) != False:
    
        text_parm.set('')
    
        hou.ui.displayMessage('Thanks for the feedback ' + usr + '!')
    
           
        Feedback_path = '/mnt/resources/pose_library/Feedback/recordScreen/'
    
        file_name = 'Chocolate_Log'
        
        log = str(date_format) + ' || from recordScreen tool - Feedback - | '
    
        file = open(Feedback_path + file_name, 'a+')
        file.write('\n' + log + usr + ' says: ' + input)
        file.close()
        
    else:
        hou.ui.displayMessage('<< The text field is empty tho ... ' + usr + '!')
    
    
  
#############################

def Read_Feedback():

    now = datetime.now()
    date_format = now.strftime('%d/%m/%Y %H:%M')
           
    Feedback_path = '/mnt/resources/pose_library/Feedback/recordScreen/'
    
    file_name = 'Chocolate_Log'
    
    os.system('xdg-open /mnt/resources/pose_library/Feedback/recordScreen/Chocolate_Log')
    
    file = open(Feedback_path + file_name, 'a+')
    file.write('\n' + str(date_format) + ' || ------------------------ Read ')
    file.close()
    
    
