import math
import colored
from colored import stylize

def __padd(s='', width=None):
    if not width:
        width = len(s) + 2
    if s == '':
        width=0
    half_with = math.ceil((width-len(s))/2)
    padd_str = ' '*half_with
    return padd_str + s + padd_str

def __apply_formats(text,styles):
    text = stylize(text,colored.fg(styles[-2]))
    text = stylize(text,colored.bg(styles[-1]))
    for style in styles[:-2]:
            text = stylize(text,colored.attr(style))
    return text

def badge(label='', message='', messagebg='blue',labelbg='dark_gray', messagecolor='white', labelcolor='white',labelwidth=None,messagewidth=None,labelstyles=None,messagestyles=None):
    if not labelstyles:
        labelstyles=[]
    if not messagestyles:
        messagestyles=[]
    labelstyles.extend([labelcolor,labelbg])
    messagestyles.extend([messagecolor,messagebg])
    
    label_formatted = __apply_formats(__padd(str(label),labelwidth),labelstyles)
    message_formatted = __apply_formats(__padd(str(message),messagewidth),messagestyles)
    return label_formatted+message_formatted