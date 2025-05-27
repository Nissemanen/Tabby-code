# Tabby-code

> <h3>ta·bee<h3>
> 
> a grey or brownish cat mottled or streaked with dark stripes.


this is a passion project to make it easier in the transition from block based coding to text based

# Installation
not implemented yet (will propably first be seen in the first version)

# For Others
If you want to remake/fix/make a better one (cause im absolutly not good at coding) i will have some simple scratch code documentation. such as how json files are structured or how other stuff in scratch works.

## Json formating for scratch
there is a web page for this but ill go a litle more detailed with absolutly everything ive found.

the scratch sb3 file is just a fancy zip file. And beneath that is a json file with everything in it, Ill try explain every property of the scratch json files.

first of all there are four main objects. `"targets"`, `"monitors"`, `"extentions"` and `"meta"`

its in `"targets"` where all the sprites and their data is stored.<br>
in `"monitors"` you find all the monitors with their positions and values.<br>
in `"extentions"` is where all the extentions are, such as the pen extention.<br>
in `"meta"` is all the metadata that the project has, this is usualy not tamperd with.<br>

### targets
every target has some core components, these are:

`isStage` if the target is the stage or not <br>
`name` the name of the sprite/stage <br>
`variabels` an array with all the targets variables <br>
`lists` an array with all the targets lists<br>
`broadcasts` an array with all the targets broadcasts<br>
`blocks` an array with all the targets blocks

