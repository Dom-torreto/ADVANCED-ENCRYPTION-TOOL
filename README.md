# ADVANCED-ENCRYPTION-TOOL  


*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: CHANDRAKANT RAMASHANKAR JAISWAR 

*INTERN ID*: CT04DL772

*DOMAIN*: CYBER SECURITY & ETHICAL HACKING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DISCRIPTION*:  

I have developed a Python-based AES-256 file encryption and decryption utility Advanced Encryption Standard (AES) with a 256-bit key. It's one of the most secure symmetric encryption algorithms used today, trusted by governments, banks, and security professionals worldwide.

The tool I created allows users to encrypt and decrypt files using AES-256 in CBC (Cipher Block Chaining) mode. It’s written in Python, using the cryptography library, which provides a robust and well-tested set of tools for modern encryption.

Here’s how it works. When a user chooses to encrypt a file, the program first prompts for the input file path (the file to be encrypted), the output file path (where the encrypted file will be saved), and a password. That password isn’t used directly. Instead, a random salt is generated and combined with the password through a key derivation function called PBKDF2 — this safely transforms the password into a secure 256-bit encryption key. A random 16-byte initialization vector (IV) is also created to ensure that encrypting the same file twice with the same password still results in different encrypted outputs.

Once the key and IV are ready, the file's content is read and padded (to make its length compatible with the AES block size), and then it’s encrypted. The output file contains the salt, the IV, and the encrypted data — all in one package. This way, the same file can be decrypted later using just the original password.

When decrypting, the process is reversed. The tool reads the salt and IV from the encrypted file, regenerates the key using the entered password, and decrypts the content. If the password is correct, the user gets back the original file exactly as it was.

To keep things simple and user-friendly, I added a menu-driven command-line interface. When the script is run, it asks the user to choose whether they want to encrypt or decrypt a file. It’s secure, thanks to password input being hidden using getpass, and it supports any kind of file — text, images, PDFs, or even executables.

I built this tool not just as a programming exercise, but as a practical way to understand how real-world encryption works. And more importantly, to provide something useful — a way for anyone to protect their files with strong, reliable encryption without needing to understand cryptography in depth. Whether it's for personal documents, project files, or sensitive business data, this tool ensures that privacy is in your hands

*OUTPUT*

![Image](https://github.com/user-attachments/assets/a08b80f5-10d4-47e7-8624-500da7c58e7c)
