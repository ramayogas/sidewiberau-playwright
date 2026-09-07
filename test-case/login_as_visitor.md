# Login Test Cases — SIDEWIBERAU

## Test Scope

Testing the login and guest access functionality.

---

## TC-LOGIN-001 — Open Login Page

**Scenario:**  
Verify that the login page can be opened successfully.

**Precondition:**
- Internet connection is available.

**Test Data:**
- URL: https://sidewiberau.com/

**Test Steps:**
1. Open the SIDEWIBERAU website.

**Expected Result:**
- Login page is displayed.
- Page title contains `Login SIDEWIBERAU`.

**Test Type:** Positive  
**Priority:** High

---

## TC-LOGIN-002 — Login as Guest

**Scenario:**  
Verify that a user can access the system as a guest.

**Precondition:**
- Login page is successfully opened.

**Test Data:**
- Button: `Login Sebagai Tamu`

**Test Steps:**
1. Open the login page.
2. Click `Login Sebagai Tamu`.

**Expected Result:**
- User is redirected to the guest interface.
- Page title contains `Sistem Informasi Destinasi Wisata Berau`.

**Test Type:** UI/Fuctional  
**Priority:** High
