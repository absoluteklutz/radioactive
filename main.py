import requests

package = input("package: ")
getpackage = requests.get(f"https://radioactive.sudocode1.xyz/packages/{package}.radio").text
receivedpackage = open(package + '.radio', "w")
receivedpackage.write(getpackage)
print("done!")
