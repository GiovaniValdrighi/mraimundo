---
title: Exploring the Trade-off Between Model Performance and Explanation Plausibility
  of Text Classifiers Using Human Rationales
date: '2024-01-01'
authors:
- Lucas Resck
- M. M. Raimundo
- Jorge Poco
publication_types:
- '2'
publication: NAACL-HLT
abstract: Saliency post-hoc explainability methods are important tools for understanding
  increasingly complex NLP models. While these methods can reflect the model's reasoning,
  they may not align with human intuition, making the explanations not plausible.
  In this work, we present a methodology for incorporating rationales, which are text
  annotations explaining human decisions, into text classification models. This incorporation
  enhances the plausibility of post-hoc explanations while preserving their faithfulness.
  Our approach is agnostic to model architectures and explainability methods. We introduce
  the rationales during model training by augmenting the standard cross-entropy loss
  with a novel loss function inspired by contrastive learning. By leveraging a multi-objective
  optimization algorithm, we explore the trade-off between the two loss functions
  and generate a Pareto-optimal frontier of models that balance performance and plausibility.
  Through extensive experiments involving diverse models, datasets, and explainability
  methods, we demonstrate that our approach significantly enhances the quality of
  model explanations without causing substantial (sometimes negligible) degradation
  in the original model's performance.
featured: false
projects:
- machine-learning-opt
links:
- name: Semantic Scholar
  url: https://www.semanticscholar.org/paper/b64c50ae270d4949579f15d4a0501fbf91d9ab4d
url_pdf: ''
---
