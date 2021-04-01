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
 4. Expected answers for testing have been generated using the baseline solution by sorting and then extracting top K value

 ## **D) Methodology Adopted**
 1. Each of the csv files are converted into pandas dataframes for easier processing 
 2. For a particular user with user_id, get all the user_ids he follows 
 3. For each user_id that the user follows, put the data in a heap. If the user follows 8 other users, there will be 8 heaps in total 
 4. The heap will be a maximising heap with timestamp as the index for decision
 5. A main heap is created that takes in data of the most recent tweet from each user heap 
 6. From the main heap, the values are popped to an array that contains the topK results
 7. This is repeated, until the array contains the topK feeds of the user from his followers
<br/>
<br/>
<p>
    <img src="Image/diagram.png"/>
</p>

## **E) Space Complexity of the Algorithm**
- m: number of followers
- n: max number of tweets by a follower
- k: top k tweets and k<=mn
- Space Complexity for storing each user heap: O( m*n )
- Space Complexity for storing latest tweets from each user: O( m )
- Space Complexity for storing topK tweets: O( k )
- **Total Space Complexity**: O( m*(n+1) + k) ~ **O( mn + k )**

## **F) Time Complexity of the Algorithm**
- m: number of followers
- n: max number of tweets by a follower
- k: top k tweets and k<=mn
- Time Complexity for building a user heap: O( n )
- Time Complexity for building all user heap: O( m*n )
- Time Complexity for popping and pushing actions into the heap: O( log(x) ) where x is the size of the heap
- Time Complexity for putting the latest tweets into the main heap: O( m*log(n) )
- Time Complexity for extracting the top K tweets from the main heap: O( k*log(m) + k*log(n) )
- There is a k*log(m) because for each top K tweet, the main heap, of max size m, is popped off into the Top K Tweets Array
- There is a plus k*log(n) because the next recent tweet may need to be pushed to the main heap from a user heap of max size n. This happens when a value is popped off from the main heap into the top K array so a next value is added from that user heap to the main heap. In this way, the main heap maintains the lastest tweets from each user he follows. 
- **Total Time Complexity**: O( m*n + m*log(n) + k*log(m) + k*log(n) ) ~ **O( m*n + k*(log(m) + log(n)) )**
- Time Complexity if a direct sorting solution was used and top K was extracted: O( mn*log(mn) )
