# Bid Auction
This is a Python program that simulates a bid auction. The program prompts the user for their name and a bid amount, then stores the information in a dictionary. The program continues to prompt for additional bids until the user indicates that there are no more bidders. Once all bids have been entered, the program identifies the highest bid and the winner of the auction.

## Usage
To run the program, simply execute the auction.py script in a Python environment. The program will prompt the user for their name and a bid amount, then store the information in a dictionary. The program will continue to prompt for additional bids until the user indicates that there are no more bidders. Once all bids have been entered, the program will identify the highest bid and the winner of the auction.

## Example
```py
$ python auction.py
What is your name?
John Smith
Enter a bid amount:
$100
Are there still other bidders?
yes
What is your name?
Jane Doe
Enter a bid amount:
$200
Are there still other bidders?
no
The winner is Jane Doe, with a bid of $200
```

## Note
This program is a part of my day 9 project of 100 days of python code.
A test version of this program is available on [replit.](https://replit.com/@labelisaiah/blind-bidding-action?v=1) Feel free to test it out and give feedback for improvements.

## Requirements
+ Python 3.x

## Dependencies
This program does not have any dependencies outside of the Python standard library.

## Limitations
+ The program does not validate user input and assumes that the user will input valid integers for the bid amount.
+ The program does not prevent duplicate names from being entered.

## Contributions
This program is part of learning projects. Contributions and suggestions for improvements are welcome. If you would like to contribute to the development of this program, please fork the repository and submit a pull request with your proposed changes.

## License
This program is licensed under the [MIT License.](https://chat.openai.com/chat/LICENSE)

## Acknowledgements
I would like to thank Dr. Angela Yu who has helped improve my understanding of Python.

Thank you for using Bid Auction.
