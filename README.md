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

So, to comply with this new rule, let’s make a new branch, for example… `git checkout -b dev && git push —set-upstream origin dev`. We’ll need this to make pull requests on later. 

### Feature Branching
Throughout this lab, every time you make a change to the code, we’ll make a new branch as if it was a “feature.” For now, we won’t be making any changes, but stay tuned!