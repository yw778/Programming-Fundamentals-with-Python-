import webbrowser
import time

print("this program started" + time.ctime());
i = 0;
while i < 3:
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/user/algorithmscourses/playlists?view=50&shelf_id=3&sort=dd")
	i = i + 1;