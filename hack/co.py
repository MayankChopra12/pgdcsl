username = "John"

passwords = [
    "Secure", "Pass1", "Locky", "Keyed", "P@55w", "Code5", "Safes", "Vault", "Entry", "Hush1", 
    "Unloc", "Guard", "Safe4", "Keyup", "Lock6", "Passy", "Keys7", "Secur", "Cloak", "C0d3s", 
    "Pword", "Secret", "Open9", "Lock3", "CodeX", "Guard", "Lockz", "Entr4", "P@ssy", "Vault", 
    "Secre", "Saf3s", "SafeT", "Pass8", "K3ys!", "Unloc", "Cloak", "Keyed", "Guard", "Lock5", 
    "P@55s", "Passz", "Secure7", "Pass123", "Unlock7", "Secret1", "room", "Access7", "Guard99", 
    "KeyPass", "Lock987", "SafePwd", "Code123", "Vault77", "Shield7", "Login22", "HackOff", 
    "Blocker", "SecureX", "Cipher9", "Defend7", "Access1", "poster", "bugbounty", "basicpentest", 
    "linux", "GuardMe", "LockIt8", "SafeHub", "PassKey", "CodeMe7", "Vaulted", "ShieldX", 
    "Entry24", "HackNo1", "BlockX9", "SecureZ", "GuardUp", "Unlock1", "DefendX", "AccessX", "KeyLock"
]

file_content = "\n".join([f"{username}:{password}" for password in passwords])

with open("output.txt", "w") as file:
    file.write(file_content)

print("File 'output.txt' has been created.")
