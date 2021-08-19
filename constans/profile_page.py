class ProfilePage:
    """Store constants related to Profile page"""
    # Hello message
    HELLO_MESSAGE_TEXT = 'Hello {lower_username}, your feed is empty.'
    HELLO_MESSAGE_XPATH = './/h2'
    HELLO_MESSAGE_USERNAME_XPATH = ".//strong"

    # Sign out
    SIGN_OUT_BUTTON_TEXT = 'Sign Out'
    SIGN_OUT_BUTTON_XPATH = "./html/body/header/div/div/form/button"

    # Posts
    CREATE_POST_BUTTON_XPATH = './/*[@href="/create-post"]'
    POST_TITLE_XPATH = './/*[@id="post-title"]'
    POST_BODY_CONTENT_XPATH = './/*[@class="body-content tall-textarea form-control"]'
    POST_SAVE_BUTTON_XPATH = './html/body/div[2]/form/button'
    POST_SUCCESS_MESSAGE_XPATH = './html/body/div[2]/div'
    POST_SUCCESS_MESSAGE_TEXT = 'New post successfully created.'
    POST_DELETE_BUTTON_XPATH = './/*[@class="delete-post-button text-danger"]'
    POST_EDIT_BUTTON_XPATH = ".//*[@data-original-title='Edit']"
    POST_SUCCESSFULLY_UPDATED_TEXT = 'Post successfully updated.'
    POST_SUCCESSFULLY_DELETED_TEXT = 'Post successfully deleted'

    # Chat button
    CHAT_BUTTON_XPATH = './/*[@class="text-white mr-2 header-chat-icon"]'
    CHAT_TEXT_INPUT_XPATH = './/input[@id="chatField"]'
    CHAT_VERIFY_MESSAGE_XPATH = './/*[@class="chat-message-inner"]'
