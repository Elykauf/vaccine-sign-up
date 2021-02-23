# vaccine-sign-up

This script was created to text you when a vaccine volenteer sign up slot fills up. It uses twilio as a texting service.


# To Run
Ensure python 3 is installed with the packages twilio, requests and beautfulsoup.

replace the keys with your twilio account keys.
Plug your phone number or whoever you want to get the texts in.

set and forget!

# Notes
I ran this script in the background of a google cloud tiny vm instance. If you run it on a computer, it will have to be running 24/7.
Twilio cost a little bit to text unverified numbers. You will be able to text the number you signed up with for free.
