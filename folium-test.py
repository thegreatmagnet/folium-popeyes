""" flask_example.py

    Required packages:
    - flask
    - folium

    Usage:

    Start the flask server by running:

        $ python flask_example.py

    And then head to http://127.0.0.1:5000/ in your browser to see the map displayed

"""

from flask import Flask

import folium

import pandas as pd 

locations = pd.read_csv('popeyes.csv')


app = Flask(__name__)


@app.route('/')
def index():


    map1=folium.Map(location=[47.608013, -122.335167],tiles='cartodbpositron',zoom_start=11)

    for i, row in locations.iterrows():
        folium.Marker(location=[row['Lat'], row['Lon']], popup=row['Full Address']).add_to(map1)

    
    return map1._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)