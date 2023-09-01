from insta_checker import InstaChecker

checker = InstaChecker()

checker.driver.get("https://www.instagram.com/")
checker.log_in()
print(checker.get_followers())
