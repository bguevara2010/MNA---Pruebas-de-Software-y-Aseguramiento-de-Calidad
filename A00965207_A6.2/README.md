A00965207_A6.2

Reservation System implemented in Python.

Overview

This project implements a Reservation System composed of three core
entities:

-   Hotel
-   Customer
-   Reservation

Persistent storage is managed using JSON files. The system includes
error handling for invalid data and follows PEP8 coding standards.

------------------------------------------------------------------------

Project Structure

A00965207_A6.2/
│
├── src/
│ ├── hotel.py
│ ├── customer.py
│ ├── reservation.py
│ ├── storage.py
│
├── tests/
│ ├── test_hotel.py
│ ├── test_customer.py
│ ├── test_reservation.py
│
├── data/
├── docs/
│ └── A00965207_A6.2.pdf
│
├── README.md
├── requirements.txt
└── .gitignore

------------------------------------------------------------------------

Requirements

pip install -r requirements.txt

------------------------------------------------------------------------

Running Unit Tests

python -m unittest discover

------------------------------------------------------------------------

Code Coverage

coverage run -m unittest discover coverage report -m

Minimum required: 85% line coverage

------------------------------------------------------------------------

Static Code Analysis

Flake8

flake8 .

No warnings should be displayed.

Pylint

pylint src

Expected score: 9.5/10 or higher

------------------------------------------------------------------------

Version Control

This repository follows Conventional Commits standard:

-   feat:
-   test:
-   style:
-   refactor:
-   docs:
-   chore:

Final stable version is tagged as:

v1.0

------------------------------------------------------------------------

Version

Current stable version: v1.0
