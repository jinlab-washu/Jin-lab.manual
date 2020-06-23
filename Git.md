# Git

## Introduction

Git is a widely used utility for versioning files and projects. Most people associate it with GitHub, however git can also be used independently or on other platforms.

There are many GUI applications for interfacing with git (GitHub Desktop, Sourcetree, etc.), however will not be able to use these on a remote server (compute1 and compute0) so you might as well just learn git.

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


## Intermediate

**TODO**

Talk about branching and merging

## Advanced

**TODO**

Talk about rebasing

## Best Practices

**TODO**

Commit messages, pulling, tagging
