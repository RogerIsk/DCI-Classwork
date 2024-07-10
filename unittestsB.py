import pytest
from unittestsA import UserLoginSystem



# tests if login possible after registering
def test_register_login_success():
    login_system = UserLoginSystem() # create object first
    login_system.register("user1", "password1") # test methods on object
    assert login_system.login("user1", "password1") # assert that it worked

# test if register possible and fails if using existing username
def test_register_existing_user():
    login_system = UserLoginSystem() # create object first
    login_system.register("user1", "password1") # test methods on object
    with pytest.raises(ValueError, match="User already exists"): # expect error
        login_system.register("user1", "password2")              # if this happens

# test if login to nonexistent user doesnt work
def test_login_nonexistent_user():
    login_system = UserLoginSystem() # create object first
    with pytest.raises(ValueError, match="User does not exist"): # expect error
        login_system.login("user1", "password1")                 # if this happens

# test if login with incorrect password fails
def test_login_incorrect_password():
    login_system = UserLoginSystem() # create object first
    login_system.register("user1", "password1") # test methods on object
    with pytest.raises(ValueError, match="Incorrect password"): # expect error
        login_system.login("user1", "wrong_password")           # if this happens


# Run the 