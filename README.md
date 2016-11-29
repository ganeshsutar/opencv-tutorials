# OpenCV

Some tutorial and a framework to work with OpenCV

### Tutorials
1. Basic Image Reading
1. Basic Video Capturing
1. Basic Video file reading

### TODO
1. A simple pipeline for creating and applying filters to Video

### Basic Working
Basically, this python script provides some classes for pipeline filtering.
For example, given a input we need to convert it into respective output,
through the pipeline which has various filter. e.g. It might be having a
ColorConverter to gray, then some edge filtering and the extract some object
may be template matching and other. At each stage we need some hook to extract
information and enrich our model.

`Input -> Filter -> Filter -> ... -> Filter -> Output`

In more generic sense we can convert the input and output to a filter also, but
right now, handling is in complete meaning as it is.

Filter can have multiple input and also multiple output, when creating the
pipeline we can add and retrive info from it.
