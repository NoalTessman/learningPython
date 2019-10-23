import plotly.io as pio
series = [1,2,3]
numarr =[1,2,3]
phold = [1,2,3]

def landGrapher():
    fig = {
        "data":[{"type":"mesh3d",
        'x':series,
        'y':numarr,
        'z':phold}],
    }
    pio.show(fig)
landGrapher()