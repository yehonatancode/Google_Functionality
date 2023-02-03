from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class GoogleSearchFunc:

    def search_functionality(self):
        # Create an instance of the Chrome webdriver
        driver = webdriver.Chrome()

        # Navigate to the Google homepage
        driver.get("https://www.google.com/")

        # Find the search box and enter a query
        search_box = driver.find_element(by=By.XPATH,
                                         value='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search_box.send_keys("Albert Einstein")

        # Submit the query by hitting enter
        search_box.send_keys(Keys.RETURN)

        # Verify that the search results contain the query
        assert "albert einstein" in driver.page_source

        # Select a suggestion from the suggestion list, we chose arbitrarily 'albert einstein iq'
        suggestion = driver.find_element(by=By.XPATH, value='//*[@id="tsf"]/div[1]/div[1]/div[2]/div/div[2]/input')
        suggestion.click()
        einstein_iq_element = driver.find_element(by=By.XPATH,
                                                  value='//*[@id="tsf"]/div[1]/div[1]/div[3]/div[2]/div[2]/div[1]/div/ul/li[11]/div/div[2]/div[1]/span')
        einstein_iq_element.click()

        # Verify that the search results contain the suggestion
        assert "albert einstein iq" in driver.page_source
        print("albert einstein iq" in driver.page_source)

        # Close the webdriver instance
        driver.close()

    def run_all(self):
        self.search_functionality()



