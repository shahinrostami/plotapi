from mako.template import Template
import mako.runtime
import urllib.request

# undefined template values default to empty strings
mako.runtime.UNDEFINED = ""


class Chord(object):
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
    ):
        self.html = Chord.template
        self.matrix = matrix
        self.names = names
        self.colors = colors
        self.opacity = opacity
        self.padding = padding
        self.label_color = label_color

        self.html = Template(self.template).render(
            colors=colors,
            opacity=opacity,
            matrix=matrix,
            names=names,
            padding=padding,
            label_color=label_color,
        )

    def __str__(self):
        return self.html

    def to_html(self, filename="out.html"):
        file = open(filename, "w")
        file.write(self.html)
        file.close()

    def show(self):
        from IPython.display import display, HTML

        display(HTML(self.html))
