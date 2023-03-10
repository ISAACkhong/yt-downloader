from pytube import YouTube #for downloading videos
from colorama import Fore #for styling the colour of the text
from youtube_search import YoutubeSearch
import os

print(Fore.CYAN + "********YOUTUBE DOWNLOADER BY ISAACKHONG********")
input(Fore.WHITE + """Credits: IsaacKhong for the code.
Please enter your suggestions in the comments to improve this project. Press enter to continue,,,""")
os.system("clear")
lsChoice = input(Fore.CYAN + "Do you want to search or enter the link? (S for search, L for link) >> ")

choice = lsChoice.lower()
if choice == "l":
  link = input(Fore.CYAN + "Please enter the link >> ")
  try:
    yt = YouTube(link)
  except:
    print(Fore.RED + "Connection Error") 
  yt.streams.filter(progressive = True, file_extension = "mp4").first().download() 
  print(Fore.GREEN + "Request completed. Please enter the project to retrieve video in 'files'. Thank you for using.") 


elif choice == "s":
  linkList = []
  query = input(Fore.CYAN + "Search Query >> ")
  no = int(input(Fore.CYAN + "How many results do you want? >> "))
  results = YoutubeSearch(query, max_results=no).to_dict()
  index = 1
  for i in results:
    print(str(index) + ")")
    print()
    print("Title: " + i.get("title"))
    suffix = i.get("url_suffix")
    l = "youtube.com" + suffix
    print("Link: " + l)
    print("\n")
    linkList.append(l)
    index += 1
  userChoice = int(input("Which video do you want? Enter the number."))
  link = linkList[userChoice-1]



try:
    yt = YouTube(link)
except:
  print(Fore.RED + "Connection Error, please try again later.") 
yt.streams.filter(progressive = True, file_extension = "mp4").first().download() 
print(Fore.GREEN + "Request completed. Please enter the project to retrieve video in 'files'. Thank you for using.") 

