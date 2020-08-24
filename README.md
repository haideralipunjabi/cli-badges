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
### Other Projects
* [cli-badges - NodeJS](https://github.com/nombrekeff/cli-badges)

---

Contributions are very welcomed 🥰