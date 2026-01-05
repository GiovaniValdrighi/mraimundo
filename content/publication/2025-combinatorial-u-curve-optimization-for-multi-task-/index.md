---
title: 'Combinatorial U-Curve Optimization for Multi-Task Learning: A Task Selection
  Approach'
date: '2025-01-01'
authors:
- G. K. Bonás
- Marcelo S. Reis
- M. M. Raimundo
publication_types:
- '2'
publication: IEEE International Joint Conference on Neural Network
abstract: Multi-task learning (MTL) is an approach where a single model learns multiple
  tasks simultaneously, potentially reducing overfitting and speeding up the learning
  process. However, selecting the right combination of tasks is crucial to avoid negative
  transfer, where learning additional tasks might hinder rather than enhance performance.
  Research has explored task relationships through shared data samples, features,
  relational knowledge, and parameters. However, sharing relational knowledge, features,
  or parameters often requires domain knowledge, potentially introducing artificial
  connections between unrelated tasks. This paper presents an MTL algorithm based
  on combinatorial U-curve optimization, focusing on data sample sharing. It uses
  a branch-and-bound-based approach to identify beneficial source tasks without requiring
  prior domain knowledge. The method organizes tasks into a tree, optimizing selection
  with backtracking and pruning for efficient exploration and minimal negative transfer.
  Results on synthetic and real-world datasets show that our algorithm is competitive
  with more sophisticated MTL frameworks such as Logistic L21, Dirty, and rMTFL, while
  maintaining a simpler design and fewer assumptions. In the Spam (Landmine) dataset,
  our algorithm yielded a mean loss that was 45% (62%) of the mean loss yielded by
  the second-best approach, Logistic Dirty (Logistic rMTFL). Although numerical improvements
  over these baselines are not always large, the proposed approach consistently matches
  or slightly outperforms them in most tasks, demonstrating robust performance even
  in scenarios with limited data or outliers.
featured: false
projects:
- machine-learning-opt
links:
- name: Semantic Scholar
  url: https://www.semanticscholar.org/paper/30b0831fdf78503e9b404e1b632e6ae5becfe163
url_pdf: ''
---
