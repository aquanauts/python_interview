# Creating a Codespace

In case you don't have a Linux or a Mac machine, you can use a Github Codespace to develop your solution for free. 

1. [Create a copy of this repository](https://github.com/aquanauts/python_interview/generate)
    1. Be sure to make it private, as you'll be pushing your solution to it
3. [Create a Codespace](https://docs.github.com/en/codespaces/developing-in-codespaces/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository) in your copy
    1. Check out the "Machine types" in the advanced options flow to ensure you're using the most powerful one available for free!
4. Once you’re inside the Codespace, create a branch to work on by running `git checkout -b working_branch`
    1. The `make patch` command just diffs against the main branch, so it’s important to work off of a branch
5. Run `make deps` to download all the relevant dependencies; this should take about 5 minutes
6. Develop your solution as usual; `make run` and `make test` should execute reasonably quickly now that dependencies are present
7. Once you've generated your patch file, you can right-click it in the file explorer and click Download
