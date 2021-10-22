import requests

package = input("package: ")
getpackage = requests.get(f"https://radioactive.sudocode1.xyz/packages.php?{package}").text
receivedpackage = open(package + '.radio', "w")
receivedpackage.write(getpackage.replace('<br style="color: red;">', '\n'))
print("done!")