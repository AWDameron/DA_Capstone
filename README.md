# DA_Capstone
### Virtual Environment Instructions
1. After you have cloned the repo to your machine, navigate to the project folder in GitBash/Terminal.
2. Create a virtual environment in the project folder.
3. Activate the virtual environment.
4. Install the required packages.
5. When you are done working on your repo, deactivate the virtual environment.

**Virtual environment commands**

| Command | Linux/Mac | Git Bash |
| Create | python3 -m venv venv | python -m venv venv |
| Activate | source venv/bin/activate | source venv/Scripts/activate |
| Install | pip install -r requirements.txt| pip install -r requirements.txt|
| Deactivate | deactivate | deactivate|

Note for VS Code Users:

If you're using VS Code to run the Jupyter Notebook or Python script, ensure that the virtual environment(venv) is selected as the kernel. This is necessary for the modules installed from requirements.txt to be active when running the project.

To select the kernel, open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P on Mac) and search for "Python: Select Interpreter". Choose the one for the virtual environment (venv).
