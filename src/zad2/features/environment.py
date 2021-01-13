from behave import *
from src.zad2.hamming import Hamming

def before_scenario(context, scenario):
    context.hamming = Hamming()

def after_scenario(context, scenario):
    context.hamming = None
