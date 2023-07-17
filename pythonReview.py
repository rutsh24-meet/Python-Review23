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
SEVEN = "7"


def main_menu():
    menu = """
MAIN MENU:
1. Add likes
2. Add dislikes
3. Comment 
4. See stats
5. Create new video
6. Find similarity
7. Exit"""
    print(menu)
    choice = input("Enter choice of action: ")

    while choice not in ["1", "2", "3", "4", "5", "6"]:
        choice = input("Invalid - Try again: ")
    return choice


def create_youtube_video():
    print(LOADING)
    title = input("Enter title of video: ")
    description = input("Enter description of video: ")
    words = []
    print("Enter up to 5 words to describe the video: ")
    for i in range(5):
        word = input(" -> ")
        words.append(word)
    new_video = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {},
                 "hashtag": words}
    print(new_video)
    return new_video


def like(video):
    if "likes" in video:
        video["likes"] += 1
        print("Like added!")
        return video
    print(LIKE_ERROR)


def add_many_likes(video):
    if "likes" in video:
        num = input("Enter number of likes to add: ")
        if not num.isnumeric():
            print("Invalid option...")
            print("Returning to main")
            return
        for i in range(int(num)):
            video["likes"] += 1


def dislike(video):
    if "dislikes" in video:
        video["dislikes"] += 1
        print("Dislike added!")
        return video
    print(DISLIKE_ERROR)


def add_many_dislikes(video):
    if "dislikes" in video:
        num = input("Enter number of dislikes to add: ")
        if not num.isnumeric():
            print("Invalid option...")
            print("Returning to main")
            return
        for i in range(int(num)):
            video["dislikes"] += 1


def add_comment(video, username, comment_text):
    video["comments"][username] = comment_text
    return video


def see_stats(video):
    title = video["title"]
    des = video["description"]
    likes = str(video["likes"])
    dislikes = video["dislikes"]
    comments = video["comments"]
    hashtag = video["hashtag"]
    sep = " #"
    hash_str = "#" + sep.join(hashtag)
    print("\nTITLE:", title)
    print("DESCRIPTION:", des)
    print("NUMBER OF LIKES:", likes)
    print("NUMBER OF DISLIKES:", dislikes)
    print("HASHTAGS:", hash_str)
    print("COMMENTS:")
    print("---------")
    for key in comments:
        print(key + " - " + comments[key])


def similarity_to_video(video_one, video_two):
    sim_perc = 0
    list_one = video_one["hashtag"]
    list_two = video_two["hashtag"]
    print(list_one)
    print(list_two)
    for word in list_one:
        print(word)
        if word in list_two:
            sim_perc += 1
    sim_perc = sim_perc * 20
    msg = f'The videos {video_one["title"]} and {video_two["title"]} are {str(sim_perc)}% similar'
    print(msg)


def main():
    vid_list = []
    choice = 0
    print(WELCOME)
    youtube_video = create_youtube_video()
    vid_list.append(youtube_video)
    print(vid_list)
    while choice != SEVEN:
        choice = main_menu()
        if choice == ONE:
            like_choice = input("To add many likes press 1, anything else for automatic add: ")
            if like_choice == ONE:
                add_many_likes(youtube_video)
            else:
                youtube_video = like(youtube_video)
        elif choice == TWO:
            dislike_choice = input("To add many dislikes press 1, anything else for automatic add: ")
            if dislike_choice == ONE:
                add_many_dislikes(youtube_video)
            else:
                youtube_video = dislike(youtube_video)
        elif choice == THREE:
            username = input("Enter username: ")
            text = input("Enter text: ")
            youtube_video = add_comment(youtube_video, username, text)
        elif choice == FOUR:
            see_stats(youtube_video)
        elif choice == FIVE:
            pass
        elif choice == SIX:
            similarity_to_video(temp, youtube_video)
    print(GOODBYE)


if __name__ == '__main__':
    main()
