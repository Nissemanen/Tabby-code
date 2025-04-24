import os
from .package import package

__all__ = ["final_product_dir"]

final_product_dir = os.path.join(os.path.dirname(__file), "_final_produt.json")

with open("._final_product.json", "w") as _f:
    _f.write("")
