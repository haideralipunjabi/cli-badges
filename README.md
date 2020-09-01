<div align="center">
  
  ![](https://vectr.com/kerff/ddbmvyZmm.svg?width=600&height=300&select=aNbKxciPh)
  
  Quirky little python library for generating badges for your cli apps.
  
  ![GitHub file size in bytes](https://img.shields.io/github/size/haideralipunjabi/cli-badges/cli_badges/cli_badges.py?style=flat-square)
  [![PyPI version](https://badge.fury.io/py/cli-badges.svg)](https://badge.fury.io/py/cli-badges)
</div>

---

**Inspired & Python Port of *[cli-badges - nombrekeff](https://github.com/nombrekeff/cli-badges)***

## Getting Started

### Installing

As usual, you need to install from PIP:

```
$ pip install cli-badges
```

### Usage

This is a simple example, using badges to display test results:

```python
from cli_badges import badge

failedBadge = badge("failed",'2',messagebg='red')
skippedBadge = badge('skipped', '1', messagebg='yellow',messagecolor='black')
successBadge = badge('success','8', messagebg='green',messagecolor='black')


print(failedBadge, successBadge, skippedBadge)
```

The above would output something similar to the terminal:

![output-example](https://raw.githubusercontent.com/haideralipunjabi/cli-badges/master/basic-output-example.png)

You could also create a donate badge with a link ([if supported](#links)):

```python
from cli_badges import badge

donateBadge = badge('❤️ donate', 'ko-fi', messagelink='https://ko-fi.com/logginjs');
print(donateBadge)
```

![donate-output-example.png](https://raw.githubusercontent.com/haideralipunjabi/cli-badges/master/donate-output-example.png)

You can also only show the label:

```python
from cli_badges import badge

onlyLabel = badge('❤️ donate', '')
print(onlyLabel)
```
![onlylabel-output-example](https://raw.githubusercontent.com/haideralipunjabi/cli-badges/master/onlylabel-output-example.png)

> Example output is a mock, console output will vary slightly from terminal to terminal.

## Badge Structure

A badge is conformed of a label and a message `<label>:<message>`. Each segment can be customized, by changing bg color, text color and style.

## Available Options

| Option | Value | Default |
|   ---  |  ---  |   ---   |
| label  | String | `''`     |
| message| String | `''`     |
| messagebg | Color | blue |
| labelbg | Color | dark_gray |
| messagecolor | Color | white |
| labelcolor | Color | white |
| labelwidth | Integer | label length + 2|
| messagewidth | Integer | label length + 2|
| labelstyles | Array of Styles | `[]` |
| messagestyles | Array of Styles | `[]`|
| labellink | URL | `''` |
| messagelink | URL | `''`|
| invert | boolean | False |
| theme | Theme | None |

### Colors

`cli-badges` uses [`colored`](https://pypi.org/project/colored/) internally for managing colors, you can check the list of available colors there.

### Styles
`cli-badges` uses [`colored`](https://pypi.org/project/colored/) internally for managing styles, you can check the list of available styles there.

#### Available Styles

* bold
* dim
* underlined
* reverse
* hidden

### Links

You can output badges with a link attached to it, that can be clicked in some terminals. `labellink` option will add the link to the label, while `messagelink` option will add the link to the message.

> #### ⚠︎ cli-badges will only output link if its supported by your terminal.

> See [this](https://gist.github.com/egmontkob/eb114294efbcd5adb1944c9f3cb5feda) for information on supported terminals

```python
badge('with', 'link',  labellink='https://link.com', messagelink='https://link2.com');
```
![withlink-output-example](https://raw.githubusercontent.com/haideralipunjabi/cli-badges/master/withlink-output-example.png)


### Themes

![theme-image](https://raw.githubusercontent.com/haideralipunjabi/cli-badges/master/themes.png)

Themes are a way to store badge configuration for repeated use. All the options (except for the theme option, obviously) that are needed by the badge can be stored by making a theme.  
The library comes with a set of inbuilt themes, but you can also define your own

#### Inbuilt Themes

* **red** : Red Message Background
* **green** : Green Message Background
* **yellow** : Black Colored Message on Yellow Background
* **cyan** : Black Colored Message on Cyan Background
* **magenta** : Black Colored Message on Magenta Background
* **success** : 'Success' Message on Green Background
* **failed** : 'Failed' Message on Red Background

#### Using Themes

`THEME` stores all the available themes, and has to be passed to the `badge()` functions `theme` argument. Arguments present in the theme will override the passed arguments. Missing arguments will have default values

```python
from cli_badges import badge,THEME
red_badge = badge('Red','Badge',theme=THEME.red)
print(red_badge)
```

#### Adding New Themes

1. Directly in Code  
To add a Theme directly, `add_theme(name,config)` function is used. `name` is the name of the theme, `config` is a `dict` containing the required options

    ```python
    from cli_badges import badge,add_theme, THEME
    add_theme('donate',{
        'label': '❤️ donate'
    })
    donate_badge = badge(message='kofi',theme=THEME.donate)
    print(donate_badge)
    ```
  
2. From a JSON File  
You can store the Theme configurations in a `json` file and load them using `load_themes(file)` function where `file` is the Theme `json` file

    ```json
    # themes.json
    {
        "redblue": {
            "messagebg": "blue",
            "labelbg":"red",
            "messagestyles": ["bold"]
        }
    }
    ```

    ```python
    from cli_badges import badge, load_themes, THEME
    load_themes(open("themes.json","r"))
    redblue_badge = badge('RED','BLUE',theme=THEME.redblue)
    print(redblue_badge)
    ```

### Inverting Styles

The `invert` option is used to apply the message styles to the label and vice-versa

```python
from cli_badges import badge
normal_badge = badge('RED','BLUE',labelbg='red', messagebg='blue')
inverted_badge = badge('RED','BLUE',labelbg='red', messagebg='blue',invert=True)
print(normal_badge,inverted_badge)
```
![invert-example](https://raw.githubusercontent.com/haideralipunjabi/cli-badges/master/invert-example.png)

### Other Libraries?

cli-badges is also available in other languages:

- `Node` [@nombrekeff/cli-badges](https://github.com/nombrekeff/cli-badges)
- `Deno` [@Delta456/cli_badges](https://github.com/Delta456/cli_badges)
---

Contributions are very welcomed 🥰