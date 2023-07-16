WELCOME = "Welcome to YouTube!"
LIKE_ERROR = "ERROR: no option for likes found..."
DISLIKE_ERROR = "ERROR: no option for dislikes found..."
GOODBYE = "Goodbye! come again soon!"
LOADING = "Creating video"

ONE = "1"
TWO = "2"
THREE = "3"
FOUR = "4"
FIVE = "5"
SIX = "6"


def main_menu():
    menu = """
MAIN MENU:
1. Add likes
2. Add dislike
3. Comment 
4. See stats
5. Create new video
6. Exit"""
    print(menu)
    choice = input("Enter choice of action: ")

    while choice not in ["1", "2", "3", "4", "5", "6"]:
        choice = input("Invalid - Try again: ")
    return choice


def create_youtube_video():
    print(LOADING)
    title = input("Enter title of video: ")
    description = input("Enter description of video: ")
    new_video = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}}
    return new_video


def like(video):
    if "likes" in video:
        video["likes"] += 1
        print("Like added!")
        return video
    print(LIKE_ERROR)


def add_many_likes(video):
    pass


def dislike(video):
    if "dislikes" in video:
        video["dislikes"] += 1
        print("Dislike added!")
        return video
    print(DISLIKE_ERROR)


def add_comment(video, username, comment_text):
    video["comments"][username] = comment_text
    return video


def see_stats(video):
    title = video["title"]
    des = video["description"]
    likes = str(video["likes"])
    dislikes = video["dislikes"]
    comments = video["comments"]
    print("\nTITLE:", title)
    print("DESCRIPTION:", des)
    print("NUMBER OF LIKES:", likes)
    print("NUMBER OF DISLIKES:", dislikes)
    print("COMMENTS:")
    print("---------")
    for key in comments:
        print(key + " - " + comments[key])


def main():
    choice = 0
    print(WELCOME)
    youtube_video = create_youtube_video()
    while choice != SIX:
        choice = main_menu()
        if choice == ONE:
            youtube_video = like(youtube_video)
        elif choice == TWO:
            youtube_video = dislike(youtube_video)
        elif choice == THREE:
            username = input("Enter username: ")
            text = input("Enter text: ")
            youtube_video = add_comment(youtube_video, username, text)
        elif choice == FOUR:
            see_stats(youtube_video)
    print(GOODBYE)


if __name__ == '__main__':
    main()
