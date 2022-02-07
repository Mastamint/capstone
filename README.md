# Meal Planner

## Project Overview

Tired of those meal plans that have strict conditions on what to eat, those that have weird foods in them that are too expensive for you, or you just want a recipe based off some leftovers you have in the fridge? Look no further! Meal Planner is what you need!

Meal Planner is an application used to select recipes based on whatever criteria you wish and then add that recipe to your meal plan. It's useful for those who want to organize their day and easily follow a plan of their own, or those that just want to search up some recipes to get some ideas. Meal Planner is here to help you search up recipes based off of a variety of parameters. Want to search up a recipe using zuccini? Meal Planner has a recipe for it. Want to search a recipe with a certain amount of calories or macros? Meal Planner can do it. Do you not like meat, or are allergic to certain things? Meal Planner can exclude that. You want to just look up random recipes and see what shows up? MEAL PLANNER CAN DO IT! 

Meal Planner is built in Django and Vue. It uses the Spoonacular API and the CSS Bulma framework to give the user recipes to choose from.

## Features

> A **user** can **generate a daily or weekly meal plan** with the ability to **specify caloric intake for each day**.
> A **user** can **search recipes with exclusions**, such as being allergic to shellfish or peanuts.
> A **user** will be able to **search random recipes** for inspiration! 

### Tasks

 - Learn and utilize the Spoonacular API
 - Allow user to create account and log in
 - Add ability for user to create a Meal Plan and edit recipes as needed
 - Save Plan into db

## Model

```
User: (username)
  Meal Plan for the day: (List of recipes with the ability to select each recipe and get the in-depth information such as ingredients needed, baking instructions, etc.)
  Total Calories: (int)
  Macros: (Total macros for the day)  
  Meal Plan for tomorrow: (List of recipes, or function to create one if blank)
  
Create/Edit Meal Plan
  Remove certain recipes and replace them with others
  Search similar recipes
  Search substitutions for ingredients
  Create new meal plan for the following day/week
```

## Schedule

### Week 1
  - Create django project
  - Create models
  - Learn Spoonacular API
  - Find a CSS framework
 
### Week 2
  - Generate a meal plan
  - Create search function and edit the plan
  - Save Plan to db
  - Set up basic functionality of the page

### Week 3
  - Add ability for user to mark off each day as "complete"
  - Allow user to track calories/macros
  - Create calendar view for user to track each month
  - Prepare presentation

## Must/Should/Can/Won't Haves
### Must Haves 
  - Users
  - Calorie/Macro Tracking
  - Edit functionality
  - Spoonacular API implementation

### Should Haves
  - Good CSS
  - Ability to look up similar recipes
  - Search functionality for diet, price, calorie, macro, etc.
 
### Can Haves
  - Charts to make the calories/macros look pretty

### Won't Haves
  - (Placeholder, Don't know yet!)
