# Programs related to Transformation and Recognizing objects
1. Detect corners and try for some perpective transformation

# Programs related to Environment
1. Create a program that detect various objects from the environment
1. Create a program that detect new object and add into his list for objects
1. Create a program that holds the environment data
1. Create a program that find the relative positioning of the objects

# Programs related to Goals and Learning
1. Thinking ...

# Learning from the Images
1. Learning for the data, about the environment

# Simple Programs
1. Face detecting and identification
1. Greeting respective to face identification

### Some consideration
Input and Output cannot be filters since they generate the stream one by one
and filter process one at a time. ???!&^%@&!

For now, filters work on only one stream, we need to think about how to create
and combine streams.

### Design
We can create input and output as a separate entity in the design domain.
Input are the ones that creates frames and have a starting filters.
Where as output can be consider to be a simple filter, so that we can add at
any intermediate point and see the output.
Output filter can be special so that they can be added at multiple points.

Example of input filter can be a directory of images, a random image generator,
or a single image reader, or a video file, or a video capture.
Output can be to window, or to a video file, or to a directory.
