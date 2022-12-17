from selenium.webdriver.chrome.options import Options

user_agent_config = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "AppleWebKit/537.36 (KHTML, like Gecko)",
    "Chrome/108.0.0.0",
    "Safari/537.36",
]

options = Options()
options.add_argument("headless")
options.add_argument("window-size=1920x1080")
options.add_argument("disable-gpu")
options.add_argument(f"user-agent={' '.join(user_agent_config)}")
