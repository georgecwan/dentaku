# Introduction

<img src="https://github.com/VikingsDev/Vikingsdev-art/blob/master/Bounties/bounties-logo.svg?sanitize=true" width="50px"/>

Contribute to Dentaku and get Bounties!

### What types of contributions we're looking for

[B] = Bounty eligible

* Bug finding
   * If you find a bug with Dentaku, please report it in the Issues tab!
* Feature requests
   * If there's a feature you want to see in Dentaku, submit an issue!
* Documentation [B]
   * Helping us keep track of our documentation is always helpful.
* Making Commands [B]
   * If you have a brilliant idea for a command, or want to implement someone elses's idea in the Issues tab, feel free to fork and make a pull request.
* Core Improvements [B]
   * Sometimes the core functionality of the bot needs to be expanded, fixed, or optimized.

# Ground Rules

Responsibilities
* Create issues for any major changes and enhancements that you wish to make. Discuss things transparently and get community feedback.
* **Claim an issue by commenting** before you start working on it! This makes sure that people won't work on the same issue at the same time.
* **Document your code well.** Write comments and make sure your code is as easy to understand as possible.
* **Be secure.** Keep API tokens, credentials, etc. out of the repository. If there are credentials you need to add as files, make sure you add the filename in the `.gitignore`
* When adding commands always create new classes and a new file.
* **Be welcoming** to newcomers and encourage diverse new contributors from all backgrounds. See the [Python Community Code of Conduct](https://www.python.org/psf/codeofconduct/).
* Always test your commands thoroughly before making a pull request. This means setting up the development environment, running the bot, and testing the command or feature you just made to make sure there are no bugs.

# Your First Contribution

Unsure where to begin contributing to Dentaku? You can start by looking through these beginner and help-wanted issues:
* Good first issue - issues which should only require a few lines of code, and a test or two.
* Beginner issues - issues which should be a bit more involved than beginner issues.

Want to make an easy command? See the next section, **Getting started**.

# Getting started

## Setting up a development environment

1. Clone repository
`git clone https://github.com/VikingsDev/Dentaku.git`
2. Create virtual environment
`python -m venv venv`
3. Create export file
`touch export.sh`
4. Edit `export.sh` using a text editor, and add
```
export EMAIL="YOUR_FACEBOOK_ACCOUNT_EMAIL"
export PASSWORD="YOUR_FACEBOOK_ACCOUNT_PASSWORD"
export BITLY_GAT="YOUR_BITLY_GENERIC_ACCESS_TOKEN"
```
Note: Keep quotation marks!<br>
Get your bit.ly [Generic Access Token](https://bitly.com/a/oauth_apps) (required if you want to use commands with link shorteners)<br>
5. Activate variables and venv <br>
`source export.sh` <br>
`source venv/bin/activate` <br>
6. Run the bot
`python main.py`

See our wiki for more instructions on how to get started.

[Creating your first command](https://github.com/VikingsDev/Dentaku/wiki/2.-Making-your-first-command)

## API Documentation

[command.py](https://github.com/VikingsDev/Dentaku/wiki/command.py)


# How to report a bug
If you find a security vulnerability, do NOT open an issue. Email vikingsdev@gmail.com instead.

Any security issues should be submitted directly to vikingsdev@gmail.com
In order to determine whether you are dealing with a security issue, ask yourself these two questions:
 * Can I access something that's not mine, or something I shouldn't have access to?
 * Can I disable something for other people?

If the answer to either of those two questions are "yes", then you're probably dealing with a security issue. Note that even if you answer "no" to both questions, you may still be dealing with a security issue, so if you're unsure, just email us at vikingsdev@gmail.com.

You can even include a template so people can just copy-paste (again, less work for you).

When filing an issue, make sure to answer these five questions:

 1. What version of Python are you using?
 2. What operating system are you using?
 3. What did you do?
 4. What did you expect to see?
 5. What did you see instead?

# Code review process

After you submit a PR, a VikingsDev Exec will look over the code and either approve it or request new changes. Once the review is complete, they will merge it and your contribution is now a part of the official Dentaku :)

# Community

Join the [VikingsDev Community](https://vikingsdev.ca/#social)! We're most active on Messenger.

# Conventions

Use snake_case for naming.

Use the imperative mood for commit messages. Read up on [this article](https://chris.beams.io/posts/git-commit/) for good commit message habits and if you aren't sure what imperative mood means.
