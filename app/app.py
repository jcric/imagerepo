from re import S
from typing import List, Dict

from numpy import var
from flask import Flask, request, render_template, request
import mysql.connector
import json
app = Flask(__name__)
DB_conf = { 'user': 'root', 'password': 'root', 'host': 'db',
            'port': '3306', 'database': 'links' }

def test_table():
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   cursor.execute('SELECT * FROM images')
   results = [c for c in cursor]
   cursor.close()
   connection.close()
   return results

def add_item(title, link, image_description):
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   request = f"INSERT INTO images (title, link, image_description) VALUES ('{title}', '{link}', '{image_description}');"
   cursor.execute(request)
   connection.commit()
   cursor.close()
   connection.close()
   return request

def delete_items(title):
   connection = mysql.connector.connect(**DB_conf)
   cursor = connection.cursor()
   request = f"DELETE FROM images WHERE title ='{title}';"
   cursor.execute(request)
   connection.commit()
   cursor.close()
   connection.close()
   return request


def style():
   S  = "<style>\n"
   S += """
  body {
  background-color: black;
  background-image: radial-gradient(
    rgba(0, 150, 0, 0.75), black 120%
  );
  height: 100vh;
  margin: 0;
  padding: 2rem;
  color: white;
  font: 1.3rem Inconsolata, monospace;
  text-shadow: 0 0 5px #C8C8C8;
  &::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: repeating-linear-gradient(
      0deg,
      rgba(black, 0.15),
      rgba(black, 0.15) 1px,
      transparent 1px,
      transparent 2px
    );
    pointer-events: none;
  }
}
::selection {
  background: #0080FF;
  text-shadow: none;
}
pre {
  margin: 0;
}
a:link {
  color: green;
  background-color: transparent;
  text-decoration: none;
}

a:visited {
  color: pink;
  background-color: transparent;
  text-decoration: none;
}
a:hover {
  color: red;
  background-color: transparent;
  text-decoration: underline;
}

"""
   S += "</style>\n"
   return S


@app.route('/add')
def add():
   title = request.args.get("title", "", str)
   link = request.args.get("link", "", str)
   image_description = request.args.get("image_description", "", str)
   S =  "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += style()
   S += "      <title>Added a link</title>\n"
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Added a link</h1>\n"
   if title != "":
      S += add_item(title, link, image_description)
   S += "      <p><a href='/'>Back!</a></p>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S




@app.route('/delete')
def delete():
   title = request.args.get("title", "", str)
   S =  "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += style()
   S += "      <title>Removed a link</title>\n"
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Removed a link</h1>\n"
   if title != "":
      S += delete_items(title)
   S += "      <p><a href='/'>Back!</a></p>\n"
   S += "   </body>\n"
   S += "</html>\n"
   return S




@app.route('/')
def index():
   S = "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += style()
   S += "      <title>Links to images list</title>\n"
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Links to images list</h1>\n"
   S += "      <ul>\n"
   for (title, link, image_description) in test_table():
      S += f"""<div> {title} <br> <a href="{link}">{link}</a> <br>  {image_description} <br> <br> </div>\n"""
   S += "      </ul>\n"
   S += '<a href="http://localhost:8000/visualisation">Images displayed</a> <br>'
   S += '<a href="http://localhost:8000/deleteform">Form for deleting</a> <br>'
   S += '<a href="http://localhost:8000/addform">Form for adding</a>'
   S += "   </body>\n"
   S += "</html>\n"
   return S


@app.route('/visualisation')
def vis():
   S = "<!DOCTYPE html>\n"
   S += "<html>\n"
   S += "   <head>\n"
   S += style()
   S += "      <title>Images displayed</title>\n"
   S += "   </head>\n"
   S += "   <body>\n"
   S += "      <h1>Images displayed</h1>\n"
   S += '<a href="http://localhost:8000/">Back!</a> <br>'
   S += "      <ul>\n"
   for (title, link, image_description) in test_table():
      S += f"""<div> {title} </div>\n"""
      S += f"""<img src="{link}" alt="{title}" width="500"<br> <br><br>\n"""
   return S

@app.route('/addform')
def addform():
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "   <head>\n"
    S += style()
    S += "      <title>Entering a value</title>\n"
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Entering a value</h1>\n"
    S += "      <form action='/add'>\n"
    S += "        <input type='text' name='title' value='Max-min Temperature Map of US'/>\n"
    S += "        <input type='text' name='link' value='https://upload.wikimedia.org/wikipedia/commons/4/40/2017-08-25_Max-min_Temperature_Map_NOAA.png'/>\n"
    S += "        <input type='text' name='image_description' value='A map of the US with Max-min Temperature'/>\n"
    S += "        <input type='submit' value='Submit'/>\n"
    S += "      </form>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S


@app.route('/deleteform')
def deleteformform():
    S  = "<!DOCTYPE html>\n"
    S += "<html>\n"
    S += "   <head>\n"
    S += style()
    S += "      <title>Entering a value</title>\n"
    S += "   </head>\n"
    S += "   <body>\n"
    S += "      <h1>Entering a value</h1>\n"
    S += "      <form action='/delete'>\n"
    S += "        <input type='text' name='title' value='Max-min Temperature Map of US'/>\n"
    S += "        <input type='submit' value='Submit'/>\n"
    S += "      </form>\n"
    S += "   </body>\n"
    S += "</html>\n"
    return S





if __name__ == '__main__':
   app.run(host='0.0.0.0')
