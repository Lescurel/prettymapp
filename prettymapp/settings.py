LANDCOVER_CLASSES = {
    "nature":{"natural":["wetland","bare_rock","heath","scrub","shrub"]},
    "urban": {
        "building": True,
        "landuse": ["construction", "commercial"],
        "place":["village","hamlet","town"],
    },
    "water": {
        "natural": ["water", "bay"],
        "place": ["sea"],
        "water":["lake"],
        "leisure": ["swimming_pool"],
    },
    "woodland": {
        "landuse": ["forest", "orchard"],
        "natural":["wood"],
        "boundary":["national_park"]
    },
    "grassland": {
        "landuse": ["grass", "vineyard", "orchard", "village_green"],
        "natural": ["grassland"],
        "leisure": ["park", "pitch", "garden", "golf_course"],
    },
    "farmland":{
        "landuse":["farmland","farmyard"], "place":["farm"]
    },
    "beach":{
        "natural":["beach", "sand"],
    },
    "islands":{
        "place":["island","islet"],
    },
    "streets": {
        "highway": [
            "motorway",
            "trunk",
            "primary",
            "secondary",
            "tertiary",
            "cycleway",
            "residential",
            "service",
            "unclassified",
            "footway",
            "motorway_link",
        ],
        "railway": True,
    },
    "other": {"amenity": ["parking"], "man_made": ["pier"], "highway": ["pedestrian"], "landuse":["quarry"]},
}

# Contains drawing settings

# https://colormagic.app/palette/6766d952be680a86c6260075
STYLES = {
    "Peach": { # e.g. Macau
        "urban": {
            "cmap": ["#FFC857", "#E9724C", "#C5283D"],
            "ec": "#2F3737",
            "lw": 0.001,
            "zorder": 4,
        },
        "water": {
            "fc": "#a1e3ff",
            "ec": "#85c9e6",
            "hatch": "ooo...",
            "hatch_c": "#2F3737",
            "lw": 1,
            "zorder": 1,
        },
        "grassland": {"fc": "#a6c851", "ec": "#2F3737", "lw": 0.1, "zorder": 2},
        "woodland": {"fc": "#4b8f3d", "ec": "#2F3737", "lw": 0.1, "zorder": 2},
        "farmland":{ "fc": "#f1c45b", "ec": "#2f3737", "lw":0.1, "zorder":2},
        "nature": { "fc": "#e2d9a6", "ec": "#2f3737", "lw":0.1, "zorder":2},
        "islands": {
            "fc": "#f2f4cb",
            "ec": "#ffe37a",
            "hatch": "ooo...",
            "hatch_c": "#2F3737",
            "lw":0.1,
            "zorder":1
        },
        "beach": { "fc": "#e3b82b", "ec": "#2f3737", "lw":0.1, "zorder":2},
        "streets": {"fc": "#2F3737", "zorder": 3},
        "other": {"fc": "#F2F4CB", "ec": "#2F3737", "lw": 1, "zorder": 3},

    },
    "Auburn": { # e.g. Barcelona
        "urban": {
            "cmap": ["#433633", "#FF5E5B", "#FF5E5B"],
            "ec": "#2F3737",
            "lw": 0.5,
            "zorder": 5,
        },
        "water": {
            "fc": "#a8e1e6",
            "ec": "#2F3737",
            "hatch": "ooo...",
            "hatch_c": "#9bc3d4",
            "lw": 1,
            "zorder": 3,
        },
        "grassland": {
            "fc": "#8BB174",
            "ec": "#2F3737",
            "hatch": "ooo...",
            "hatch_c": "#A7C497",
            "lw": 1,
            "zorder": 1,
        },
        "woodland": {"fc": "#64B96A", "ec": "#2F3737", "lw": 1, "zorder": 2},
        "streets": {"fc": "#2F3737", "zorder": 4},
        "other": {"fc": "#F2F4CB", "ec": "#2F3737", "lw": 1, "zorder": 3},
    },
    "Citrus": { # e.g. Würzburg
        "urban": {
            "cmap": ["#FFFF3F", "#F4D58D", "#F5CB5C"],
            "ec": "#2F3737",
            "lw": 0.5,
            "zorder": 5,
        },
        "water": {
            "fc": "#007F5F",
            "ec": "#2F3737",
            "lw": 1,
            "zorder": 3,
        },
        "grassland": {
            "fc": "#55A630",
            "ec": "#2F3737",
            "hatch": "ooo...",
            "hatch_c": "#80B918",
            "lw": 1,
            "zorder": 1,
        },
        "woodland": {"fc": "#80B918", "ec": "#2F3737", "lw": 1, "zorder": 2},
        "streets": {"fc": "#FFFFFF", "zorder": 4},
        "other": {"fc": "#EAE2B7", "ec": "#2F3737", "lw": 1, "zorder": 3},
    },
    "Flannel": { # e.g. Heerhugowaard
        "urban": {
            "cmap": ["#433633", "#FF5E5B", "#FF5E5B"],
            "ec": "#2F3737",
            "lw": 0.5,
            "zorder": 5,
        },
        "water": {
            "fc": "#a8e1e6",
            "ec": "#9bc3d4",
            "hatch_c": "#2F3737",
            "hatch": "ooo...",
            "lw": 1,
            "zorder": 3,
        },
        "grassland": {
            "fc": "#8BB174",
            "ec": "#A7C497",
            "hatch": "ooo...",
            "hatch_c": "#2F3737",
            "lw": 1,
            "zorder": 1,
        },
        "woodland": {"fc": "#64B96A", "ec": "#2F3737", "lw": 1, "zorder": 2},
        "streets": {"fc": "#2F3737", "zorder": 4, "ec": 475657},
        "other": {"fc": "#F2F4CB", "ec": "#2F3737", "lw": 1, "zorder": 3},
    },
}

STREETS_WIDTH = {k:0.1*v for k,v in {
    "motorway": 4,
    "trunk": 4,
    "primary": 3.5,
    "primary_link": 3.5,
    "motorway_link": 3,
    "secondary": 3,
    "secondary_link": 3,
    "tertiary": 2.5,
    "tertiary_link": 2.5,
    "cycleway": 2.5,
    "residential": 2,
    "service": 1.5,
    "unclassified": 1.5,
    "pedestrian": 1.5,
    "footway": 0.7,
}.items()}
