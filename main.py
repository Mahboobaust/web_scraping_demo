import pyshorteners

def shorten_url(long_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(long_url)
    print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    # Replace 'YOUR_LONG_URL' with the URL you want to shorten
    long_url_to_shorten = "https://drive.google.com/file/d/1H0QUWiNipt2cmhvMvbfaH9DwvhanCHf_/view?usp=sharing"

    shorten_url(long_url_to_shorten)
