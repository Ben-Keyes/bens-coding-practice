# 🚀 bens-coding-practice

![Build Status](https://github.com/Ben-Keyes/bens-coding-practice/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/github/license/Ben-Keyes/bens-coding-practice)

Hiya! Welcome to **my coding practice repository**.  
Here, I tackle coding challenges like [LeetCode](https://leetcode.com) and [CodingBat](https://codingbat.com), plus other fun practice projects.

This repo is also connected to my personal Jira Board, *Beelzebub* (aka Bennie & Lucky), for tracking workflow and progress.
<img width="1082" height="506" alt="image" src="https://github.com/user-attachments/assets/c9b9ff7c-e093-41ab-9665-03957ff7073b" />
*This Jira board helps me organize tasks, track progress, and manage code challenges systematically.*


## How to Use

Clone the repo:

```bash
git clone https://github.com/Ben-Keyes/bens-coding-practice.git
```

Run all tests with:
```bash
pytest
```

## Code Style & Testing Notes
- Methods are implemented as instance methods to follow common coding challenge conventions and to facilitate testing with pytest fixtures, even when they could be refactored as static methods because they don't use instance state.
- Tests use pytest fixtures and standard conventions to demonstrate good testing practices.
