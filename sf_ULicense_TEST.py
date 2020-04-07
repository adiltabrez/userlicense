# Essential Imports (packages, lib, etc.)
from simple_salesforce import Salesforce
import pandas as pd
import creds

def getLicSummary():

    # Variable Declarations
    q_license_name = (
        "SELECT Name, UsedLicenses, TotalLicenses FROM UserLicense WHERE Name IN ('Salesforce Platform','Customer Community')")
    q_org_name = creds.orgname
    q_profile_name = ("SELECT Id FROM User WHERE Profile.Name ='System Administrator' AND IsActive=true")

    # Salesforce Connection
    sf_DEV = Salesforce(
        username=creds.username,
        password=creds.password,
        security_token=creds.sectocken)

    # Getting the Total Profile Count
    d_prof_data = sf_DEV.query_all(q_profile_name)
    d_prof_df = pd.DataFrame(d_prof_data['records']).drop(columns='attributes')
    profilecount = d_prof_df.shape[0]

    d_lic_data = sf_DEV.query_all(q_license_name)
    d_lic_df = pd.DataFrame(d_lic_data['records']).drop(columns='attributes')
    remliccount = d_lic_df["TotalLicenses"] - d_lic_df["UsedLicenses"]

    d_lic_df.insert(3, "Remaining Licenses", remliccount)
    d_lic_df.insert(3, "Profile Count", profilecount)
    d_lic_df.insert(0, "Client Name", q_org_name)
    d_lic_df.rename(
        columns={'Name': 'License Name', 'TotalLicenses': 'Total Licenses', 'UsedLicenses': 'Used Licenses'},
        inplace=True
    )
    d_lic_df = d_lic_df[
        ['Client Name', 'License Name', 'Total Licenses', 'Used Licenses', 'Remaining Licenses', 'Profile Count']]
    print(d_lic_df)

getLicSummary()