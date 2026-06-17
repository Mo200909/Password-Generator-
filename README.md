## Keyspace

With all character categories enabled (lowercase, uppercase, digits, symbols), 
the generator draws from a 94-character set. At the default length of 32, 
this yields a keyspace of approximately 94^32 ≈ 7.7 × 10^62 possible passwords.

For context, this far exceeds any practical brute-force threat model — a 
16-character password from this same character set (94^16 ≈ 8.8 × 10^31) 
already provides effectively unbreakable security against current and 
foreseeable computing power. The 32-character default was chosen for margin, 
not because shorter outputs would be meaningfully weaker.
