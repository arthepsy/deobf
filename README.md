# deobfuscate passwords
Some "encrypted" passwords are actually obfuscated and leads to **false sense of security**.

### JetBrains WebStorm
Stored passwords can be found in `webServers.xml` file.  
This utility is both Python 2 and Python 3 compatible, without any dependencies.  

* Obfuscate (_encrypt_) password:  
  ```
  ./webstorm.obf.py -e Password
  dffadfcbdfd9dfd9dfdddfc5dfd8dfce
  ```

* Deobfuscate (_decrypt_) password:  
  ```
  ./webstorm.obf.py -d dffadfcbdfd9dfd9dfdddfc5dfd8dfce
  Password
  ```

