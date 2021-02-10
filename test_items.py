def test_add_to_cart_button_exists(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    assert len(browser.find_elements_by_css_selector("button.btn-add-to-basket")) > 0
