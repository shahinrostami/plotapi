"""Chord - Python wrapper around d3-chord

This package enables the generation of Chord diagrams. They can be saved 
directly to HTML files or displayed in a Jupyter Notebook output cell.

Copyright 2020, Dr. Shahin Rostami
http://shahinrostami.com
https://github.com/shahinrostami/chord
https://pypi.org/project/chord/
"""

from mako.template import Template
import mako.runtime
import urllib.request
import uuid

# undefined template values default to empty strings
mako.runtime.UNDEFINED = ""


class ColorScheme:
    # Categorical
    Category10 = "d3.schemeCategory10"
    Accent = "d3.schemeAccent"
    Dark2 = "d3.schemeDark2"
    Paired = "d3.schemePaired"
    Pastel1 = "d3.schemePastel1"
    Pastel2 = "d3.schemePastel2"
    Set1 = "d3.schemeSet1"
    Set2 = "d3.schemeSet2"
    Set3 = "d3.schemeSet3"
    Tableau10 = "d3.schemeTableau10"

    # Diverging
    BrBG = "d3.schemeBrBG"
    PRGn = "d3.schemePRGn"
    PiYG = "d3.schemePiYG"
    PuOr = "d3.schemePuOr"
    RdBu = "d3.schemeRdBu"
    RdGy = "d3.schemeRdGy"
    RdYlBu = "d3.schemeRdYlBu"
    RdYlGn = "d3.schemeRdYlGn"
    Spectral = "d3.schemeSpectral"

    # Sequential
    Blues = "d3.schemeBlues"
    Greens = "d3.schemeGreens"
    Greys = "d3.schemeGreys"
    Oranges = "d3.schemeOranges"
    Purples = "d3.schemePurples"
    Reds = "d3.schemeReds"

    # Sequential Multi-Hue
    BuGn = "d3.schemeBuGn"
    BuPu = "d3.schemeBuPu"
    GnBu = "d3.schemeGnBu"
    OrRd = "d3.schemeOrRd"
    PuBuGn = "d3.schemePuBuGn"
    PuBu = "d3.schemePuBu"
    PuRd = "d3.schemePuRd"
    RdPu = "d3.schemeRdPu"
    YlGnBu = "d3.schemeYlGnBu"
    YlGn = "d3.schemeYlGn"
    YlOrBr = "d3.schemeYlOrBr"
    YlOrRd = "d3.schemeYlOrRd"

    def __init__(self, val):
        exclude = (
            "Category10", "Accent", "Dark2", "Paired",
            "Pastel1", "Pastel2", "Set1", "Set2", "Set3",
            "Tableau10"
        )

        num = val if isinstance(val, int) else len(val)

        for attr, val in self.__dict__.items():
            if not attr.startswith("__") and attr not in exclude:
                self.__dict__[attr] = f"{val}[{num}]"


class Chord:
    template_url = "https://shahinrostami.com/assets/chord/chord.tmpl"
    template = urllib.request.urlopen(template_url).read()

    def __init__(
        self,
        matrix,
        names,
        colors="d3.schemeSet1",
        opacity=0.8,
        padding=0.01,
        label_color="#454545",
        wrap_labels=True,
    ):
        self.html = Chord.template
        self.matrix = matrix
        self.names = names
        self.colors = colors
        self.opacity = opacity
        self.padding = padding
        self.label_color = label_color
        self.wrap_labels = wrap_labels

    def __str__(self):
        return self.html

    """Generates the HTML using the Mako template."""

    def render_html(self):
        self.tag_id = "chart-" + str(uuid.uuid4())[:8]
        self.html = Template(Chord.template).render(
            colors=self.colors,
            opacity=self.opacity,
            matrix=self.matrix,
            names=self.names,
            padding=self.padding,
            label_color=self.label_color,
            tag_id=self.tag_id,
            wrap_labels="true" if self.wrap_labels else "false",
        )

    """Outputs the generated HTML to a HTML file. """

    def to_html(self, filename="out.html"):
        self.render_html()
        with open(filename, "w") as file:
            file.write(self.html)

    """Outputs the generated HTML to a Jupyter Notebook output cell."""

    def show(self):
        self.render_html()
        from IPython.display import display, HTML

        display(HTML(self.html))
