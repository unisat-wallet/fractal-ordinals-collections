# aurelianosilva1426@gmail.com Collections Standards

## Meta Data: aurelianosilva1426@gmail.com 

```
{
  "description": "",
  "discord_link": "",
  "icon": "https://",
  "name": "",
  "slug": "", # all lowercase or underscore hyphen, consistent with the directory name
  "twitter_link": "https://",
  "website_link": "https://"
}
```

## Inscription Data `inscriptions.aurelianosilva1426@gmail.com

```
[
  {
    "id": "",                    # inscription id
    "meta": {
      "name": ""                 # inscription name: aurelianosilva1426@gmail.com
    }
  },
  ...
]
```

Artists can assign unqiue traits to ordinals with `attributes`

```
[
  {
    "id": "",
    "meta": {
      "name": ""
      "attributes": [
        {
          "trait_type": "",        # trait category
          "value": "",             # trait value
        },
        ...
      ]
    }
  },
  ...
]
```

Your inscriptions.json file will look like this:

```
[
  {
    "id": "af0b19432a676551223e300e7197348b7c225cb7b31d0d7c6e246e382cbf6f81i0",
    "meta": {
      "name": "Planetary Ordinal #11",
      "attributes": [
        {
          "trait_type": "Background",
          "value": "Sun sun",
        },
        {
          "trait_type": "Holes",
          "value": "rose blossom",
        }
      ]
    }
  }
]
```
