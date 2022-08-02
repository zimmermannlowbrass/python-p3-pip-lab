# Environment Lab

## Learning Goals

- Use pipenv to set up a virtual environment
- Install libraries using pipenv

***

## Key Vocab

- **Package** is a bundle of software to be installed.
- **Repository** storage location for software packages


***

## Introduction

In this lab we will create a virtual environment using pipenv with a
specific python version and libraries.

***

## Instructions

- Using the command `pipenv --python 3.9.2`, set up a virtual environment using python 3.9.2.
- Using the `pipenv install` command install these versions of the following libraries
 `requests==2.25.0` and `pytest==5.4.2`

Run `pipenv shell` to enter the virtual environment. Then run
`pytest -x` to run your tests.

Once all of your tests are passing, commit and push your work using `git` to
submit.

***

## Conclusion

Virtual environments allow us to have a deterministic and predictable
 runtime for our python projects. You can apply what we learned in
 this exercise to make sure you have the right environment to
 run your python code in for your future projects.
***

## Resources

- [Pip env](https://pipenv.pypa.io/en/latest/basics/)
- [PYPI](https://pypi.org/)