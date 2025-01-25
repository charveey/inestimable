import instaloader
import yaml
import os
import sys

def scrape_instagram_posts(username, max_posts=10):
    """
    Scrape posts from an Instagram account
    
    Args:
        username (str): Instagram username to scrape
        max_posts (int): Maximum number of posts to scrape
    
    Returns:
        list: List of post dictionaries with image URLs and captions
    """
    # Initialize Instaloader
    L = instaloader.Instaloader()
    
    try:
        # Login anonymously (no credentials needed)
        profile = instaloader.Profile.from_username(L.context, username)
        
        # Collect posts
        posts = []
        for post in profile.get_posts():
            # Stop if we've reached max posts
            if len(posts) >= max_posts:
                break
            
            # Check if post has an image
            if post.mediacount == 1 and post.typename == 'GraphImage':
                posts.append({
                    'caption': post.caption[:100] if post.caption else f'Post {len(posts) + 1}',
                    'image': post.url
                })
        
        return posts
    
    except Exception as e:
        print(f"Error scraping Instagram profile: {e}")
        return []

def save_posts(username, output_path='_data/dump.yml'):
    """
    Scrape and save Instagram posts to YAML file
    
    Args:
        username (str): Instagram username to scrape
        output_path (str): Path to save YAML file
    """
    # Ensure data directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Scrape posts
    posts = scrape_instagram_posts(username)
    
    # Save to YAML
    with open(output_path, 'w') as f:
        yaml.dump(posts, f, default_flow_style=False)
    
    print(f"Saved {len(posts)} posts from {username} to {output_path}")

# Command-line interface
if __name__ == '__main__':
    # Check for correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: python scrape_instagram.py <username> [output_path]")
        sys.exit(1)
    
    # Get username from command line
    instagram_username = sys.argv[1]
    
    # Optional output path
    output_path = sys.argv[2] if len(sys.argv) > 2 else '_data/dump.yml'
    
    # Scrape and save
    save_posts(instagram_username, output_path)
