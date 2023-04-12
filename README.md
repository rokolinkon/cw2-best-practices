# Best Practices
## Welcome
Welcome back again to another companion lab to the PowerPoint presentation! This part is considerably more _conceptual_ than the previous two labs we’ve done, which made much more sense to be hands-on considering they were all about learning the ins and outs of working with Git, but since there were some coding concepts in this one, too, and doing things is a good way to remember them, here we are! Fork this repository as usual, clone it to your local machine (if using the GitHub CLI, which will be optionally included throughout the lab, you can use `gh repo clone your-username/cw2-best-practices`), and if you’re using the web, make sure to have the GitHub page for the forked repository open.

---

## Branching
### Master Branch Protection
On the GitHub page for the new repository you forked, let’s set up protection for the `master` branch to ensure only quality code makes it into that branch (but mostly just as an example). Head over to the settings for your forked repository:

![image](https://user-images.githubusercontent.com/70546234/229968214-dd808672-31c3-4df9-97d4-7fd6c0386994.png)

Head down to the “Branches” section:

![image](https://user-images.githubusercontent.com/70546234/229971198-121e3e0d-a419-4224-bb82-285a2867a51b.png)

And add a branch protection rule:

![image](https://user-images.githubusercontent.com/70546234/229971290-fd860c0c-192f-414b-9658-6cd245a7fbb9.png)

And set it up for branch `master`, requiring a pull request before code can make it into this branch:

![image](https://user-images.githubusercontent.com/70546234/229971468-f8922b96-2558-432d-a49a-2efe5a7af17b.png)

In an ideal scenario, you’d be requiring approvals before the PR can be merged, but for this tutorial, since you’ll be merging your own pull requests (and GitHub won’t let you approve your own PRs), we’ll have to leave that un-checked. Click "Create," and you’ll no longer be able to force a push straight to the master branch:

![image](https://user-images.githubusercontent.com/70546234/229973052-d245586b-af5d-4b12-b33c-b9991c277bbd.png)

And when you try to push normally, you’ll get a warning:

![image](https://user-images.githubusercontent.com/70546234/229973109-45b3a695-9d61-4bf3-a10a-937030e1acdc.png)

So, to comply with this new rule, let’s make a new branch, for example… `git checkout -b dev && git push --set-upstream origin dev`. We’ll need this to make pull requests on later. 

### Feature Branching
For this exercise, let’s make a feature branch and call it `clean-code`, for a step later on. At the end, we will merge this back into `dev` and make a PR from `dev` to `master`.

## Card Tracking
Let’s create an Issue for a feature we’re about to add. On the GitHub page for your repository, click “Issues.”

![image](https://user-images.githubusercontent.com/70546234/230183191-681529ef-ee5d-4171-9f14-02a003b7643b.png)


Then "New issue"

![image](https://user-images.githubusercontent.com/70546234/230183343-448f771a-c527-401b-a86d-27fa07273854.png)

And add a title and description, plus give it the “enhancement” label.

![image](https://user-images.githubusercontent.com/70546234/230184409-e7d06650-23d7-45d3-a23f-542a8a8f8574.png)

And create the issue! Or, if you use the CLI, you can do this all in one command:<br>
`gh issue create --label enhancement -t <title> -b <body>`

![image](https://user-images.githubusercontent.com/70546234/230190022-95c816c9-1f25-4a04-864a-b3abba55d096.png)


## Clean Code
In the root of this repository is a file called `clean_code.py` with some code in it that is considerably _not_ clean. Still on our `clean-code` branch, refactor this file to better follow some PEP 8 standards:
### `fr`
- The method name should be descriptive—rename it to “from_roman”
> **Note**: To avoid having to rename every usage of a function or variable, most IDEs have a built-in “refactor” command—in VSCode, the keyboard shortcut is F2, and in PyCharm (and all JetBrains IDEs), it’s Shift + F6. Or, you can just right-click on the name of the variable or function and click “Rename” on VSCode, or hover over “Refactor” and click “Rename” on PyCharm.
- The parameter name is unclear for a possible user of this method—rename it from `n` to something like `roman_number` and add a type hint, `: str`, since we know this should be a string.
- Finally with the method signature, add a return-type hint—just after the parameters in parentheses, add ` -> int` before the colon so users know what type this method returns.
- Next, variables inside the method. Rename `rn` to `roman_numeral` and `r` to `return_value` (or `retval` for a more C-like look).
- Inside the loop signature, rename `i` to `index` and `c` to `character` so we can keep track of what’s what when we’re deep inside the method signature.
- Now that everything is renamed, a lot of spacing conventions are messed up. To make this more readable, let’s…
  - move `return_value = 0` to a new line and remove the semicolon
  - add a space between `index,` and `character` on line 3
  - reduce the complexity of the ternary operator on line 6 by splitting it into multiple lines:
    - Add a line break after `try:`
    - Move the ternary operator to a regular `if` statement and space it out by rearranging it like…
    	- ```py
       if roman_numeral[i+1] == ‘v’:
      		return_value += 4
       elif roman_numeral[i+1] == ‘x’:
      		return_value += 9
       else: return_value += 1
      ```