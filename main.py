from reactpy import component, web, html
from reactpy.backend.flask import configure
from flask import Flask
from datos import productos

mui = web.module_from_template("react", "@mui/material" , fallback="⌛")
Container = web.export(mui, "Container")
Grid = web.export(mui, "Grid")
peper = web.export(mui, "Paper")
Box = web.export(mui, "Box")
Typography = web.export(mui, "Typography")
Rating = web.export(mui, "Rating")

def targetas(productos):
  def targeta(producto):
    return Grid(
      {"item": True, "sm": 6, "md": 3, "lg": 3},
      peper(
        {"elevation": 4},
        html.img({
          "src": f"https://picsum.photos/id/{producto['id']}/400/100",
          "class_name": "img-fluid",
          "style": { "widh": "100%" , "height": "5rem"}
        }),
        Box(
          {"sx": {"bgcolor": "background.paper"}},
          Typography({"variant": "h5"}, producto['nombre']),
          Rating({
            "readOnly": True, 
            "name": "half-rating",
            "presicion": "0.5",
            "value": producto['rating']
          }),
          Typography({"variant": "body2"}, producto['descripcion']),
          Typography({"variant": "h5"}, producto['precio']),
        )
      )
    )
  return Grid(
    {"containter": True, "spacing": 8},
    [targeta(producto) for producto in productos]  
 )

@component
def App():
    return Container (
      { "maxWidth": "md" },
      targetas(productos)
    )
app = Flask (__name__)
configure(app, App)
app.run(host='0.0.0.0', debug=True)
