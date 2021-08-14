class LoginPageConstants:
    """
    Store constants related to Login Page
    """

    # Sign Up
    SIGN_UP_USERNAME_XPATH = './/input[@id="username-register"]'
    SIGN_UP_EMAIL_XPATH = './/input[@name="email"]'
    SIGN_UP_PASSWORD_XPATH = './/input[@name="password" and @id="password-register"]'
    SIGN_UP_BUTTON_XPATH = './/*[contains(text(),"Sign up for OurApp")]'

    # Sign In
    SIGN_IN_USERNAME_XPATH = './html/body/header/div/form/div/div[1]/input'
    SIGN_IN_PASSWORD_XPATH = ".//input[@class='form-control form-control-sm input-dark' and @name='password']"
    SIGN_IN_BUTTON_XPATH = ".//button[@class='btn btn-primary btn-sm']"

    # Messages
    INVALID_SIGN_IN_MESSAGE_TEXT = 'Invalid username / password'
    ALERT_USERNAME_3_CHARS_TEXT = 'Username must be at least 3 characters.'
    ALERT_USERNAME_ONLY_LET_AND_DIG_TEXT = "Username can only contain letters and numbers."
    ALERT_USERNAME_ALREADY_TAKEN_TEXT = 'That username is already taken.'
    ALERT_USERNAME_MAX_LENGTH_TEXT = 'Username cannot exceed 30 characters.'
    ALERT_EMAIL_VALID_EMAIL_TEXT = 'You must provide a valid email address.'
    ALERT_PASSWORD_MIN_LENGTH_TEXT = "Password must be at least 12 characters."
    ALERT_PASSWORD_MAX_LENGTH_TEXT = "Password cannot exceed 50 characters"
    SIGN_UP_ALERT_XPATH = './/*[@class="alert alert-danger small liveValidateMessage liveValidateMessage--visible"]'
    SIGN_IN_ALERT_XPATH = './/html/body/div[2]/div[1]'

