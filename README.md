
<h1 align="center">
  <br>
  <a href="https://plotapi.com"><img src="https://plotapi.com/wp-content/uploads/2021/07/plotapi_logo.svg" alt="PlotAPI" width="300"></a>
</h1>

<h4 align="center">Engaging visualisations, made easy.</h4>

<p align="center">
<a href="https://pypi.org/project/plotapi/"><img src="https://img.shields.io/badge/pypi%20package-7.0.0-success.svg"></a>
<a href="https://crates.io/crates/plotapi"><img src="https://img.shields.io/badge/rust%20crate-1.0.0-success.svg"></a>
<a href="https://plotapi.com/pricing/"><img src="https://img.shields.io/badge/license-get-green.svg"></a>
<a href="https://discord.polyra.com"><img src="https://img.shields.io/badge/chat-join-7289da.svg"></a>
<a href="https://jupyter.org"><img src="https://img.shields.io/badge/supports-jupyter-orange.svg"></a>
<a href="https://www.linkedin.com/in/shahinrostami/"><img src="https://img.shields.io/badge/linked-in-blue.svg"></a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="https://plotapi.com/#pricing">Get Access</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="https://plotapi.com/docs">Docs</a>
</p>

![screenshot](https://plotapi.com/wp-content/uploads/2021/08/1500x500.jpeg)

## Key Features

* **PlotAPI Chord** - Illustrate inter-relationships between data.
* **PlotAPI SplitChord** - Illustrate inter-relationships between bipartite data.
* **PlotAPI Sankey** - Illustrate the flow from one set of values to another.
* **PlotAPI Terminus** - Illustrate distributing something out amongst recipients.
* **PlotAPI Bar Fight** - A beautiful take on the classic Bar Chart Race.
* **PlotAPI Pie Fight** - A beautiful take on the classic Pie Chart Race.
* **PlotAPI Heat Map** - Beautiful and interactive heat maps.
* **PlotAPI Line Fight** - A beautiful take on the classic Line Chart Race.
* **PlotAPI Pareto Front** - Illustrate non-dominated (Pareto) fronts over time.
* **PlotAPI Goal rush** - Illustrate progress toward a goal over time.
* **Upcoming Visualisations** - Access to new visualisations as they are introduced.
* **Supports Most Programming Languages** - Get started with any language able to make HTTP requests.
* **First-Class Python Support** - Get started with pip install plotapi
* **Jupyter Lab/Notebook + Google Colab Support** - Super-charge your notebooks with inline visualisations.
* **Beautiful Themes & Fonts** - Select from pre-made beautiful themes, or add your own.
* **Share or Embed Interactive HTML** - Download and embed your interactive visualisations.
* **Upload and Share** - Upload and share your visualisations, privately or publicly.
* **Render to PDF, SVG, or PNG** - Generate high-quality output ready for print.
* **Record Animation to MP4 Video** - Create social media-ready animated visualisations.

## Get Access

Visit [the website](https://plotapi.com/#pricing) to get access to PlotAPI.

## Installation

Get up and running with Python with the following command.

```bash
pip install plotapi
```

## Usage

### Example - Chord Pro

https://user-images.githubusercontent.com/15690380/126084021-b008b256-2a31-4106-84af-42777ea480d9.mp4

#### Created with PlotAPI

```python
Chord(matrix, names).show()
```

#### The data

```python
matrix = [
    [0, 5, 6, 4, 7, 4],
    [5, 0, 5, 4, 6, 5],
    [6, 5, 0, 4, 5, 5],
    [4, 4, 4, 0, 5, 5],
    [7, 6, 5, 5, 0, 4],
    [4, 5, 5, 5, 4, 0],
]

names = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Thriller"]
```

### Example - Sankey Pro

https://user-images.githubusercontent.com/15690380/126084745-712fd744-b626-429d-85f3-30b11979fe30.mp4

#### Created with PlotAPI

```python
Sankey(links).show()
```

#### The data

```python
links = [
    {"source":"Salary", "target":"Me", "value": 40000},
    {"source":"Freelance", "target":"Me", "value": 10000},
    {"source":"Dividends", "target":"Me", "value": 6000},

    {"source":"Me", "target":"Rent", "value": 1100*12},
    {"source":"Me", "target":"Food", "value": 300*12},
    {"source":"Me", "target":"Magazine Subscription", "value": 2000},
    {"source":"Me", "target":"Personal Tax", "value": 6000},
    {"source":"Me", "target":"Investments", "value": 30000},

    {"source":"Investments", "target":"Facebook", "value": 8000},
    {"source":"Investments", "target":"Amazon", "value": 7000},
    {"source":"Investments", "target":"Apple", "value": 6000},
    {"source":"Investments", "target":"Netflix", "value": 5000},
    {"source":"Investments", "target":"Google", "value": 4000},
]
```

## License

MIT

---

## Prefer not to code? Try the App at PlotAPI.com

<a href="https://plotapi.com"><img src="https://plotapi.com/static-asset/marketing/plotpanel_preview_2.jpg" alt="PlotAPI front-end"></a>


> [plotapi.com](https://plotapi.com) &nbsp;&middot;&nbsp;
> GitHub [@shahinrostami](https://github.com/shahinrostami) &nbsp;&middot;&nbsp;
> Twitter [@shahinrostami](https://twitter.com/shahinrostami)  &nbsp;&middot;&nbsp;
> A [Polyra](https://polyra.com) innovation
