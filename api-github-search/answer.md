1. What is the role of query parameters in this request?
Ans- Query parameters are used to customize the API request
     some of the query parameters are:-
     "q" : "python" - searches the keyword
     "sort" : "stars" - sorts the keyword by values in this case stars
     "order" : "desc" - sets the order of the result in this case descending order
     "per_page" : 5 - limits the results in this case 5

2. Why do we use response.json() instead of response.text?
Ans- response.json() converts the response into python dictionary which makes it more easier to read and work with it
     whereas response.text just gives the raw string which is harder to read and harder to work with, so using response.json()
     is more efficient for understanding.