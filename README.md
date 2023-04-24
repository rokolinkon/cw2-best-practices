# Best Practices
## Welcome
Welcome back again to another companion lab to the PowerPoint presentation! This part is considerably more _conceptual_ than the previous two labs we’ve done, which made much more sense to be hands-on considering they were all about learning the ins and outs of working with Git, but since there were some coding concepts in this one, too, and doing things is a good way to remember them, here we are! Fork this repository as usual, clone it to your local machine (if using the GitHub CLI, which will be optionally included throughout the lab, you can use `gh repo clone your-username/cw2-best-practices`), and if you’re using the web, make sure to have the GitHub page for the forked repository open.

---
# Section 1: Setup

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

# Section 2: Refactoring

## Clean Code
In the root of this repository is a file called `clean_code.py` with some code in it that is considerably _not_ clean. Still on our `clean-code` branch, refactor this file to better follow some PEP 8 standards:
> **Note**: This code uses features added in Python version 3.10. It will fail to run on any Python version older than that.

### `fr`
- The method name should be descriptive—rename it to “from_roman”
> **Note**: To avoid having to rename every usage of a function or variable, most IDEs have a built-in “refactor” command—in VSCode, the keyboard shortcut is F2, and in PyCharm (and all JetBrains IDEs), it’s Shift + F6. Or, you can just right-click on the name of the variable or function and click “Rename” on VSCode, or hover over “Refactor” and click “Rename” on PyCharm.
- The parameter name is unclear for a possible user of this method—rename it from `n` to something like `roman_number` and add a type hint, `: str`, since we know this should be a string.
- Finally with the method signature, add a return-type hint—just after the parameters in parentheses, add ` -> int` before the colon so users know what type this method returns.
- Next, variables inside the method. Rename `rn` to `roman_numeral` and `r` to `return_value` (or `retval` for a more C-like feel).
- Inside the loop signature, rename `i` to `index` and `c` to `character` so we can keep track of what’s what when we’re deep inside the method signature.
Now that everything is renamed, a lot of spacing conventions are messed up. To make this more readable, let’s…
  - move `return_value = 0` to a new line and remove the semicolon
  - add a space between `index,` and `character` on line 3
  - reduce the complexity of the ternary operator on line 6 by splitting it into multiple lines:
    - Add a line break after `try:`
    - Move the ternary operator to a regular `if` statement and space it out by rearranging it like…
    ```py
       if roman_numeral[i+1] == ‘v’:
      		return_value += 4
       elif roman_numeral[i+1] == ‘x’:
      		return_value += 9
       else: return_value += 1
    ```
    - Repeat this change for every ternary operator, spacing them out and making them easier to read
> **Note**: On most IDEs, you can create multiple cursors by holding Alt/Option while clicking in another location that lets you type the same thing in both of those places at once. Everywhere you see a space that needs to be added, you can alt-click to add a cursor there, and then by just pressing spacebar one time, you can clean up all of them. Try it!
  - place spaces after every colon that introduces a one-liner code block (such as after `except IndexError:` and one-liner `if` statements)
  - place spaces around `+=` operators
The function should now look quite a bit longer, but significantly more readable. We’ll make the function shorter in a later step by refactoring out into methods, but for now, let’s move onto the next function.
### `to`
- Rename this function to `to_roman` to be consistent with the last, and rename the variable `n` to `arabic_number`
- Refactor the `if n<4000` and `if n>0` statements into _guard clauses_, significantly reducing indentation in the method and making it easier to read, otherwise known as “fail fast,” by flipping the booleans (`if n>4000` and `if n<0`) and moving the `else` clauses’ `raise` statements up to the beginning, meaning the function should start like…
```py
def to_roman(arabic_number):
	if arabic_number > 4000: raise ValueError("only numbers up to 3999 are supported")
	if arabic_number < 0: raise ValueError("only positive numbers are supported")
	# …
```
- Then, unindent the main code of the function by two tabs to be syntactically valid.
> **Note**: On most IDEs and code editors, you can do this by highlighting all the code you want to unindent and pressing Shift + Tab.
- Now, the main code of the function. It’s quite a mess as it stands—there are insane, unnecessary list comprehensions happening to build the tuples of numerals, and they’re all in one line with the indexing and ternary operators. A good rule to follow is that making _readable_ code is always better than showing off how complicated of list comprehensions you can write (although this was my opportunity to do so). Let’s split this up into multiple lines and assign some variables so we’re not doing everything inline.
  - Make four new lines under `r=str()` to assign variables, and add…
```py
thousands =
hundreds =
tens =
ones =
```
  - For each list comprehension, there’s a comment underneath showing a much more sensible way to assign these tuples that is much easier to read. Copy those and place them after the variable declarations, so it looks something like…
```py
thousands = ('', 'M', 'MM', 'MMM')
hundreds = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
tens = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')
ones = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')
```
  - Now, use those variables instead of the list comprehensions. Replace everything from `tuple(` to the index with the floor division with the variables you’ve created in respective order, while also adding spaces around the operators and keywords. It should look like…
```py
r += thousands[arabic_number//1000] if arabic_number > 999 else str()
r += hundreds[int((arabic_number//100).__str__()[-1])] if arabic_number > 99 else str()
r += tens[int((arabic_number//10).__str__()[-1])] if arabic_number > 9 else str()
r += ones[int(arabic_number.__str__()[-1])]
```
  - For better readability, convert all calls to `str()` into empty string literals, `""` or `''`.
  - Rename `r` to `return_value` or `retval`.
  - Finally, flip the ternary operator so we don’t need the `else ""`—put the `if arabic_number > 999:` calls in front of the additions, so they should look like `if arabic_number > 999: r += thousands[arabic_number//1000]`. This should save on both readability and performance time, as the interpreter won’t spend time concatenating empty strings to the return value.
The code is now much, much cleaner! Any given person could read it and understand what it’s doing and how it’s doing it—and it’s considerably easier to debug. But we’re not done with this code yet. It’s time for…

## Object-Orientation
Though this code doesn’t necessarily represent a real-world object, we can still push it toward being object-oriented by refactoring it a bit. First of all, these two functions are related enough to be methods inside the same class:
- At the top of the file, add a new line with a class declaration `class RomanNumeralConverter:`
- Select the two method definitions and indent them
- Add the `self` parameter as the first parameter to both methods
- Above the assertion at the bottom of the file, instantiate the class, `converter = RomanNumeralConverter()`
- Prefix the method calls with `converter.`
- Run the file to make sure no error is raised

Congratulations—this code is now object-oriented! That wasn’t so hard, right? But if you use an IDE with good Python linting, you may notice a squiggle under the methods with the `self` parameter you just added…

![image](https://user-images.githubusercontent.com/70546234/232331841-c4e1a416-31a5-4890-9e28-9d775c40e330.png)

This is because these two methods currently only have a tie to each other in terms of conceptual grouping—the linter claims they could be made _static_ because they don’t necessarily use any attributes of the class—instantiating the class to use the methods is pointless. So, instead of making these methods static, which defeats the purpose of object-orientation, let’s add a new feature to make them more a part of the object and less just a part of the class: caching!

### Adding a caching system
Of course, this will be a rather rudimentary cache and won’t make our script run a _ton_ faster, but it’ll be fun to do—and isn’t that what matters?

- Push down the method definitions in `RomanNumeralConverter` a few lines to give us some room to add some instance variables
- Add a constructor to initialize these variables:
```py
def __init__(self):
  self.roman_to_arabic_cache = {}
  self.arabic_to_roman_cache = {}
```
- Now, we have two cache variables to play with, and they were both initialized to empty dictionaries. Inside these dictionaries, we can store mappings of numerals we’ve already converted so that, if a user needs to convert the same thing again, we can pull from the cache instead of having to convert it anew every time.
- But we don’t want users manually modifying these caches—let’s make them private by adding a double underscore to the beginning of their names.
```py
self.__roman_to_arabic_cache = {}
self.__arabic_to_roman_cache = {}
```
- Now, we can add a system to let the user index the object they instantiate as though they were accessing the cache directly, using one of Python’s built-in “magic methods.”
```py
def __getitem__(self, item):
  if type(item) is str:
    return self.from_roman(item)
  elif type(item) is int:
    return self.to_roman(item)
  else: raise ValueError("Cannot subscript RomanNumeralConverter with '%s', expected 'str' or 'int'"%type(item))
```
- Now, we can put to use the `self` parameter of our methods. At the beginning of the `from_roman` method, between the assignments of `roman_numeral` and `return_value` add a check into the cache:
```py
# …
roman_numeral = roman_number.lower()
if roman_numeral in self.__roman_to_arabic_cache.keys():
    return self.__roman_to_arabic_cache[roman_numeral]
return_value = 0
# …
```
- At the bottom of the method, save the return value into the cache before returning it:
```py
# …
    case _: raise ValueError("only numerals IVXLCDM are supported")
self.__roman_to_arabic_cache[roman_numeral] = return_value
return return_value
```
- And do the same for the `to_roman` method—add a check into the cache after the guard clauses:
```py
# …
if n < 0: raise ValueError("only positive numbers are supported")
if arabic_number in self.__arabic_to_roman_cache.keys():
    return self.__arabic_to_roman_cache[arabic_number]
return_value = ""
```
- And save values into the cache after converting them
```py
# …
return_value += ones[int(arabic_number.__str__()[-1])]
self.__arabic_to_roman_cache[arabic_number] = return_value
return return_value
```

### A simple main method
- Now, to illustrate usage of an object-oriented class, we’ll make a simple main method to test it out.
- Remove the assertion down at the bottom, and in its place, add `if __name__ == "__main__":`
> `if __name__ == “__main__”` is a Python convention to determine the entry-point in a program. This prevents code from being run on import, and if it’s present in a script, lets readers of the code know that it can be run.
- Under that, add an infinite loop until the user manually breaks out so the cache can take effect, with some code to get the input and print out the results…
```py
converter = RomanNumeralConverter()
while True:
    number = input("Input a number to convert or ‘q’ to quit\n>> ")
    if number == 'q': break
    print(converter[number])
```

# Section 3: Merging

## Merging changes back into the master branch

### Merge `clean-code` back into `dev`
And now the branches from earlier come back! Just as mentioned at the very beginning, merge `clean-code` back into our intermediary branch, `dev`: `git switch dev && git merge clean-code`.

### Make a pull request

Since we set up branch protection on GitHub, we’ll have to merge our changes back into `master` via a _pull request_. To make one on the web…
- On the GitHub page of your repository, click “Pull Requests”

![image](https://user-images.githubusercontent.com/70546234/234106571-65e509fb-0433-46df-96c7-fecd8ddcc554.png)

- Then “New pull request”

![image](https://user-images.githubusercontent.com/70546234/234106787-b3ccb413-5f7a-4e4d-9643-e19488f82b7e.png)

- Select the `dev` branch as the compare

![image](https://user-images.githubusercontent.com/70546234/234106873-133b5696-6ee9-492c-9260-b21113da91aa.png)

- Write a good description, and include a _closing keyword_ for the issue we created earlier, as this pull request fixes that issue. Here, I used “resolves #1,” but other valid keywords include “fixes” and “closes.”

![image](https://user-images.githubusercontent.com/70546234/234107177-c8d91e99-60a7-4cbd-986d-e3ccfe2d2abd.png)

- Create the pull request, merge it, and we’re done! Notice that issue #1 should now be closed.

Or, do this all via the GitHub CLI, while on the `dev` branch:

`gh pr create -t "refactoring changes" -b "also adds a caching system and closes #1"`

![image](https://user-images.githubusercontent.com/70546234/234109648-1f7f75cb-361f-42ba-9798-48042dc9b5fe.png)

… and to merge it …

`gh pr merge -t "merge commit text"`

![image](https://user-images.githubusercontent.com/70546234/234109835-34acc7da-da63-40d8-9188-8ee6e861c20b.png)


## Congrats!
Hey, you’ve reached the end! Hopefully this was helpful—it is considerably more conceptual than the previous two labs were. The next one should be more hands-on — for those of you who read this far, you get a sneak peek — we’ll be talking about unit testing. I know, I know, no one likes writing unit tests; why would I write code to test my own code? That’s just taking away from development time! I know. That’s what people say. And it’ll feel like that. And unit testing is *not* infallible. But it *is* a good thing to go about doing. We’ll talk about it when we get there. For now, nice job on this lab!
