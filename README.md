# cloudwalk

The program has two steps, the first was made in ruby:
  The first check is the recommendation that is rule-based, if all rules is approved, the program will call the microservice in python to check the score.
  
The last step was made in python with machine learning, using Jupyter Notebook. I trained my machine with the data provided.
  In this step if the score is higher than 0.5, finally the transaction is gonna approved.
