import feedparser

RSS_FEEDS = {
    "TechCrunch": "https://techcrunch.com/feed/",
    "HackerNews": "https://news.ycombinator.com/rss",
    "TheVerge": "https://www.theverge.com/rss/index.xml"
}

def get_latest_news():
    all_headlines = []
    print("📡 Initializing RSS Stream...")
    for source, url in RSS_FEEDS.items():
        print(f"📥 Scanning {source} via RSS...")
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            all_headlines.append({
                "source": source,
                "title": entry.title,
                "link": entry.link
            })
    print(f"✅ Pulse check complete. Found {len(all_headlines)} signals.")
    return all_headlines