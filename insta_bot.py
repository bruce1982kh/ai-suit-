from instagrapi import Client

def send_instagram_dm(username, password, target_user, message):
    cl = Client()
    try:
        cl.login(username, password)
        user_id = cl.user_id_from_username(target_user)
        cl.direct_send(message, [user_id])
        return f"Message sent to {target_user}"
    except Exception as e:
        raise Exception(f"Failed to send DM: {str(e)}")
