
# Reddit Comment Scraper

This Python script uses the Reddit API to fetch comments from specified Reddit threads and save them into a structured text file (`reddit_comments.txt`).

## Prerequisites

Before you can run this script, you need to have the following:

1. Python 3.x installed on your machine.
2. `praw` (Python Reddit API Wrapper) library installed. You can install it using pip:
   ```
   pip install praw
   ```
3. Reddit API credentials (client ID, client secret, and user agent). You can get these by creating a Reddit app [here](https://www.reddit.com/prefs/apps).

## Setup

1. **Clone the Repository or Download the Script:**

   Clone this repository or download the script file.

2. **Set Up Reddit API Credentials:**

   Open the script and replace the placeholders with your Reddit API credentials:
   ```python
   reddit = praw.Reddit(
       client_id='your_client_id',           
       client_secret='your_client_secret',   
       user_agent='your_user_agent'          
   )
   ```

3. **Add Reddit Thread URLs:**

   In the `reddit_urls` list, add the URLs of the Reddit threads you want to fetch comments from:
   ```python
   reddit_urls = [
       'https://www.reddit.com/...',
       # Add more URLs as needed
   ]
   ```

## Usage

1. Run the script using Python:
   ```
   python reddit_scraper.py
   ```

2. The script will fetch comments from the specified Reddit threads and save them in `reddit_comments.txt` in a structured format.

## Output Format

The output file (`reddit_comments.txt`) will contain the comments organized by Reddit threads with unique comment IDs and hierarchies, making it easy to understand which comments are replies to others.

Example output:
```
================================================================================
Thread URL: https://www.reddit.com/r/socialskills/comments/1epo1hb/how_the_hell_to_make_friends_in_your_20s/
Title: How the hell to make friends in your 20s?
================================================================================

Comment ID: comment1_id
Reply to: No replies
Author: CommentAuthor1
Body: This is a top-level comment.
----------------------------------------

    Comment ID: reply1_id
    Reply to: comment1_id
    Author: ReplyAuthor1
    Body: This is a reply to the top-level comment.
    ----------------------------------------

        Comment ID: reply2_id
        Reply to: reply1_id
        Author: ReplyAuthor2
        Body: This is a nested reply.
        ----------------------------------------

================================================================================
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to contribute to this project by submitting a pull request or opening an issue.
