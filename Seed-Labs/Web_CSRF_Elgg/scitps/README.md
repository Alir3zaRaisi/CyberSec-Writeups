# 🔐 CSRF Attacks on Elgg - SEED Labs

This project documents a series of Cross-Site Request Forgery (CSRF) attacks performed on a vulnerable Elgg-based social networking platform, as part of the SEED Labs Web Security series.

Author: **Alireza Raisi**  
Date: **May 24, 2025**

---

## 📄 Overview

This repository contains a write-up and scripts for four tasks designed to demonstrate CSRF attacks under different conditions:

1. **Capturing HTTP POST Requests**  
2. **GET-based CSRF Attack (Friend Request)**  
3. **POST-based CSRF Attack (Profile Modification)**  
4. **Testing CSRF Countermeasures in Elgg**

---

## 🧪 Lab Setup

These tasks were performed in a SEED Labs environment using Docker containers. The Elgg web application was used with CSRF protection initially disabled, then re-enabled for testing.

---

## 📚 Contents

### ✅ Write-Up

- [`Web_CSRF_Elgg_Writeup.pdf`](./Web_CSRF_Elgg_Writeup.pdf): Full LaTeX report detailing all 4 tasks, attacks, results, and conclusions.
- Includes screenshots, HTTP request captures, and code explanations.

### 🧬 Scripts

All exploit scripts are located in the [`scripts/`](./scripts) folder:

| File | Description |
|------|-------------|
| `csrf_get_friend.html` | GET-based CSRF attack to force a friend request to Alice |
| `csrf_post_profile.html` | POST-based CSRF attack to change Alice’s profile text |

---

## 🔐 CSRF Countermeasure

In Task 4, the Elgg CSRF countermeasure was re-enabled by modifying:

```
/var/www/elgg/vendor/elgg/elgg/engine/classes/Elgg/Security/Csrf.php
```

Once active, the attacks failed due to the inability to guess or retrieve session-specific CSRF tokens (`__elgg_token` and `__elgg_ts`), highlighting the importance of token-based protection.

---

## 🚫 Important Notes

- These tasks are conducted in a controlled lab environment and are strictly for educational purposes.
- Do **not** attempt these techniques on real-world websites or systems you do not own or have explicit permission to test.

---

## 📧 Contact

For questions, feel free to reach out via GitHub Issues or email.
