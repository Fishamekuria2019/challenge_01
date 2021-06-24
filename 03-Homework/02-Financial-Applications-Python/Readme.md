# Application

## Challenge: Python Loan Qualifier Application

![A wooden balance scale weighs a burlap bag labeled "Loan" on one side and cutout image of a house on the other side.](Images/loan_image.png)

### Background

You’re progressing in your role as an application developer at a fintech lending startup. The lending software that you’ve built so far has been a big success for the company. As part of that success, you’ve been meeting a lot with the BizOps team to discuss creating additional useful features.

At a recent meeting, a new must-have feature request emerged. Specifically, BizOps wants to know if your software can prompt the user to save the qualifying loans as a new CSV file.

This project is a great way to show off your new software engineering skills, so congratulations on this opportunity!

### What You're Creating

You will apply software engineering best practices to create new features and enhancements for a loan qualifier application. Specifically, you'll do the following:

1. Create a GitHub repository.

2. Translate new business requirements to code for adding a function to save loans.

3. Organize your code for the changes to the `fileio` module.

4. Update the CLI to add additional dialogs for loan output.

5. Write new tests for the functionality to save loans.

6. Update the documentation to reflect your new functions and operations.

In addition, your project should be based on the user story and acceptance criteria outlined here.

#### User Story

As a user, I need the ability to save the qualifying loans to a CSV file so that I can share the results as a spreadsheet.

#### Acceptance Criteria

* Given that I am using the loan qualifier command-line interface (CLI), when I run the qualifier, then the tool should prompt the user to save the results as a CSV file.

* Given that there are no qualifying loans, when prompting a user to save a file, then the program should notify the user and exit.

* Given that I have a list of qualifying loans, when I am prompted to save the results, then I should be able to opt out of saving the file.

* Given that I have a list of qualifying loans, when I choose to save the loans, the tool should prompt for a file path to save the file.

* Given that I am using the loan qualifier CLI, when I choose to save the loans, then the tool should save the results as a CSV file.

### Files

[Qualifier Starter Code](Challenge/Starter_Code.zip)

### Instructions

This assignment is broken into the following parts:

1. Version Control: Create the Project Repository

2. Software Requirements: Translate Business Requirements to Code

3. System Design: Organize Your Code

4. Usability: Update the CLI

5. Testing and Debugging: Write New Tests

6. Documentation: Update All of the Docs

#### Version Control: Create the Project Repository

In this section, you'll create the GitHub repository for your project. Use the starter code provided to initialize your repository. Don't forget the README.md! You'll need to update this as you develop your code.

Complete the following steps:

1. Create a new GitHub repository.

2. Add your README.md file and `.gitignore`.

3. Commit your project files.

> **Pro Tip** Remember GitHub best practices—commit and push your updates to the repo frequently and with detail!

#### Software Requirements: Translate Business Requirements to Code

In this section, you'll translate the high-level business requirements into functional code.

In `app.py`, write a function named `save_csv()` that uses the `csv` library to save the qualifying data as a file.

> **Hint** Don't worry about the user dialog at the moment. Just focus on the code that saves the qualifying loan data as a CSV file. Try writing this directly in `app.py` initially. Once this is working, we can refine the overall design in the systems design step.

#### Systems Design: Organize Your Code

Now that you have the `save_csv()` code working, the next step is to refine the systems design.

This is where you should consider the overall architecture and design of your system. Think about the purpose of this function. Look for a location that best represents the functionality, organization, and use of the new code.

Complete the following steps:

1. Integrate your new `save_csv()` function into the existing loan qualifier application.

2. Update the function and module docstrings for the new feature.

> **Pro Tip** Remember the rule of DRY: whenever you find yourself repeating code, make sure to separate it out and import it where you need it. This will save you lots of time in the future and make your code reusable.

#### Usability: Update the CLI

Now that you've impressed your fellow developers with great systems design, you need to improve the usability for the not-so-technical users, so that they can access and save their qualifying loans to a CSV.

You'll need to add a new save dialog to the existing CLI, by completing the following steps:

1. In `app.py`, create a new function named `save_qualifying_loans()` that accepts the list of qualifying loans.

2. Inside the new `save_qualifying_loans()` function, create the user dialog to prompt the user for whether or not they would like to save their qualifying loans. Use Questionary to prompt the user with `.confirm().ask()`.

3. Inside the `save_qualifying_loans()` function, create the user dialog for the save CSV function. Use Questionary to prompt the user and ask for the output file path.

Be sure to test this out and think about how a user will interact with your CLI.

#### Test and Debug: Write New Tests

To ensure software quality and future stability of the codebase, you'll also want to update the unit tests to include this new feature.

Take some time to think about this from a user's perspective. What are the edge cases for this new code? Is there anything that a user might try to do that would cause the program to crash?

Consider the following acceptance criteria:

> Given that I am using the loan qualifier CLI, when I choose to save the loans, then the tool should save the results as a CSV file.

Create a new test called `test_save_csv` to ensure that the `fileio` code can successfully write to a CSV file at a particular path.

> **Hint** Use `Path('/path/to/output.csv').exists()` with PyTest `assert` to determine whether the file was successfully created.
>
> To learn more, read the [Python documentation on exists()](https://docs.python.org/3/library/pathlib.html#pathlib.Path.exists).

#### Extension

If you're up for an extra challenge, add `test_filters` to test that your `filters` properly remove institutions that specific input should eliminate. Try to test each individual filter!

#### Documentation: Update All of the Docs

Update your GitHub repository README.md to document the new features of your code.

The updated README.md should include a description and usage examples of this new functionality. This will make it easier for you and any developers working on the project to keep track of all the features that are now available in the software. It also shows that you're capable of writing professional-level documentation. This will help you attract other project collaborators and might catch the attention of a hiring manager!

Congratulations on completing your fintech software engineering project! You've turned business requirements into real-world code, tested your application, written professional-grade documentation, and managed a repo. These are all things developers do on a daily basis. All you need now is to keep on coding!

### Requirements

#### Initialize and Design (20 points)

To receive all points, your analysis must fulfill the following criteria:

 * Version Control: Create the Project Repository

   * Challenge repository initialized with starter code. _(5 points)_

   * README.md added and updated. _(5 points)_

 * Requirements: Translate Business Requirements to Code

   * Business requirements translated to code. _(5 points)_

 * System Design: Organize your Code

   * Code organized and integrated into the existing project. _(5 points)_

#### Development, Testing, and Deployment (30 points)

To receive all points, your code must fulfill the following criteria:

 * Usability: Update the CLI

   * Save dialog added to existing command-line interface. _(15 points)_

 * Testing and Debugging: Write New Tests

   * `test_save_csv` performs expected test. _(15 points)_

   * Optional: `test_filters` performs expected test. _(10 points)_

#### Documentation: Update All of the Docs (20 points)

To receive all points, your code must fulfill the following criteria:

 * Include documentation that contains all or most of the sections from the README template.  _(10 points)_

 * Have clear and concise documentation updated to reflect the current state of your project and it's features. _(5 points)_

 * Include rich documentation content such as example usage screenshots and code blocks that demonstrate the application.  _(5 points)_

#### Coding Conventions and Formatting (10 points)

To receive all points, your code must fulfill the following criteria:

 * Move imports to the top of the file, just after any module comments and docstrings, and before module globals and constants. _(3 points)_

 * Name functions and variables with lowercase characters, with words separated by underscores. _(2 points)_

 * Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code. _(3 points)_

 * Use concise logic and creative engineering where possible. _(2 points)_

#### Deployment and Submission (10 points)

To receive all points, your files should fulfill the following criteria:

 * Be contained in a repository cloned to your local machine. _(4 points)_

 * Have been added to the repo using the command line. _(3 points)_

 * Contain appropriate commit messages. _(3 points)_

#### Comments (10 points)

 * To receive all points, your code should be well commented with concise, relevant notes that can be understood by another developer. _(10 points)_

---

### Submission

To submit your challenge assignment, click Submit, then provide the URL of your GitHub repository for grading.

> **Note** You're allowed to miss up to two Challenge assignments and still earn your certificate. If you complete all Challenge assignments, your lowest two grades will be dropped. If you wish to skip this assignment, click Submit, then indicate that you're skipping by typing “I choose to skip this assignment” in the text box.

---

## Career Connection

![Career Services Logo](Images/cs_logo.png)

Welcome to your second Career Connection! We hope you’ve enjoyed digging into the wonderful world that is Python—it can be overwhelming at first, but it’s an incredibly important skill for your career in fintech. Python is also one of the most dynamic skills you'll learn in this course, as it can be used in so many different ways.

Let’s talk a little about how Python will be useful to you in the future. Python is used across many financial and fintech sectors, including the following:

* Banking

* Insurance

* Payments

* Trading

* Lending

Companies use Python for everything from web development to machine learning. Within fintech, there's a significant demand for technologists who can use Python to automate tasks, build financial applications, perform analysis, and develop data science and machine-learning tools. With Python, you can do all of these things!

### Python and Fintech

This is why you’re here, right? Fintech. Python’s versatility and extensive package library lends itself to financial technologies. It can be used for a wide range of tasks, like financial analysis, financial data visualization, and machine learning. Over the next few months, you’ll learn how to do all of these and more.

But what is the demand for Python skills? The [Stack Overflow Developer Survey](https://insights.stackoverflow.com/survey/2020#technology-programming-scripting-and-markup-languages-all-respondents) showed that Python was the fourth most popular technology, behind JavaScript, HTML/CSS, and SQL. Now, considering that Python is used for completely different tasks than those other three, it's arguably the most popular scripting language you can learn!

Additionally, respondents rated it as one of the most loved languages to use, coming in just behind Rust and TypeScript. It was also the number-one most wanted language—the language the most developers expressed interest in using—beating out even JavaScript!

### Python Technical Interview Preparation

As you progress through the boot camp, you’ll learn how to apply Python to a wide range of financial analysis topics. One of the most important skills is using the versatility of Python to solve algorithmic problems. Employers often use sites like [HackerRank](https://www.hackerrank.com/) or [CodeSignal](https://codesignal.com/) to test these skills.

Sign up for one or both of these platforms to explore their practice opportunities.

### Activity: Pseudocoding

The ability to code is only one part of the technical interview process. Prospective employers will often ask you to write out the logic, or steps, to solve a coding problem. This is often referred to as **pseudocode**—because the solution is written in plain language that other people can understand, and it doesn't have to follow the syntax of the coding language.

Watching you pseudocode can help employers see how you work through a problem. But don't sweat it too much! Pseudocoding is easier than writing working code, because you don't have to get bogged down in the coding syntax.

#### Files

The following zip file contains the starter code you'll need for this activity.

[Starter Code](Activities/01_Pseudocoding.zip)

### Instructions

1. From the Unsolved folder, Copy and paste the `count_the_vowels.txt` file into your IDE (VS Code).

2. Practice writing pseudocode for a function that does the following:

* The function that takes a string input: `str`.

* The function returns the number, or count, of vowels in the input string.

    > **Hint** For the purpose of this activity, count the letters A, E, I, O, and U as vowels.
    >
    > Also, the input string will consist of lowercase letters.

    ```python
    def count_the_vowels(str):
      # @TODO: Your pseudocode here!
    ```

### Pseudocode Solution

```python
def count_the_vowels(str):
    # initialize a counter variable to 0
    # loop through each character in the string
        # if the char matches one of the vowels in uppercase of lowercase
        # increment counter by one
    # return the counter
```

### Python Solution

```python
def count_the_vowels(str):
    ## initialize a counter variable to 0
    num_vowels = 0
    ## loop through each character in the string
    for char in str:
        ## if the char matches one of the vowels in uppercase or lowercase
        if char in "aeiouAEIOU":
            ## increment counter by one
            num_vowels = num_vowels + 1

    ## return  the  counter
    return num_vowels
```

### Continue to Hone Your Skills

![Career Services Online Events banner](Images/online-events.png)

To learn more about the technical interviewing process and practice algorithms in a mock-interview setting, attend one of our [upcoming workshops](https://careerservicesonlineevents.splashthat.com/).
