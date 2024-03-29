# Optimization
Various optimization mini-projects.


## Solving a Sudoku Puzzle

Consider the following Sudoku puzzle<sup>1</sup>:

 <p align="center">
  </p>
<figure>
  <p align="center">
    <img src="https://github.com/bwalzer4/Optimization/blob/main/Visuals/Sudoku_1.png?raw=True" />
  </p>
</figure>

How can we write a program or algorithm to solve the Sudoko puzzle? One solution is to formulate the puzzle as a binary optimization problem. To formulate the problem we first start by setting up the constraints. The constraints for the Sudoko puzzle are as follows:

1. Each cell can be filled with only the numbers 1-9
2. In each 3 x 3 square a number may only appear once
3. In each row and column a number may only appear once

The objective function in this optimization problem is arbitrary since we are just looking for any solution that satisfies the constraints and do not require a minimum or maximum value. I formulated and solved the optimization problem using the Python Convex Optimization Package (CVXPY).<sup>2</sup>

The output below shows the solution to the Sudoko puzzle!

```python
>>>solved_sodoku
array([[9., 7., 6., 4., 8., 5., 1., 2., 3.],
       [3., 8., 4., 2., 1., 9., 5., 7., 6.],
       [1., 5., 2., 3., 7., 6., 8., 4., 9.],
       [8., 9., 7., 6., 5., 4., 3., 1., 2.],
       [4., 6., 3., 7., 2., 1., 9., 8., 5.],
       [2., 1., 5., 9., 3., 8., 7., 6., 4.],
       [6., 3., 9., 1., 4., 7., 2., 5., 8.],
       [5., 2., 1., 8., 6., 3., 4., 9., 7.],
       [7., 4., 8., 5., 9., 2., 6., 3., 1.]])
```

## Generating a 2-D Ellipsoid to Circumscribe a Set of Points

Given a random set of points, such as the ones below, how can we generate an ellipsoid with the smallest area? One solution is to formulate and solve a semidefinite optimization problem. Semidefinite programs are a convex optimization problems with variables that are positive semidefinite matrices. A positive semidefinite matrix is definied by having nonnegative eigenvalues. 

 <p align="center">
  </p>
<figure>
  <p align="center">
    <img src="https://github.com/bwalzer4/Optimization/blob/main/Visuals/random_points.png?raw=True" />
  </p>
</figure>

The optimization problem can be formulated as follows:

 <p align="center">
  </p>
<figure>
  <p align="center">
    <img src="https://github.com/bwalzer4/Optimization/blob/main/Visuals/SDP_program.PNG?raw=True" />
  </p>
</figure>

The first set of constraints is predicated on the equation of the ellipsoid, and the second constraint indicates the matrix must be positive semidefinite. Solving for <b>A</b> and <b>b</b> allows us to derive the ellipsoid shape matrix and center. From there we can plot the ellipsoid over the original set of points.

 <p align="center">
  </p>
<figure>
  <p align="center">
    <img src="https://github.com/bwalzer4/Optimization/blob/main/Visuals/ellipsoid.png?raw=True" />
  </p>
</figure>

## References and Notes
1. Sudoko puzzle found on https://www.extremesudoku.info/ from 7 November 2021.
2. https://www.cvxpy.org/
