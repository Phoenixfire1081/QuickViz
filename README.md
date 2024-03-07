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

## Usage - time series

Similar to the multiple thresholds case, the required thresholds can be entered in the given text field within box brackets. 

The time series data needs to be prepared in the following manner.

```
# Number of time steps
nTs = 5

# Create 4D scalar field with time as the last dimension
# xlen, ylen, zlen corresponds to the size of the 3D scalar field
timeSeries = np.zeros((xlen, ylen, zlen, ts), dtype = _dtype)

# Loop and add scalar fields
for i in range(ts):
  timeSeries[:, :, :, i] += scalar

```
The next part is same as before

```
from mayaviVisualization import mayaviVisualizeTimeSeries

visObject = mayaviVisualizeTimeSeries(timeSeries)
visObject.configure_traits()
```
