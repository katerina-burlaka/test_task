# Run Test Task.

* [1. Prerequisites](#1-prerequisites)
* [2. Download or Clone the repository and install the required libraries](#2-download-or-clone-the-repository-and-install-the-required-libraries)
* [3. Run tests](#3-run-tests)

## 1. Prerequisites.

### 1.1 Install Python.

- Download and install Python 3.6 or higher [link](https://www.python.org/downloads/).

### 1.2 Install Chrome browser.

- Install Chrome browser following the [guide](https://www.google.com/chrome/).

### 1.3 Install ChromeDriver.

For MacOS:
```bash
brew install chromedriver
```
What's **BREW** and how to install and use you can find [here](https://brew.sh/).

For Ubuntu Linux or Windows OS:
- Download the latest version of ChromeDriver by [link](https://chromedriver.chromium.org/downloads).
- Go to the Downloads directory and unzip the chromedriver.zip file.
  
For Ubuntu Linux:
- Open the Downloads directory in the terminal and move the chromedriver binary file to the /usr/local/bin directory.
```bash
mv chromedriver /usr/local/bin
```
For Windows OS:
- Copy the chromedriver binary file to C:\Windows folder.

## 2. Download or Clone the repository and install the required libraries.

### 2.1 Download or Clone the repository.

- Download the repository by [link](https://github.com/katerina-burlaka/test_task.git).
- Unzip the test_task-master.zip file.
- Rename the test_task-master directory to test_task

If GIT is installed on your PC/Laptop you simply do in the terminal:
```bash
git clone https://github.com/katerina-burlaka/test_task.git
```

### 2.2 Install the required libraries.
- Open terminal
- Go to the test_task directory:
```bash
cd test_task
```
- Install the pipenv library:
```bash
pip install pipenv
```
- Install all required libraries:
```bash
pip install
```
- Activate the environment:
```bash
pipenv shell
```
- If you need to deactivate the environment:
```bash
exit
```

## 3. Run tests.
- All tests locate in the test_task.py file
### 3.1 How to run one test.
- Go to the test_task directory:
```bash
cd test_task
```
- Run the next command:
```bash
python3.6 -m unittest test_task.TestTask.test_01_check_image
```

### 3.2 How to run all tests.
- Go to the test_task directory:
```bash
cd test_task
```
- Run the next command:
```bash
python3.6 -m unittest test_task.TestTask
```
