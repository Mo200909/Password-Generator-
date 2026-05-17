
A cryptographically secure password generator built using Python's `secrets` module, which is recommended 
over `random` for security-sensitive applications. The `make_secure_password` function lets you customize 
the password length and toggle the inclusion of uppercase letters, digits, and symbols. It uses a 
retry loop to guarantee that every generated password satisfies all the character-category requirements 
you've enabled — no weak outputs slip through. Two example passwords are printed on run: a full 32-character 
default and a shorter 8-character symbol-free variant. This is a practical, real-world utility that 
demonstrates best practices in Python security programming.
