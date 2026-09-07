import re
from playwright.sync_api import Page, expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page()
    
    # Expect a title "to contain" a substring.
    page.goto("https://sidewiberau.com//")
    print("opened")
    try:
        expect(page).to_have_title(re.compile("Login SIDEWIBERAU"))
        print("Open Page - PASSED ✅")
    
    except AssertionError:
        print("Open Page - FAILED ❌")
        
    # Click Button
    page.get_by_role("button",name="Login Sebagai Tamu").click()
    try:
        expect(page).to_have_title(re.compile("Sistem Informasi Destinasi Wisata Berau"))
        print("Sign in as Guest - PASSED ✅")
    except AssertionError:
        print("Sign in as Guest - FAILED ❌")
   
    input("...")