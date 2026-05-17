
A cryptographically secure password generator built using Python's `secrets` module, which is recommended 
over `random` for security-sensitive applications. The `make_secure_password` function lets you customize 
the password length and toggle the inclusion of uppercase letters, digits, and symbols. It uses a 
retry loop to guarantee that every generated password satisfies all the character-category requirements 
you've enabled: no weak outputs slip through.
