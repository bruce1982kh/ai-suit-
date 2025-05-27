
from instagrapi import Client
import random
from ai_reply import generate_reply

# Initialize the client
def login_instagram(username, password):
    cl = Client()
    cl.login(username, password)
    return cl

# Send a direct message
def send_instagram_dm(username, password, target_user, message):
    cl = login_instagram(username, password)
    try:
        user_id = cl.user_id_from_username(target_user)
        cl.direct_send(message, [user_id])
        return f"✅ DM sent to {target_user}"
    except Exception as e:
        return f"❌ Failed to send DM: {str(e)}"

# Auto-follow users from a given username’s followers
def auto_follow_from_user(username, password, source_username, limit=5):
    cl = login_instagram(username, password)
    try:
        user_id = cl.user_id_from_username(source_username)
        followers = cl.user_followers(user_id)
        count = 0
        for user in followers.values():
            cl.user_follow(user.pk)
            count += 1
            if count >= limit:
                break
        return f"✅ Followed {count} followers of {source_username}"
    except Exception as e:
        return f"❌ Auto-follow failed: {str(e)}"

# Auto-like recent posts from a target account
def auto_like_posts(username, password, target_user, limit=5):
    cl = login_instagram(username, password)
    try:
        user_id = cl.user_id_from_username(target_user)
        medias = cl.user_medias(user_id, limit)
        for media in medias:
            cl.media_like(media.id)
        return f"✅ Liked {len(medias)} posts from {target_user}"
    except Exception as e:
        return f"❌ Auto-like failed: {str(e)}"

# Auto-comment using AI on recent posts from a target account
def auto_comment_with_ai(username, password, target_user, limit=3):
    cl = login_instagram(username, password)
    try:
        user_id = cl.user_id_from_username(target_user)
        medias = cl.user_medias(user_id, limit)
        for media in medias:
            ai_comment = generate_reply(f"Write a fun comment for an Instagram post by {target_user}", platform="instagram")
            cl.media_comment(media.id, ai_comment)
        return f"✅ Commented on {len(medias)} posts from {target_user}"
    except Exception as e:
        return f"❌ Auto-comment failed: {str(e)}"
