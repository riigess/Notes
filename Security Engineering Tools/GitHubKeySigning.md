# GitHub Key Signing
In order to do github's key signing, you will need a GPG key in order to do so.

## Steps
1. Install some sort of gpg signing system (GPGSuite, gnupg, gpg)
2. Create your SSH Key for github and configure your system - however you wish to do so - to use the key when making commits
3. Use `gpg --gen-key` to create a new key, and follow the prompts (using the same email as what you used for your SSH Key)
4. `gpg --export --armor youremail@example.com > mypubkey.asc`
5. Confirm your git's global settings are set using `git config --global user.name ""` and `git config --global user.email ""` are used
6. Use `gpg --list-secret-keys --keyid-format LONG` to get the key's ID to push to `git` in the next step here
7. Use `git config --global user.signingkey <key_id>` to push the keyid to git to use when signing commits
8. Make sure you `cat` mypubkey.asc and copy and paste that into github
9. Enable gpg signing in git using `git config --global commit.gpgsign true`
10. Give it a test and confirm everything works using `git commit -S -m ""`. Making sure to use -S to sign the commit!
