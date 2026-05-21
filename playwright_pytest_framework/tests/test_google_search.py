from pages.home_page import HomePage

def test_google_search(page):
    home = HomePage(page)

    home.navigate_to()
    home.search_for("Playwright Python")

    # Wait for results to load (e.g., a search‑result selector)
    page.wait_for_selector("text=Playwright Python")

    # Very basic assertion
    assert "TENY" in page.title()



