class ProfilePage:
    """Store constants related to Profile page"""
    # Hello message
    HELLO_MESSAGE_TEXT = 'Hello {lower_username}, your feed is empty.'
    HELLO_MESSAGE_XPATH = './/div[@class="text-center"]//h2'
    HELLO_MESSAGE_USERNAME_XPATH = ".//strong"

    # Sign out
    SIGN_OUT_BUTTON_TEXT = 'Sign Out'
    SIGN_OUT_BUTTON_XPATH = "./html/body/header/div/div/form/button"

    # Posts
    CREATE_POST_BUTTON_XPATH = './/*[@href="/create-post"]'
    POST_TITLE_XPATH = './/*[@class="form-control form-control-lg form-control-title"]'
    POST_BODY_CONTENT_XPATH = './/*[@class="body-content tall-textarea form-control"]'
    POST_SAVE_BUTTON_XPATH = './html/body/div[2]/form/button'
    POST_SUCCESS_MESSAGE_XPATH = './html/body/div[2]/div[1]'
    POST_SUCCESS_MESSAGE_TEXT = 'New post successfully created.'
