# URL Download

```py
import urldl


url = "https://github.com/FayasNoushad.png"
name = "profile.png"

urldl.download(url, name)
# For download image of url in name directory

urldl.download(url)
# Same of the above without name ( not recommended )
# Note :- This type not supported in some links
```

## Installation

```
pip install urldl
```

## Features

- Download content of url
- Manual and automatic file name
