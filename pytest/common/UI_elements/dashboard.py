from seleniumpagefactory.Pagefactory import PageFactory

class DashboardPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'top_nav': ('xpath', "//*[@id='root']/div/div/div[1]/div[2]/ul/li[1]/a"),
        'new_alerts': ('xpath', "//*[@id='root']/div/div/div[2]/div/div[3]/div[2]/div[1]/a"),
        'new_hosts': ('xpath', "//*[@id='root']/div/div/div[2]/div/div[3]/div[2]/div[2]/a"),
        'new_admins': ('xpath', "//*[@id='root']/div/div/div[2]/div/div[3]/div[2]/div[3]/a"),
        'new_applications': ('xpath', "//*[@id='root']/div/div/div[2]/div/div[3]/div[2]/div[4]/a"),
        'threat_compromised_hosts': ('xpath', "//*[@id='root']/div/div/div[2]/div/div[4]/div[2]/div[1]/a"),
        'threat_malicious_files': ('xpath', "//*[@id='root']/div/div/div[2]/div/div[4]/div[2]/div[2]/a"),
        'threat_memory_injections': ('xpath', "//*[@id='root']/div/div/div[2]/div/div[4]/div[2]/div[3]/a"),
        'threat_compromised_accounts': ('xpath', "//*[@id='root']/div/div/div[2]/div/div[4]/div[2]/div[4]/a"),
        'vulns_risks_applications': ('xpath', "//*[@id='root']/div/div/div[2]/div/div[6]/div[1]/a"),
        'vulns_risks_vulnerable_applications': ('xpath', "//*[@id='root']/div/div/div[2]/div/div[6]/div[2]/a"),
        #removed 'vulns_risks_critical_vulnerabilities': ('xpath', "//*[@id='root']/div/div/div[2]/div/div[5]/div[2]/a[3]"),
        'vulns_risks_admin_accounts': ('xpath', "//*[@id='root']/div/div/div[2]/div/div[6]/div[3]/a")
    }

    def click_top_nav(self):
        self.top_nav.click()

    def click_new_alerts(self):
        self.new_alerts.click()


    def click_new_hosts(self):
        self.new_hosts.click()

    def click_new_admins(self):
        self.new_admins.click()

    def click_new_applications(self):
        self.new_applications.click()

    def click_threat_compromised_hosts(self):
        self.threat_compromised_hosts.click()

    def click_threat_malicious_files(self):
        self.threat_malicious_files.click()

    def click_threat_memory_injections(self):
        self.threat_memory_injections.click()

    def click_threat_compromised_accounts(self):
        self.threat_compromised_hosts.click()

    def click_vulns_risks_applications(self):
        self.vulns_risks_applications.click()

    def click_vulns_risks_vulnerable_applications(self):
        self.vulns_risks_vulnerable_applications.click()

    """
    def click_vulns_risks_critical_vulnerabilities(self):
        self.vulns_risks_critical_vulnerabilities.click()
    """
        
    def click_vulns_risks_admin_accounts(self):
        self.vulns_risks_admin_accounts.click()

    

    