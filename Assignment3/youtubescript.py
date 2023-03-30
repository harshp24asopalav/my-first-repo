# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.youtube.com")
time.sleep(3)

#sign in
sign_in = driver.find_element("xpath","/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
sign_in.click()
time.sleep(3)

# #Close ad banner
# ad_close=driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[3]/ytd-banner-promo-renderer/div/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
# ad_close.click()
# time.sleep(3)
#
# #open shorts
# shorts_button = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[2]/a/yt-icon")
# shorts_button.click()
# time.sleep(3)
#
# #like the video
# like_button = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[2]/div[2]/ytd-reel-video-renderer[1]/div[3]/ytd-reel-player-overlay-renderer/div[2]/div[3]/ytd-like-button-renderer/ytd-toggle-button-renderer[1]/yt-button-shape/label/button/yt-touch-feedback-shape/div/div[2]")
# like_button.click()
# time.sleep(3)
#
# #sign in prompt
# sign_in = driver.find_element("xpath","/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-modal-with-title-and-button-renderer/div/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
# sign_in.click()
# time.sleep(3)

#sign in to google
email = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
email.send_keys("seleniumtestingfor8040@gmail.com")
# Click enter
email.send_keys(Keys.RETURN)
time.sleep(1)

#show passwords
show = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div/div")
show.click()


enter_password = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
enter_password.send_keys("DEMOaccount")
enter_password.send_keys(Keys.RETURN)
time.sleep(3)

# #GO TO library
# open_library = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-mini-guide-renderer/div/ytd-mini-guide-entry-renderer[4]/a/span")
# open_library.click()
# time.sleep(3)
#
# #click on browse videos
# browse_video = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-shelf-renderer/div[1]/div[1]/yt-formatted-string/a")
# browse_video.click()
# time.sleep(3)

#search for video
search_bar =driver.find_element("xpath","/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
search_bar.send_keys("odhaji jigrra")
search_bar.send_keys(Keys.RETURN)
time.sleep(3)
# Verifying that the search results page has loaded
#assert "odhaji jigrra" in driver.title

# Selecting a song from the search results

song_link = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-image/img")
song_link.click()

# # # Waiting for the song to load and ad to finish
time.sleep(20)

click_on_like_button = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/ytd-segmented-like-dislike-button-renderer/div[1]/ytd-toggle-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
click_on_like_button.click()
time.sleep(5)

#click on options
three_bars = driver.find_element("xpath","/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[1]/yt-icon-button[2]/button/yt-icon")
three_bars.click()
like_videos = driver.find_element("xpath","/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-collapsible-section-entry-renderer/div[2]/ytd-guide-entry-renderer[3]/a/tp-yt-paper-item/yt-formatted-string")
like_videos.click()
time.sleep(3)

#verify that video has been added to liked videos library
library = driver.find_element("xpath","/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[1]/div[1]/ytd-playlist-byline-renderer/div/yt-formatted-string[1]")
assert library.text == "1 video"
driver.close()
# # # Clicking on copy link button
# copy_link_button = driver.find_element("xpath","/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown[2]/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer[1]/tp-yt-paper-item")
# copy_link_button.click()
#
# time.sleep(15)
# #nothanks = driver.find_element("xpath","/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-mealbar-promo-renderer/div/div[2]/yt-button-renderer[1]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]")
# #nothanks.click()
# # time.sleep(9)
# # sign_in_button=driver.find_element("xpath","/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown[3]/div/ytd-modal-with-title-and-button-renderer/div/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[1]")
# # sign_in_button.click()
# time.sleep(2)
# # # Verifying that the laptop has been added to the cart
# # cart_count = driver.find_element("id","nav-cart-count")
# # assert cart_count.text == "1"
#
# # Closing the webdriver
# #driver.close()

