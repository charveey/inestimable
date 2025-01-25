# Inestimable - A fan site I made for a friend | Powered by Jekyll

## Setup
1. Install Jekyll: `gem install bundler jekyll`
2. Install Python dependencies: `pip install -r requirements.txt`
3. Clone the repository
4. Run `bundle install`
5. Scrape Instagram posts: `python scrape_instagram.py`
6. Start the local server: `bundle exec jekyll serve`

## Dependencies
- GSAP (included via CDN)
- Jekyll
- Sass
- Python
  - Instaloader
  - PyYAML

## Instagram Scraping
1. Replace `instagram_username` in `scrape_instagram.py` with desired account
2. Run the script to update `_data/bestsellers.yml`

## Customization
- Modify Instagram username in scraping script
- Adjust content in `_data/bestsellers.yml`
- Modify styles in `_sass/main.scss`

## Notes
- Ensure you have appropriate permissions for Instagram scraping
- Instagram may block scraping attempts
