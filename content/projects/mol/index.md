---
title: Gradient-based Algorithms for Multi-objective Optimization
summary: Research on continuous optimization methods for vector-valued functions, focusing on steepest descent, Newton-like methods, and bilevel optimization structures using JAX.
tags:
  - Mathematical Programming
  - Continuous Optimization
  - Bilevel Optimization
  - JAX
  - Numerical Analysis
date: '2025-01-05'

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption: Convergence trajectory of a gradient-based multi-objective solver.
  focal_point: Smart

url_code: 'https://github.com/marcosmrai/jaxmoo'
url_pdf: ''
url_slides: ''
url_video: ''

slides: ''
---

This project addresses the fundamental mathematical challenge of optimizing vector-valued functions without reducing them to a single scalar objective a priori. The core research question is: **how do we define and efficiently follow a descent direction when objectives conflict?**

While scalar optimization relies on setting the gradient to zero, multi-objective optimization operates under the **Karush-Kuhn-Tucker (KKT)** conditions for Pareto optimality. Our research focuses on developing rigorous, efficient algorithms to reach these stationary points in continuous, differentiable spaces.

### Key Research Topics:

* **Descent Directions:** Developing algorithms that extend the concepts of Steepest Descent and Newton's method to multiple objectives, solving the quadratic subproblems required to find common descent vectors.
* **Bilevel Optimization:** Investigating theoretical properties and solvers for hierarchical problems (Stackelberg games), where one optimization problem is embedded within the constraints of another.
* **Pareto Front Approximation:** Creating methods to efficiently map the continuous manifold of optimal solutions, rather than finding just a single point.
* **JAX Implementation:** Leveraging Just-In-Time (JIT) compilation and automatic differentiation to implement these mathematical concepts in the **`jaxmoo`** library, providing a low-level, high-performance foundation for researchers.