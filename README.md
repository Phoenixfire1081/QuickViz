# Visualization with Mayavi and traitsUI

In the current version only isosurfaces with 3D scalar fields are supported.

## Required packages

The following packages are necessary - mayavi, PyQt5, traitsui==7.4.3 (8 causes problems)

```
pip install mayavi PyQt5
pip install --upgrade traitsui==7.4.3
```

## Usage - single threshold

In this case, a slider is presented to choose the threshold. A precise input can also be made in the text field.

```
from mayaviVisualization import mayaviVisualizeWithThreshold

visObject = mayaviVisualizeWithThreshold(scalarField)
visObject.configure_traits()
```

## Usage - multiple thresholds

The thresholds can be entered in the given text field within box brackets. 

```
from mayaviVisualization import mayaviVisualizeWithMultipleThreshold

visObject = mayaviVisualizeWithMultipleThreshold(scalarField)
visObject.configure_traits()
```
