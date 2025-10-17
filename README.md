# The Robot Driver

The purpose of this project is to understand PlayWright basics in a Python environment by creating a program that controls a web browser to complete a fixed, single task. In this case that task is to retrieve the price of a product on the website Uniqlo.

## To run the project, you simply need:
- [Node](https://nodejs.org/en)
- [Python](https://www.python.org/downloads/)
- [PlayWright](https://playwright.dev/docs/intro#installing-playwright)

Once these technologies are installed, make sure to run the following command to install the Playwright browsers:
```
playwright install
```

After that, you should be able to run the program!

If you'd like to see what playwright is doing in action, go ahead and change **line 6** to the following:
```
browser = playwright.chromium.launch(headleass = False)
```
