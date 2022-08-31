"""
Plotapi - Engaging visualisations, made easy.

This package enables the generation of beautiful visualisations. 
They can be saved directly to HTML, PNG, PDF, and MP4 files.
They can also be displayed in a Jupyter Notebook output cell.

Copyright 2021-2022, Dr. Shahin Rostami
http://shahinrostami.com
http://plotapi.com
https://github.com/shahinrostami/plotapi
https://pypi.org/project/plotapi/
"""
""" LICENSE
MIT
"""
import json
import os
import requests

session = requests.Session()
url = "https://plotapi.com"
ssl_verficiation = True
path = os.path.dirname(__file__)

try:
    with open(f"{path}/plotapi_api_key", "r") as api_key_file:
        env_api_key = api_key_file.read().replace("\n", "")

        if env_api_key != None:
            session.auth = ("api_key", env_api_key)
except:
    pass


def content_encoding(raw_params):
    return raw_params, "identity"


def api_key(key):
    global session
    session.auth = ("api_key", key)

    try:
        with open(f"{path}/plotapi_api_key", "w") as api_key_file:
            print(key, file=api_key_file)

        print(
            "Your Plotapi API key has been saved in your local environment. You will not need to set it again."
        )
    except:
        pass


class Visualisation:
    def api_key(key):
        api_key(key)

    def verify_ssl(truth):
        global ssl_verficiation
        ssl_verficiation = truth

    def set_license(username, password):
        global session
        session.auth = (username, password)

    def __init__(self, params, endpoint):
        self.params = params
        self.endpoint = endpoint

    """PlotAPI Generation"""

    def get_html(self):
        """Generates the HTML using the Plotapi service."""
        params, directive = content_encoding(self.params)
        result = session.post(
            f"{url}/{self.endpoint}/",
            json=params,
            headers={"Content-Encoding": directive},
            verify=ssl_verficiation,
        )

        if result.status_code == 200:
            return result.text
        else:
            detail = json.loads(result.content.decode("utf8"))
            raise Exception(detail)

    def get_png(self):
        """Generates the PNG using the Plotapi service."""
        params, directive = content_encoding(self.params)
        result = session.post(
            f"{url}/{self.endpoint}/png",
            json=params,
            headers={"Content-Encoding": directive},
            verify=ssl_verficiation,
        )

        if result.status_code == 200:
            return result.content
        else:
            detail = json.loads(result.content.decode("utf8"))
            raise Exception(detail)

    def get_pdf(self):
        """Generates the PDF using the Plotapi service."""
        params, directive = content_encoding(self.params)
        result = session.post(
            f"{url}/{self.endpoint}/pdf",
            json=params,
            headers={"Content-Encoding": directive},
            verify=ssl_verficiation,
        )

        if result.status_code == 200:
            return result.content
        else:
            detail = json.loads(result.content.decode("utf8"))
            raise Exception(detail)

    def get_mp4(self):
        """Generates the MP4 using the Plotapi service."""
        params, directive = content_encoding(self.params)
        result = session.post(
            f"{url}/{self.endpoint}/mp4",
            json=params,
            headers={"Content-Encoding": directive},
            verify=ssl_verficiation,
        )

        if result.status_code == 200:
            return result.content
        else:
            detail = json.loads(result.content.decode("utf8"))
            raise Exception(detail)

    def to_string(self, filename="out.html"):
        """Outputs the generated HTML to as a string."""
        html = self.get_html()
        return html

    """ File output"""

    def to_html(self, filename="out.html"):
        """Outputs the generated HTML to a HTML file."""
        html = self.get_html()
        file = open(filename, "w", encoding="utf-8")
        file.write(html)
        file.close()

    def to_png(self, filename="out.png"):
        """Outputs the generated PNG to a file."""
        image = self.get_png()
        file = open(filename, "wb")
        file.write(image)
        file.close()

    def to_pdf(self, filename="out.pdf"):
        """Outputs the generated PDF to a file."""
        pdf = self.get_pdf()
        file = open(filename, "wb")
        file.write(pdf)
        file.close()

    def to_mp4(self, filename="out.mp4"):
        """Outputs the generated MP4 to a file."""
        pdf = self.get_mp4()
        file = open(filename, "wb")
        file.write(pdf)
        file.close()

    """ Jupyter Lab output"""

    def show(self):
        """Outputs the generated HTML to a Jupyter Lab output cell."""
        from IPython.display import display, HTML

        html = self.get_html()
        display(HTML(html))

    def show_png(self):
        """Outputs the generated PNG to a Jupyter Lab output cell."""
        from IPython.display import display, Image

        image = self.get_png()
        display(Image(image))

    def show_mp4(self):
        """Outputs the generated MP4 to a Jupyter Lab output cell."""
        from IPython.display import display
        from IPython.core.display import Video

        video = self.get_mp4()
        display(
            Video(
                video,
                mimetype="video/mp4",
                html_attributes="autoplay controls",
                embed=True,
            )
        )


class Chord(Visualisation):
    def __init__(self, matrix, names, **kwargs):
        params = kwargs
        params["matrix"] = matrix
        params["names"] = names
        endpoint = "chord"
        super().__init__(params, endpoint)


class Sankey(Visualisation):
    def __init__(self, links, **kwargs):
        params = kwargs
        params["links"] = links
        endpoint = "sankey"
        super().__init__(params, endpoint)


class Terminus(Visualisation):
    def __init__(self, links, **kwargs):
        params = kwargs
        params["links"] = links
        endpoint = "terminus"
        super().__init__(params, endpoint)


class BarFight(Visualisation):
    def __init__(self, samples, **kwargs):
        params = kwargs
        params["samples"] = samples
        endpoint = "barfight"
        super().__init__(params, endpoint)


class PieFight(Visualisation):
    def __init__(self, samples, **kwargs):
        params = kwargs
        params["samples"] = samples
        endpoint = "piefight"
        super().__init__(params, endpoint)


class HeatMap(Visualisation):
    def __init__(self, matrix, **kwargs):
        params = kwargs
        params["matrix"] = matrix
        endpoint = "heatmap"
        super().__init__(params, endpoint)


class LineFight(Visualisation):
    def __init__(self, samples, **kwargs):
        params = kwargs
        params["samples"] = samples
        endpoint = "linefight"
        super().__init__(params, endpoint)


class ParetoFront(Visualisation):
    def __init__(self, samples, **kwargs):
        params = kwargs
        params["samples"] = samples
        endpoint = "paretofront"
        super().__init__(params, endpoint)
