# Chapter 1

Pretty good intro, for me at least. I know next to nothing about python and even less about cryptography. This chapter felt like it got straight to the point but also eased me into the lesson structure and python.

I've used python before, for all of about 5 seconds when I built a [silly demo up on google app engine](http://sharksweaters.appspot.com).

### Running the Password Crack Demo

This is pretty straight forward, but involved some file editing on my part - i guess I had a lot of system accounts on my machine. I've included the output of `/etc/shadow` for a user on my machine (no, not root...). The `dictionary.txt` is also updated with three passwords one is used by the user in this demo and another used by the zip in the next demo.

Running the demo is pretty easy

    $ python crack.py

The user account and their hashed/salted password is stored in `passwords.txt`

### Running the Zip Password Crack Demo

To run the demos in this chapter, you'll need to create a zip file with a password and put some secrets in it. Luckily for you I've included a whole pile of secrets for you to use.

    $ zip --password <password> secure.zip secrets.txt

Whatever you typed for `<password>` needs to be added to the dictionary so the script can do it's thing. Then you can run the demo. You need to specify the zipfile `-f` and the dictionary `-d` to use.

    $ python unzip.py -f secure.zip -d dictionary.txt


