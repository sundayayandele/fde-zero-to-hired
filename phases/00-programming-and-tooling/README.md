<!-- GENERATED from CURRICULUM.md by scripts/build.py. Do not edit by hand: edit CURRICULUM.md, then run `python scripts/build.py`. -->

# Phase 0: Programming and tooling (weeks 1–4)

[Home](../../README.md) · [Phase 1: Software engineering and ML foundations](../01-swe-and-ml-foundations/README.md) →

The goal is to write clean, tested Python, ship a small web API to the cloud, and explain how a neural network learns. Every FDE posting treats this as assumed, not taught.

| Week | Topic | What you do |
| --- | --- | --- |
| 1 | Python basics | Types, control flow, functions, files, errors. Solve 20 small exercises. |
| 2 | Python for real work | Classes, modules, virtual environments, `pip`/`uv`, typing, `pytest`. |
| 3 | Developer tooling | Git and GitHub (branches, PRs), Linux shell, VS Code, Docker basics. |
| 4 | Data handling | JSON, CSV, SQL (SELECT, JOIN, GROUP BY), pandas, calling REST APIs with `httpx`. |

**Resources:** Harvard CS50P (Python), *The Missing Semester* (MIT, shell and Git), SQLBolt.

**Code:** start with [fde-00-programming-starter](https://github.com/sundayayandele/fde-00-programming-starter) and complete the exercises in `labs/` week by week. The reference solution, [fde-00-programming](https://github.com/sundayayandele/fde-00-programming), is a tested complaint-ingestion pipeline and CLI over the US CFPB complaints data, with SQLite, Postgres and a report API. Open it only after you have tried each exercise.

**Exit check:** a public GitHub repo with a tested command-line tool that pulls data from a public API, stores it in SQLite and prints a report. CI runs the tests on every push.

## Watch

Optional short videos for each week, all in English with English captions. Moodle learners get them embedded on a Watch page per week.

### Week 1: Python basics

- [Python in 100 Seconds](https://www.youtube.com/watch?v=x7X9w_GIm1s) · Fireship · 2 min. A two-minute map of what Python is and why it is the language of ML work.
- [Python Tutorial for Beginners 6: Conditionals and Booleans - If, Else, and Elif Statements](https://www.youtube.com/watch?v=DZwmZ8Usvnk) · Corey Schafer · 17 min. if, elif, else and Boolean logic: the decisions every program makes.
- [Python Tutorial for Beginners 8: Functions](https://www.youtube.com/watch?v=9Os0o3wzS_I) · Corey Schafer · 22 min. Functions, arguments and return values: how to break a problem into reusable pieces.
- [Python Tutorial: File Objects - Reading and Writing to Files](https://www.youtube.com/watch?v=Uh2ebFW8OYM) · Corey Schafer · 25 min. Reading and writing files safely with context managers.
- [Python Tutorial: Using Try/Except Blocks for Error Handling](https://www.youtube.com/watch?v=NIWwJbo-9_8) · Corey Schafer · 11 min. try and except: handling errors instead of crashing.

### Week 2: Python for real work

- [Python OOP Tutorial 1: Classes and Instances](https://www.youtube.com/watch?v=ZDa-Z5JzLYM) · Corey Schafer · 15 min. Classes and instances: the basis of most Python libraries you will use.
- [Python Tutorial for Beginners 9: Import Modules and Exploring The Standard Library](https://www.youtube.com/watch?v=CqvZ3vGoGs0) · Corey Schafer · 22 min. Importing modules and finding your way around the standard library.
- [Python Tutorial: UV - A Faster, All-in-One Package Manager to Replace Pip and Venv](https://www.youtube.com/watch?v=AMdG7IjgSPM) · Corey Schafer · 27 min. uv: one fast tool for Python versions, virtual environments and dependencies.
- [Python Tutorial: Type Hinting vs Type Checking vs Data Validation - What’s the Difference?](https://www.youtube.com/watch?v=fM4O9bModsE) · Corey Schafer · 18 min. Type hints vs type checking vs data validation, and when you need each.
- [getting started with pytest (beginner - intermediate) anthony explains #518](https://www.youtube.com/watch?v=mzlH8lp4ISA) · anthonywritescode · 13 min. Getting started with pytest, from one of its maintainers.

### Week 3: Developer tooling

- [How Git Works: Explained in 4 Minutes](https://www.youtube.com/watch?v=e9lnsKot_SQ) · ByteByteGo · 4 min. How Git stores your work, in four minutes, so the commands make sense.
- [How to create a pull request in 4 min | GitHub for Beginners](https://www.youtube.com/watch?v=nCKdihvneS0) · GitHub · 4 min. Opening a pull request, the way every team reviews code (official GitHub).
- [60 Linux Commands you NEED to know (in 10 minutes)](https://www.youtube.com/watch?v=gd7BXuUQ91w) · NetworkChuck · 11 min. The Linux commands you will use daily on servers and in containers.
- [Getting Started with Python in VS Code (Official Video)](https://www.youtube.com/watch?v=D2cwvpJSBX4) · Visual Studio Code · 10 min. Setting up VS Code for Python (official Visual Studio Code).
- [100+ Docker Concepts you Need to Know](https://www.youtube.com/watch?v=rIrNIzy6U_g) · Fireship · 9 min. The Docker ideas you need: images, containers, volumes, networks, Compose.

### Week 4: Data handling

- [Python Tutorial: Working with JSON Data using the json Module](https://www.youtube.com/watch?v=9N6a-VLBa2I) · Corey Schafer · 21 min. Reading and writing JSON, the format every API speaks.
- [Learn Basic SQL in 15 Minutes | Business Intelligence For Beginners | SQL Tutorial For Beginners 1/3](https://www.youtube.com/watch?v=kbKty5ZVKMY) · Adam Finer - Learn BI · 18 min. SELECT, WHERE and ORDER BY: the SQL you need in fifteen minutes.
- [SQL Joins Explained  |¦| Joins in SQL |¦| SQL Tutorial](https://www.youtube.com/watch?v=9yeOJ0ZMUYw) · Socratica · 10 min. How SQL joins combine tables.
- [SQL Group By: An Explanation and How To Use It](https://www.youtube.com/watch?v=x2_mOJ3skSc) · Database Star · 5 min. GROUP BY and aggregates: turning rows into summaries.
- [Learning Pandas for Data Analysis? Start Here.](https://www.youtube.com/watch?v=DkjCaAMBGWM) · Rob Mulla · 23 min. pandas for loading, cleaning and exploring tabular data.
- [HTTPX Tutorial - A next-generation HTTP client for Python](https://www.youtube.com/watch?v=qAh5dDODJ5k) · Patrick Loeber · 11 min. Calling REST APIs from Python with httpx.

### Want more depth? (longer, optional)

- [Harvard CS50’s Introduction to Programming with Python – Full University Course](https://www.youtube.com/watch?v=nLRL_NcnK-4) · freeCodeCamp.org · 16.0 h. Harvard CS50P, the full course behind this phase. Long: use it for any week you want more depth.
- [Lecture 1: Course Overview + Introduction to the Shell](https://www.youtube.com/watch?v=MSgoeuMqUmU) · Missing Semester · 75 min. MIT Missing Semester, lecture 1: the shell and the tools courses usually skip.

---

[Home](../../README.md) · [Phase 1: Software engineering and ML foundations](../01-swe-and-ml-foundations/README.md) →
