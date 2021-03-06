# Git

## Introduction

Git is a widely used utility for versioning files and projects. Most people associate it with GitHub, however git can also be used independently or on other platforms.

There are many GUI applications for interfacing with git (GitHub Desktop, Sourcetree, etc.), however you will not be able to use these on a remote server (compute1 and compute0) so you might as well just learn git.

## Getting Started

The lab uses GItHub for storing all of our repositories, so you'll need to create an account. Once you have an account, you'll need to set up SSH keys if you are using 2-Factor Authentication (2FA). You will need to [create a key](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) and then [add it to your account](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account). You will need to do this on each device you are planning to use with GitHub (compute1, compute0, your personal machine, etc.).

## Basics

Now, let's go through the basic git workflow.

First, we'll need to clone a repository:

```
git clone REPOSITORY_URL
```

Or, if you have 2FA enabled:

```
git clone git@github.com:jinlab-washu/MGI.workflows.git
```

Once you have your repository, you can start adding files and making changes. After you have made some changes check the status:

```
git status
```

You will see a list of modified files and untracked files. Untracked files are newly created files that have not yet been versioned with git. To `commit` your work you need to `add` the appropriate files to the staging area:

```
git add FILE1 FILE2 FILE3
```

You do not need to add all of the files you've changed or created, just those that you have finished modifying. If you run `git status` again you will now see a list of files that are ready to be committed. If these files are correct then go ahead and commit:

```
git commit
```

This will open your default text editor where you will write a commit message explaining your changes. When you're finished just save and close the editor and your commit will be created. If you run `git log` you will now see your latest commit at the top of the list. However, this commit is only in your local repository. To share it with your collaborators you need to `push` it to the `remote` repository, in this case GitHub:

```
git push
```

Now if you look at the repository on GitHub you will see be able to see your changes.

Finally, to get changes other people have made you can just:

```
git pull
```

## Intermediate

If you are working on a larger change that will span multiple commits it will probably make sense to create a new `branch`. Branching allows you to commit and push changes without impacting the `master` branch that other collaborators will be using for running analysis. To create a new branch:

```
git branch MY_NEW_BRANCH
```

To switch to this branch:

```
git checkout MY_NEW_BRANCH
```

If you prefer, you can create a new branch and switch to it with one command:

```
git checkout -b MY_NEW_BRANCH
```

Now that you are in your new branch you can make changes, commit, and push just like earlier. On GitHub you will need to select your newly created branch in order to see your changes. 

Once you have finished and tested your feature you will want to merge it back into `master` (probably, use good judgement). To merge a branch you will first need to switch to the destination branch, e.g. `git checkout master`. Now that you are on `master`, you can go ahead and merge:

```
git merge MY_NEW_BRANCH
```

Assuming no one else has made any changes on `master` this will work perfectly. However, if other users have changed files that you are changing you will receive a merge conflict. To resolve a merge conflict you will first need to find out what files have issues using `git status`. Next, you will need to open each of those files and manually correct the conflicting chunks. These conflicts will look something like:

```
Some non-broken stuff here
<<<<<<< HEAD
Hey here's some text
=======
Hey here's some text we changed
>>>>>>> MY_NEW_BRANCH
Some more non-broken stuff
```

The section marked with `HEAD` denotes the line on the destination branch:

```
<<<<<<< HEAD                                                                                                                                                                   
Hey here's some text                                                                                                                                                           
======= 
```

The section marked with `MY_NEW_BRANCH` is the change you are trying to merge in in its place:

```
=======                                                                                                                                                                        
Hey here's some text we changed                                                                                                                                                
>>>>>>> MY_NEW_BRANCH 
```

You will need to either delete one of those chunks or manually combine them into the desired final result. Once you are finished you can `add` and `commit` the changed files just like you would any other changes.

## Advanced

**TODO**

Talk about rebasing, changing remote repositories

## Best Practices

### gitignore

If you have files in your working directory you do not want to accidentally commit you should add their names to file named `.gitignore`. This will prevent them from showing up in `git status` making it difficult to accidentally add them to a repository.

For example, let's say we've copied `PHI.txt` and some FASTQ files to our working directory to more easily test a script we're writing. Obviously we do not want to push PHI to a public repository and the FASTQ files aren't really part of the project so they shouldn't be included either. Our `.gitignore` would look something like:

```
PHI.txt
*.fastq
```

This will explicitly ignore `PHI.txt` and all files with the extension `.fastq`. 

### Commit Messages

Commit messages should be short, but descriptive. Generally, a message like "Updated FILE" is not helpful.

## Tagging

Each version of a project should be tagged so that we can easily identify which commits were used in which experiments or analysis projects. That being said, this should not turn into tagging every single commit as a new version.

To view existing tags you can run:

```
git tag
```

To add a tag to the most recent commit:

```
git tag TAG_NAME
```

## Other Software

As mentioned previously, there are numerous graphical clients for interacting with git. The only one of these you will be able to run in your terminal on the clusters is magit, which is built on top of emacs. Generally speaking, learning plain git (and arguably magit) will be a much more worthwhile investment of your time than learning one of the desktop options. Git will be available and work exactly the same on pretty much any platform you will encounter; the same cannot be said for other options.

### magit

[Magit](https://magit.vc) is a git client built on top of emacs. Unfortunately, compute1 ships emacs 24.3.1 and compute0 ships emacs 24.5.1. To install magit from the emacs package archive you need to be running 25.1 or greater. 

However, an older version of magit (v2.3.0) is able to be built from source on compute0. Unfortunately, compute1 will require an even older version.

If you're going to be doing any significant development or git work on the clusters you should just make a Docker image with a more recent version of emacs and use that instead. If, for some reason, you really do want to use the default emacs feel free to build from source. 

### GitHub Desktop

https://desktop.github.com

### Sourcetree

https://sourcetreeapp.com 
