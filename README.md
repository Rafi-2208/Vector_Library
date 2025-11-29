# Vector_Library
fast library for vector operations

This is a simple python library for 2d (and in future 3d) vector operation with goal to run faster than numpy on low dimensional arrays

# Features:
-all arithmetic operations work on 2 vectors as well as vector and number

## Functions:
-length(self): Returns length of vector

-norm(self): Returns normalised vector

-rotate(self, a): Returns vector rotated by angle in degrees

-dot(v1, v2): Returns dot product of two vectors

-cross(v1, v2): Returns cross product of two vectors

-angle(v1, v2 ,mode): Returns the angle between two vectors (-180 to 180 range counter-clockwise being positive). If only one vector is given returns angle from positive x-axis. Has 2 modes 'd' and 'r' which return angle in degrees or radians respectively (default mode is degrees).

-project(v1 , v2): Returns vector projected from vector v1 to vector v2 and remaining vector perpendicular to vector v2

-reflect(v1 , v2): Returns vector v1 reflected in vector v2
