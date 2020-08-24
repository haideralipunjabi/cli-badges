<div align="center">
  
  ![](https://vectr.com/kerff/ddbmvyZmm.svg?width=600&height=300&select=aNbKxciPh)
  
  Quirky little python library for generating badges for your cli apps.
  
  ![GitHub file size in bytes](https://img.shields.io/github/size/haideralipunjabi/cli-badges/cli_badges/cli_badges.py?style=flat-square)
  
</div>

---

## Getting Started

### Installing

As usual, you need to install from npm/yarn:

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

![](./output-example.png)

You can also only show the label:

```python
from cli_badges import badge

onlyLabel = badge('❤️ donate', '')
print(onlyLabel)
```

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

### Other Projects
* [cli-badges - NodeJS](https://github.com/nombrekeff/cli-badges)

---

Contributions are very welcomed 🥰