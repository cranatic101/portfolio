from flask import Flask, render_template, request, jsonify
from app import app

@app.route("/",methods=['GET','POST'])
def index():
  return render_template("index.html")