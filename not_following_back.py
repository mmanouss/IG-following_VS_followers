import json
import os

#Loads the following and followers JSON files from the Instagram data export
with open('following.json', 'r') as f:
  following = json.load(f)
with open('followers_1.json', 'r') as f:
  followers = json.load(f)

#Parses the given JSON file into a set of usernames
def parse_json(json_file, relationship):
    if type(json_file) == list:
      return {user['string_list_data'][0]['value'] for user in json_file}
    else:
      return {user['string_list_data'][0]['value'] for user in json_file[relationship]}
  
#Subtracts your followers from your following, to determine who you are following that isn't a also follower of yours 
not_following = parse_json(following, 'relationships_following') - parse_json(followers, 'relationships_followers')

#Checks if a previous instance of not_following exists, renames it to "old" if so
if os.path.exists("not_following_back.txt"):
    os.rename("not_following_back.txt", "old_not_following_back.txt")

#Writes the list of users to a text file
with open('not_following_back.txt', 'w') as f:
  f.writelines(sorted([username + '\n' for username in not_following]))
  
print("The list of users has been written to 'not_following_back.txt'.")

#Writes a file with the differences between the new and old instance of not_following, if an old one exists
if os.path.exists("old_not_following_back.txt"):
  with open('not_following_back.txt', "r") as file1, open('old_not_following_back.txt', "r") as file2, open("differences_included.txt", "w") as output_file:
      file1_contents = file1.readlines()
      file2_contents = file2.readlines()
      output_file.write("Who no longer follows you, that followed you previously:\n")
      for user in file1_contents:
          if user not in file2_contents:
              output_file.write(user)
      output_file.write("\nWho you no longer follow, that you followed previously:\n")
      for user in file2_contents:
          if user not in file1_contents:
              output_file.write(user)
  print("Differences between most recent comparison written to 'differences_included.txt'.")