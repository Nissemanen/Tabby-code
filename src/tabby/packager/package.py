import os
import json


def package(path: str):
    print(f"successfully packaged to {path}")

def set_final_product(inp: str):
    with open(os.path.join(os.path.dirname(__file__), "_final_product.json"), "w") as _fin_pro:
        return json.dump(inp, _fin_pro)

def get_final_product():
    with open(os.path.join(os.path.dirname(__file__), "_final_product.json"), "r") as _fin_pro:
        return json.load(_fin_pro)

def append_final_product(inp: str):
    return None