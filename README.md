Publishing machine learning project on the Internet
---

Data set:
https://www.kaggle.com/uciml/iris

### Building the project
1. Create a Virtual Env using `virtualenv venv`
2. Activate the Virtual Env using `cd venv/bin` & then, `source activate`
3. Install all dependencies using `pip install -r requirements.txt`

### Running project locally
Run `index.py` file which will boot up server and visit the url in the browser.

### Running on the Internet
1. Signup on `pythonanywhere.com`
2. Go to `Web` section and create new Flask Application as per the python version applicable to you.
3. Upload your code through file upload or clone your git repository via console.
4. Build the pickle file again to match the environment. Run `model.py` file through console.
5. The application is ready to be served on the internet.
6. The running version of this code is available [here](http://vdharam01.pythonanywhere.com/)