from pages.base_page import BasePage


class add(BasePage):
    fill_in_email="//*[@name='email']"
    fill_in_name="//*[@name='name']"
    choose_leg="//*[ @ id = 'mui-component-select-leg']"
    submit_button="//*[@type='submit']"
    clear_button="//*[contains(@class, 'MuiButton-containedSecondary')]"
    add_link_to_youtube="//*[@aria-label='Add link to Youtube']"
    fill_in_weight="(//*[@type='number'])[1]"
    fill_in_height ="(//*[@type='number'])[2]"
    main_position="//*[@name='mainPosition']"
    choose_district="//*[contains(@id,'select-district')]"
pass
