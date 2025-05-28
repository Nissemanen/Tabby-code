.. Tabby code documentation master file, created by
   sphinx-quickstart on Thu May 22 17:25:29 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Tabby code documentation
========================

Add your content using reStructuredText syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.

sprite module
=============

This module defines the `Sprite` class, which represents a visual object (sprite) in a project structure
similar to a Scratch-like environment.

It contributes data to a shared `json_project` dictionary.

Classes
-------

Sprite
------

.. class:: Sprite(name: str)

   Represents a sprite object in the project.

   :param name: The name of the sprite.

   Upon initialization, the sprite:
     - Appends its name to a global sprite list.
     - Adds a corresponding entry in the `json_project["targets"]` list.

   Attributes:
     - name (str): The name of the sprite.
     - __sprite_num (int): Order in which the sprite was added.
     - __parent: Parent object (initially `None`).

   Example target dictionary added to the project:

   .. code-block:: json

      {
         "isStage": False,
         "name": "Sprite1",
         "variables": [],
         "lists": {},
         "broadcasts": {},
         "blocks": {},
         "comments": {},
         "currentCostume": 0,
         "costumes": [],
         "sounds": [],
         "volume": 100,
         "layerOrder": 1,
         "visible": True,
         "x": 0,
         "y": 0,
         "size": 100,
         "direction": 90
      }