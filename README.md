vkusersonline
=============

How many users are online in specified vk.com group?

Step 1. Input you groups in vkuoconfig.py

Step 2. Run vkuo.py and log in. If you use python 2, the email must be in quotes.

Step 3. Wait until the script stops or you tired. You can stop it any time, the data will not lost.

Step 4. Run vkuoplot.py with collected data file as parameter, to view the time plot. For example:

./vkuoplot.py myfriends_online.txt

You also can specify more than one file to plot them all in one figure.


Dependencies: vk_api (sudo easy_install3 vk_api), requests (sudo apt-get install python3-requests or sudo easy_install3 requests).
