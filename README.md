# Visualization with Mayavi

In the current version only isosurfaces with 3D scalar fields are supported.

## Usage - single threshold

In this case, a slider is presented to choose the threshold. A precise input can also be made in the text field.

```
visObject = mayaviVisualizeWithThreshold(scalarField)
visObject.configure_traits()
```

## Usage - multiple thresholds

The thresholds can be entered in the given text field within box brackets. 

```
visObject = mayaviVisualizeWithMultipleThreshold(scalarField)
visObject.configure_traits()
```
