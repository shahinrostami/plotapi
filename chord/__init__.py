from mako.template import Template
import mako.runtime
import urllib.request
import uuid

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

    def render_html(self):
        self.tag_id = "chart-" + str(uuid.uuid4())[:8]
        print(self.tag_id)
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

    def to_html(self, filename="out.html"):
        self.render_html()
        file = open(filename, "w")
        file.write(self.html)
        file.close()

    def show(self):
        self.render_html()
        from IPython.display import display, HTML

        display(HTML(self.html))
