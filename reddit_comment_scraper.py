import praw

# Set up Reddit API credentials
reddit = praw.Reddit(
    client_id='',           # Replace with your client ID
    client_secret='',   # Replace with your client secret
    user_agent=''          # Replace with your user agent
)

# List of Reddit thread URLs to fetch comments from
reddit_urls = [
    'https://www.reddit.com/...',


    # Add more URLs as needed
]

# Open a text file to save the comments
with open('reddit_comments.txt', 'w', encoding='utf-8') as file:
    # Function to fetch comments from a Reddit thread and save to file
    def fetch_comments_from_url(url):
        submission = reddit.submission(url=url)
        submission.comments.replace_more(limit=None)  # Load all comments

        # Header for each thread
        file.write(f"\n{'=' * 80}\n")
        file.write(f"Thread URL: {url}\n")
        file.write(f"Title: {submission.title}\n")
        file.write(f"{'=' * 80}\n\n")

        # Function to recursively write comments and their replies
        def write_comment(comment, level=0):
            # Assign a unique ID for each comment
            comment_id = f"{comment.id}"
            reply_to_id = f"Reply to: {comment.parent_id[3:]}" if comment.parent_id != comment.link_id else "No replies"

            # Write comment with indentations based on the hierarchy level
            file.write(f"{' ' * level * 4}Comment ID: {comment_id}\n")
            file.write(f"{' ' * level * 4}{reply_to_id}\n")
            file.write(f"{' ' * level * 4}Author: {comment.author}\n")
            file.write(f"{' ' * level * 4}Body: {comment.body}\n")
            file.write(f"{' ' * level * 4}{'-' * 40}\n")

            # Recursively write replies
            for reply in comment.replies:
                write_comment(reply, level + 1)

        # Write all top-level comments and their replies
        for top_level_comment in submission.comments:
            write_comment(top_level_comment)
            file.write("\n" + "=" * 80 + "\n")  # Separator between top-level comments


    # Iterate over each URL in the list and fetch comments
    for url in reddit_urls:
        print(f"Fetching comments from: {url}")
        fetch_comments_from_url(url)

print("Comments have been saved to 'reddit_comments.txt'.")