def test_read_configfile(read_configfile):
  if read_configfile.configFile == 'qa.ini':
    assert read_configfile.getGmailURL() == 'qa.gmail.com'
    assert read_configfile.getGmailUserName() == 'qa@gmail.com'

  elif read_configfile.configFile == 'prod.ini':
    assert read_configfile.getOutlookURL() == 'prod.outlook.com'
    assert read_configfile.getOutlookUserName() == 'prod@outlook.com'