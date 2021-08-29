class ProfilePageConstants:
    """Store constants related to Profile page"""

    # Hello message
    HELLO_MESSAGE_TEXT = 'Hello {lower_username}, your feed is empty.'
    HELLO_MESSAGE_XPATH = './/h2'
    HELLO_MESSAGE_USERNAME_XPATH = ".//strong"

    # Posts in my profile
    POST_NAMES_XPATH = './/strong'

    # Sign out
    SIGN_OUT_BUTTON_TEXT = 'Sign Out'
    SIGN_OUT_BUTTON_XPATH = "./html/body/header/div/div/form/button"

    # Posts
    CREATE_POST_BUTTON_XPATH = './/*[@href="/create-post"]'

    # Chat button
    CHAT_BUTTON_XPATH = './/*[@class="text-white mr-2 header-chat-icon"]'

    # My profile
    MY_PROFILE_BUTTON_XPATH = './/a[@href="/profile/{lower_username}"]'

    # Search
    SEARCH_BUTTON_XPATH = './/*[@data-original-title="Search"]'
    SEARCH_INPUT_FIELD_XPATH = './/input[@id="live-search-field"]'
    SEARCH_RESULT_MESSAGE_XPATH = './/strong'
    SEARCH_RESULT_XPATH = './/html/body/div[4]/div[2]/div/div[2]/div/div'
    SEARCH_CLOSE_BUTTON_XPATH = './/*[@class="close-live-search"]'
