"""Build a feed for a community you choose.

See the course lab page for the demonstration checklist.
"""

from lab_classes import User, Tweet


def build_feed():
    # Create your accounts and posts, then call their methods.
    # Return the two lists: return users, posts
    user1 = User("tottenham")
    user2 = User("liverpoolfc")

    users = [user1, user2]

    post1 = Tweet("tottenham", "Ready for the next #PremierLeague match!")
    post2 = Tweet("liverpoolfc", "The Reds to take on Tottenham #YNWA")
    post3 = Tweet("tottenham", "Views from the South Stand. #COYS")

    posts = [post1, post2, post3]

    user1.follow()
    user1.follow()
    user2.follow()
    user1.unfollow()
    user1.follow()

    post1.like()
    post1.like()
    post2.like()
    post1.unlike()
    post3.like()
    post3.like()
    post1.like()

    return users, posts


def main():
    # Call build_feed and display the returned objects and hashtags.
    users, posts = build_feed()
    
    print("Users:")

    for user in users:
        print(user)
        print("Followers:", user.followers)

    print("Posts:")
    for post in posts:
        print(post)
        print(post.hashtags())
        print("Likes:", post.likes)


if __name__ == '__main__':
    main()
