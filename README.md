# A fast and lightweight post-processing framework

Based on [mayavi](https://docs.enthought.com/mayavi/mayavi/), this framework is useful to visualize and perform calculations on Fluid flow data. It supports the following visualization options:

- Isosurfaces
- Volume rendering
- 2D slice (filled and unfilled contours, streamlines with line integral convolution technique, vector slice)
- 3D streamlines

## Required packages

The following packages are necessary - mayavi, PyQt5, traitsui==7.4.3 (8 causes problems)

```
pip install mayavi PyQt5
pip install traitsui==7.4.3
pip install pyface==7.4.4
```

## UI

The framework has several modes: 

- Dataset (allows local import, JHTDB support will be added later).
- Visualization with options mentioned above.
- Analysis (consult documentation for explanation on the various tools).
- Log-lattice (interface for the log-lattice simulation code developed by Dr. Amaury Barral).

![Screenshot](resources/Layout.png)

## Usage 

Documentation is being built with Sphinx and readthedocs and can be seen at https://quickviz.readthedocs.io/en/latest/. Some components may not work. 

## Known issues

The UI works reasonably well on Linux machines but the elements appear to be spaced out oddly on Mac OS.
Tested machines:

- Ubuntu 24.04
- Mac OS Sequoia
