# Analysis of Emoji Usage on LinkedIn
___
## Project Overview
___
This project utilizes a **Selenium** webscraper to pull posts from LinkedIn.   The posts have all duplicates removed and then are stripped of their emojis and the emojis are stored into their own unique database for analysis via **pandas** and **matplotlib**. 

## Project Requirements
___
1. Scrape two pieces of data from anywhere, read two data files (csv,json)
2. Generate a summary from multiple doucments and summarize them into a dataframe.
3. Utilize 3 matplotlib visualizations.
4. Use a virtual environment.
5. Jupyter notebook is clearly anotated.

## Running the Project
____
### Make sure to retrieve the config.json file.  If you need access to it, please send me an email or message me in slack
1. Save the config.json file in the project folder.  *This is essential for the webscraper to run.*
2. install the requirements.txt file. `pip install -r requirements.txt`
3. Unzip the Raw_Data.zip and Data_CSV.zip. (if you want the folders to be created automatically you can just run the *mini webscraper*)
4. Initialize the virtual environment.

### Virtual Environment Instructions
1. After you have cloned the repo to your machine, navigate to the project folder in GitBash/Terminal.
2. Create a virtual environment in the project folder.
3. Activate the virtual environment.
4. Install the required packages.
5. When you are done working on your repo, deactivate the virtual environment.

**Virtual environment commands**

| Command | Linux/Mac | Git Bash |
| ----------- | ----------- | ----------- |
| Create | python3 -m venv venv | python -m venv venv |
| Activate | source venv/bin/activate | source venv/Scripts/activate |
| Install | pip install -r requirements.txt| pip install -r requirements.txt|
| Deactivate | deactivate | deactivate |

Note for VS Code Users:

If you're using VS Code to run the Jupyter Notebook or Python script, ensure that the virtual environment(venv) is selected as the kernel. This is necessary for the modules installed from requirements.txt to be active when running the project.

To select the kernel, open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P on Mac) and search for "Python: Select Interpreter". Choose the one for the virtual environment (venv).
