from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page_button="//*[text()='Main page']"
    dev_team_contact="//a[contains(@href, 'client')]"
    add_player_hyperlink= "//a[contains(@href, 'add')]"
    sign_out="//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"
    choose_language="//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]"
    players="//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]"
    go_to_last_created_player="//div[3]/div/div/a[1]"
    go_to_last_updated_player ="//div/a[2]"
    go_to_last_created_match ="//div/a[3]"
    go_to_last_updated_report="//div/a[5]]"
pass
