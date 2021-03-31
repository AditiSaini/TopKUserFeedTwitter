# ***Finding top K tweets for a user feed***

## **A) Installing Dependencies and Running the program**
### 1. Install dependency virtualenv using pip
	MACOS: python3 -m pip install --user virtualenv
	WINDOWS: py -m pip install --user virtualenv
### 2. Create a virtual environment 
	MACOS: python3 -m venv env
	WINDOWS: py -m venv env
### 3. Activate virtual environment
	MACOS: source env/bin/activate
	WINDOWS: .\env\Scripts\activate
### 4. Download dependencies from requirements.txt file
	pip install -r requirements.txt
### 5. Run the program
	MACOS: python3 main.py
	WINDOWS: python3 main.py
### 6. Deactivating the virtual environment 
	deactivate


## **B) Running tests**
### 1. Go to the root directory of the folder and run 
	python3 test.py


## **C) Assumptions**
 1. The user tweets data is static 
 2. The computation for the top k feeds takes place when the user requests the data
 3. The top k feeds are based only on timestamp. The more recent the tweet, the higher the position

### NOTE: Both the original as well as the bonus tasks have been implemented
