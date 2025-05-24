# XSS Worm Lab – Elgg Exploitation

This project demonstrates several XSS-based attacks against the Elgg social networking platform, inspired by the Samy worm. It includes JavaScript payloads for:

- **Task 4:** Adding Samy as a friend via CSRF.
- **Task 5:** Modifying the victim’s profile field ("About Me").
- **Task 6:** Creating a self-propagating XSS worm using `<script src=...>`.
- **DOM-Based Worm:** Injecting the worm directly via DOM manipulation.

## 💾 Files Included

- `report.pdf`: Full write-up of the lab with payload explanations and screenshots.
- `payloads/`
  - `task4_add_friend.js`
  - `task5_modify_profile.js`
  - `task6_self_propagating.js`
  - `dom_based_worm.js`

## ⚠️ Disclaimer

This project is for educational purposes only. Do not attempt these attacks on systems you do not own or have explicit permission to test.

---

Created as part of a security lab project.
