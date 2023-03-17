[![DOI](https://zenodo.org/badge/591152996.svg)](https://zenodo.org/badge/latestdoi/591152996)

# Gender Bias in Software Engineering: Analyzing Large Language Models

This repository serves as the online appendix for the paper "She Elicits Requirements and He Tests: Software Engineering Gender Bias in Large Language Models", which is to be presented at [MSR 2023](https://conf.researchr.org/home/msr-2023).

## Abstract

Implicit gender bias in software development is a well-documented issue, such as the association of technical roles with men. To address this bias, it is important to understand it in more detail. This study uses data mining techniques to investigate the extent to which 56 tasks related to software development, such as assigning GitHub issues and testing, are affected by implicit gender bias embedded in large language models. We systematically translated each task from English into a genderless language and back, and investigated the pronouns associated with each task. Based on translating each task 100 times in different permutations, we identify a significant disparity in the gendered pronoun associations with different tasks. Specifically, requirements elicitation was associated with the pronoun "he" in only 6% of cases, while testing was associated with "he" in 100% of cases. Additionally, tasks related to helping others had a 91\% association with "he" while the same association for tasks related to asking coworkers was only 52%. These findings reveal a clear pattern of gender bias related to software development tasks and have important implications for addressing this issue both in the training of large language models and in broader society.

## Contents

* [`tasks.txt`](tasks.txt): Contains all sentences used as input for the back-translation.
* [`llm-bias.py`](llm-bias.py): Contains the Python code that leverages the DeepL API to back-translate each sentence 100 times.
* [`output.txt`](output.txt): Displays the raw output.
* [`llm-bias.csv`](llm-bias.csv): Aggregates the results.

## Citation

If you would like to cite this paper, please use the following reference:

```
@inproceedings{treude2023software,
  title={She Elicits Requirements and He Tests: Software Engineering Gender Bias in Large Language Models},
  author={Treude, Christoph and Hata, Hideaki},
  booktitle={Proceedings of the 20th International Conference on Mining Software Repositories},
  year={2023}
}
```
