---
title: Reasoning Distillation and Structural Alignment for Improved Code Generation
date: '2025-01-01'
authors:
- Amir Jalilifard
- Anderson de Rezende Rocha
- M. M. Raimundo
publication_types:
- '2'
publication: arXiv.org
abstract: 'Effective code generation with language models hinges on two critical factors:
  accurately understanding the intent of the prompt and generating code that applies
  algorithmic reasoning to produce correct solutions capable of passing diverse test
  cases while adhering to the syntax of the target programming language. Unlike other
  language tasks, code generation requires more than accurate token prediction; it
  demands comprehension of solution-level and structural relationships rather than
  merely generating the most likely tokens. very large language model (VLLM) are capable
  of generating detailed steps toward the correct solution of complex tasks where
  reasoning is crucial in solving the problem. Such reasoning capabilities may be
  absent in smaller language models. Therefore, in this work, we distill the reasoning
  capabilities of a VLLM into a smaller, more efficient model that is faster and cheaper
  to deploy. Our approach trains the model to emulate the reasoning and problem-solving
  abilities of the VLLM by learning to identify correct solution pathways and establishing
  a structural correspondence between problem definitions and potential solutions
  through a novel method of structure-aware loss optimization. This enables the model
  to transcend token-level generation and to deeply grasp the overarching structure
  of solutions for given problems. Experimental results show that our fine-tuned model,
  developed through a cheap and simple to implement process, significantly outperforms
  our baseline model in terms of pass@1, average data flow, and average syntax match
  metrics across the MBPP, MBPP Plus, and HumanEval benchmarks.'
featured: false
projects:
- machine-learning-opt
links:
- name: Semantic Scholar
  url: https://www.semanticscholar.org/paper/355d485c65b62ed2a6c103bd5429e1ccd5e292a6
url_pdf: ''
---
