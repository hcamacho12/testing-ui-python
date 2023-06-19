from seleniumpagefactory.Pagefactory import PageFactory

class DiscoverPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'top_nav': ('xpath', "//*[@id='root']/div/div/div[1]/div[2]/ul/li[3]/a"),
        'add_target_group': ('xpath', "//*[@id='root']/div/div/div[2]/div[2]/div/div[1]/div[2]/button"),
        'create_target_dialog_target_name': ('xpath', "//*[@id='target-group-dialog']/div[1]/div/input"),
        'create_target_dialog_controller_group': ('xpath', "//*[@id='target-group-dialog']/div[2]/div/div[2]/div"),
        'create_target_dialog_monitored_radio': ('xpath', "//*[@id='target-group-dialog']/fieldset/div/label[1]/span[1]/input"),
        'create_target_dialog_scheduled_radio': ('xpath', "//*[@id='target-group-dialog']/fieldset/div/label[2]/span[1]/input"),
        'create_target_dialog_no_schedule_radio': ('xpath', "//*[@id='target-group-dialog']/fieldset/div/label[3]/span[1]/input"),
        'create_target_dialog_scheduled_frequency': ('xpath', "//*[@id='target-group-dialog']/div[3]/div[1]/div[1]/div/div/div[2]/div"),
        'create_target_dialog_scheduled_time_hours': ('xpath', "//*[@id='target-group-dialog']/div[3]/div[1]/div[2]/div/div[1]/div/div/input"),
        'create_target_dialog_scheduled_time_minutes': ('xpath', "//*[@id='target-group-dialog']/div[3]/div[1]/div[2]/div/div[2]/div/div/input"),
        'create_target_dialog_scheduled_time_ampm': ('xpath', "//*[@id='target-group-dialog']/div[3]/div[1]/div[2]/div/div[3]/div/div/div[2]/div"),
        'create_target_dialog_extension_options': ('xpath', "//*[@id='target-group-dialog']/div[4]/div[1]/button"),
        'create_target_dialog_extension_options_search_text': ('xpath', "//*[@id='target-group-dialog']/div[4]/div[2]/div[1]/div/div/div/input"),
        'create_target_dialog_extension_options_search_button': ('xpath', "//*[@id='target-group-dialog']/div[4]/div[2]/div[1]/div/div/button"),
        'create_target_dialog_cancel_button': ('xpath', "/html/body/div[2]/div[3]/div/div[5]/button[1]"),
        'create_target_dialog_save_button': ('xpath', "/html/body/div[2]/div[3]/div/div[5]/button[2]"),
        'target_group_action_menu_button': ('xpath', "//*[@id='root']/div/div/div[2]/div[2]/div/div[2]/div[2]/div/button"),
        'target_group_action_menu_delete_button': ('xpath', "/html/body/div[2]/div[3]/ul/li[5]"),
        'target_group_delete_modal_delete_button': ('xpath', "/html/body/div[2]/div[3]/div/div[5]/button[2]"),
        'target_group_query_tab': ('xpath', "//*[@id='root']/div/div/div[2]/div[2]/div/div[3]/ul/li[2]")
    }

    def click_top_nav(self):

        self.top_nav.click()

    #----- add target group workflow ------

    def click_add_target_group(self):

        self.add_target_group.click()

    def enter_target_group_name(self, target_group_name):
        """
            30 character limit for target group name
        """

        self.create_target_dialog_target_name.click()

        self.create_target_dialog_target_name.set_text(target_group_name)

    def select_controller_group(self):
        """todo
        """
        pass

    def click_schedule_radio(self, option):
        """
            only one schedule option can be selected per target group created
        """
        if option == 'monitored':
            self.create_target_dialog_monitored_radio.click() 
        elif option == 'scheduled':
            self.create_target_dialog_scheduled_radio.click()
        elif option == 'not-scheduled':
            self.create_target_dialog_no_schedule_radio.click()
        else:
            raise Exception(f"Unexpected radion option value: {option}")


    def set_sched_scan_freq_and_time(self, frequency, hours, minutes, ampm):
        """
        when scheduled radion option is selected user must set:
            scheduled scan frequency - daily, weekly, or monthly
            time > Hours - set hour value for schedule
            time > minutes - set minute value for schedule
            ampm - specify is time set  is am or pm
            
        """

        #set frequency value
        self.create_target_dialog_scheduled_frequency.click()
        #set time hours value
        #set time minutes value
        #set am/pm

    def click_tg_save_button(self):

        self.create_target_dialog_save_button.click()

    def click_tg_action_menu_delete(self):

        self.target_group_action_menu_button.click()
        self.target_group_action_menu_delete_button.click()
        self.target_group_delete_modal_delete_button.click()

    #----- target group query workflow -----

    def click_target_group_query_tab(self):

        self.target_group_query_tab.click()