# Followers vs. Following on Instagram #

### This script allows you to check who doesn't follow you back on Instagram, without any logging in through a third party required! ###

1. Log into Instagram on your web browser.
2. Navigate to **More** at the bottom left of the screen and then select **Settings** > **Accounts Center** at the top of the window > **Your information and permissions**, then select **Download your information**.
3. Click **Download or transfer information** > **All available information** > **Download to device**
4. Specific data fields should be filled out as follows:
   Date Range: **All time**
   Notify: **your email here**
   Format: **JSON**
   Media quality: **Low**
6. Once you receive your Instagram information, download it and navigate to the folder named "followers_and_following".
7. From that folder, drag "followers_1.json" and "following.json" into a folder with "not_following_back.py".

*NOTE: The file names might be slightly varied, ex. "followers.json". If this is the case, you must rename the file(s) to match the names mentioned in step 5.*

6. Run "not_following_back.py", and a text file containing the usernames of those who don't follow you back will be generated within the same folder :)
