
import feedparser
from datetime import datetime

# Function to fetch blog posts from RSS feed
def fetch_blog_posts(rss_feed_url):
    feed = feedparser.parse(rss_feed_url)
    blog_posts = []

    for entry in feed.entries:
        post = {
            'title': entry.title,
            'summary': entry.summary if hasattr(entry, 'summary') else '',
            'link': entry.link,
            'published': entry.published if hasattr(entry, 'published') else 'Unknown Date'
        }
        blog_posts.append(post)

    return blog_posts

# Function to recommend posts based on keyword relevance
def recommend_blog_posts(user_interests, blog_posts):
    recommended_posts = []

    for post in blog_posts:
        relevance_score = 0
        for interest in user_interests:
            if interest.lower() in post['title'].lower() or interest.lower() in post['summary'].lower():
                relevance_score += 1

        if relevance_score > 0:
            recommended_posts.append((post, relevance_score))

    recommended_posts.sort(key=lambda x: x[1], reverse=True)
    return recommended_posts[:2]

# Main script logic
if __name__ == '__main__':
    print("🧠 Real Talk with Riggles Blog Recommender")
    print("Tell us your interests and we’ll match them with our latest blog posts.\n")

    user_input = input("What are your professional interests? (comma-separated): ")
    user_interests = [term.strip() for term in user_input.split(',')]

    rss_feed_url = 'https://www.getrealwithriggles.com/real-talk-with-riggles?format=rss'
    blog_posts = fetch_blog_posts(rss_feed_url)
    recommended_posts = recommend_blog_posts(user_interests, blog_posts)

    print("\n🔍 Top Recommendations:")
    if recommended_posts:
        for i, (post, score) in enumerate(recommended_posts, 1):
            print(f"\n🔹 Recommendation {i} (Relevance Score: {score})")
            print(f"📌 Title: {post['title']}")
            print(f"📝 Summary: {post['summary'][:250]}...")  # Truncate long summaries
            print(f"📅 Published: {post['published']}")
            print(f"🔗 Link: {post['link']}")
    else:
        print("⚠️ No relevant posts found. Try different keywords.")
