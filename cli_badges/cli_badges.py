import math
import colored
from colored import stylize
from types import SimpleNamespace
import json
from copy import deepcopy
__THEMES = {
    'red': {
        'messagebg': 'red'
    },
    'green': {
        'messagebg': 'green'
    },
    'yellow': {
        'messagebg': 'yellow',
        'messagecolor': 'black',
    },
    'cyan': {
        'messagebg': 'cyan',
        'messagecolor': 'black',
    },
    'magenta': {
        'messagebg': 'magenta',
        'messagecolor': 'black',
    },
    'success': {
        'message': 'Success',
        'messagebg': 'green'
    },
    'failed': {
        'message': 'Failed',
        'messagebg': 'red'
    }
}

THEME = SimpleNamespace(**__THEMES)


def __padd(s='', width=None):
    if not width:
        width = len(s) + 2
    if s == '':
        width = 0
    half_with = math.ceil((width-len(s))/2)
    padd_str = ' '*half_with
    return padd_str + s + padd_str


def __apply_formats(text, styles):
    text = stylize(text, colored.fg(styles[-2]))
    text = stylize(text, colored.bg(styles[-1]))
    for style in styles[:-2]:
        text = stylize(text, colored.attr(style))
    return text


def __link(text, url):
    return "\u001B]8;;{}\u0007{}\u001B]8;;\u0007".format(url, text)


def badge(label='', message='', messagebg='blue', labelbg='dark_gray', messagecolor='white', labelcolor='white', labelwidth=None, messagewidth=None, labelstyles=None, messagestyles=None, labellink='', messagelink='', swap=False,theme=None):
    if type(theme) == dict:
        args = locals()
        options = deepcopy(theme)
        for k,v in args.items():
            if k not in options.keys() and k!='theme':
                options[k] = v
        return badge(**options)
    if not labelstyles:
        labelstyles = []
    if not messagestyles:
        messagestyles = []
    labelstyles.extend([labelcolor, labelbg])
    messagestyles.extend([messagecolor, messagebg])
    if labellink:
        label = __link(label, labellink)
    if messagelink:
        message = __link(message, messagelink)
    label_formatted = __apply_formats(
        __padd(str(label), labelwidth), (labelstyles if not swap else messagestyles))
    message_formatted = __apply_formats(
        __padd(str(message), messagewidth), (messagestyles if not swap else labelstyles))
    return label_formatted+message_formatted

def add_theme(name,config):
    global __THEMES
    global THEME
    __THEMES[name] = config
    THEME.__setattr__(name,config)

def load_themes(fp):
    themes = json.load(fp)
    for k,v in themes.items():
        add_theme(k,v)