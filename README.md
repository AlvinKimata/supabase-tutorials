**Supabase Tutorials Repository**
=====================================

This repository contains a collection of Python scripts that demonstrate the use of Supabase, a PostgreSQL database-as-a-service, in various scenarios.

**Table of Contents**
-----------------

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Scripts](#scripts)
	* [01_crud_example.py](#01_crud_examplepy)
	* [02_auth.py](#02_authpy)
	* [03_function.py](#03_functionpy)
4. [Environment Variables](#environment-variables)
5. [Getting Started](#getting-started)

**Introduction**
---------------

Supabase is a PostgreSQL database-as-a-service that provides a simple and intuitive API for interacting with your database. This repository contains a collection of Python scripts that demonstrate the use of Supabase in various scenarios, including CRUD (Create, Read, Update, Delete) operations, authentication, and function invocation.

**Prerequisites**
----------------

* Python 3.8 or later
* Supabase account with a PostgreSQL database
* `supabase` and `gotrue` libraries installed (`pip install supabase gotrue`)

**Scripts**
------------

### 01_crud_example.py

This script demonstrates basic CRUD operations on a Supabase database. It creates a new table, inserts a new row, reads the row, and updates the row.

### 02_auth.py

This script demonstrates authentication with Supabase using the `gotrue` library. It signs up a new user, signs in with a password, and prints the session token.

### 03_function.py

This script demonstrates the invocation of a Supabase function using the `supabase.functions()` method. It invokes a function named `hello-world` and prints the response.

**Environment Variables**
-------------------------

To run these scripts, you will need to set the following environment variables:

* `SUPABASE_URL`: the URL of your Supabase database
* `SUPABASE_KEY`: the API key for your Supabase database

You can set these variables in a `.env` file in the root of the repository, or in your operating system's environment variables.

**Getting Started**
-------------------

1. Clone this repository to your local machine.
2. Create a new Supabase account and database.
3. Set the `SUPABASE_URL` and `SUPABASE_KEY` environment variables.
4. Run the scripts using Python (e.g. `python 01_crud_example.py`).

Note: Make sure to replace the `credentials` dictionary in `02_auth.py` with your own email and password.