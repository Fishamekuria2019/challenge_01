# Building an ATM Application

Before writing any code for a new software application, a developer must first understand what that application will be expected to do.

With that in mind, let's develop the user stories associated with a basic ATM application.

## Structure of a User Story

A user story is a concise description of a software requirement from the perspective of the person who desires that feature. User stories adhere to the following three-part template:

> As a [type of user], I want [some goal] so that [some reason].

  * **As a [type of user]:** This part refers to the person or role who requires the new feature.

  * **I want to [some goal]:** In this part of the template, you need to express what the user is trying to achieve. This statement should be free of technology implementation details.

  * **So that [some reason]:** This part of the template will help you prioritize features by reframing the benefit the user wants to gain in terms of the bigger picture of the problem solved. If you can't write this part of the user story, you might consider omitting this feature.


## ATM User Stories

Think of the ATM application in terms of its user stories.

> “Think of an ATM machine. Applying user stories as the framework for the business needs and software requirements, what basic functions do all ATM machines perform?”

Create the following ATM user stories:

* As a user of an ATM, I: **input my PIN for identification.**

* As a user of an ATM, I: **identify whether I’m going to make a deposit or withdrawal.**

* As a user of an ATM, I: **input the amount of my deposit or withdrawal.**

* As a user of an ATM, I: **receive cash...not going to dispense cash here (sorry!!)**

* As a user of an ATM, I: **want to receive my adjusted account balance.**

## ATM Software Requirements:

Software developers must also be aware of software and compliance requirements ahead of the development process.

Specify any compliance or validation requirements that should be associated with basic ATM functionality:

* Verify that the PIN is valid.

* Validate that the deposit or withdrawal amount is a positive number.

* Verify that there are enough funds in the account to cover the withdrawal.

With these user stories and system requirements in mind, we can start to convert the specifications into code.
