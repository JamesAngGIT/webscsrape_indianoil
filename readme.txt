to create new venv
  python -m venv venv

to activate
  venv\Scripts\activate
  
in gitignore file
  don't include venv folder
  only include scripts
  ref --> https://www.youtube.com/watch?v=APOPm01BVrk

to save to requirements file
  pip freeze > requirements.txt

to install from requirements file.
  pip install -r requirements.txt

to remove virtual environment
  rmdir venv /s

to add base libraries into virtual venv
  python -m venv venv --system-site-packages

to see only local libraries
  pip list --local

to install gensim (https://radimrehurek.com/gensim/)
  pip install --upgrade gensim
  if there's error, error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools":
  upgrade Microsoft visual C++, see here https://github.com/benfred/implicit/issues/76
  download from here https://visualstudio.microsoft.com/visual-cpp-build-tools/
  After installation, should be okay

to view output
  install Hydrogen from atom packages
  python -m pip install ipykernel
  restart atom --> then you'll have jupyter-like output
