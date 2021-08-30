class PostConstants:
    """Store constants related to Post Page"""

    # Posts
    POST_TITLE_XPATH = './/*[@id="post-title"]'
    POST_BODY_CONTENT_XPATH = './/*[@class="body-content tall-textarea form-control"]'
    POST_SAVE_BUTTON_XPATH = './html/body/div[2]/form/button'
    POST_SUCCESS_MESSAGE_XPATH = './html/body/div[2]/div'
    POST_SUCCESS_MESSAGE_TEXT = 'New post successfully created.'
    POST_DELETE_BUTTON_XPATH = './/*[@class="delete-post-button text-danger"]'
    POST_EDIT_BUTTON_XPATH = ".//*[@data-original-title='Edit']"
    POST_SUCCESSFULLY_UPDATED_TEXT = 'Post successfully updated.'
    POST_SUCCESSFULLY_DELETED_TEXT = 'Post successfully deleted'
    POST_NAME_XPATH = './/h2'
