httpq
=====

This is a quick tool is use when I target large scope while doing bug hunting. It helps me to check page status/title.
I often use it after [httprobe](https://github.com/tomnomnom/httprobe) or other testing tools.

## Description

When you have a large scope of URLs to test you need to know if you get redirected or if you found a legitimate URL. This tool helps you to find low hanging fruits by displaying the HTTP code and the Web page title (e.g. admin portal, etc.).

**Note: ** You need to have a list prepended with the protocol, like **http://** or **https://**.

Here is a quick example without redirection:

```bash
python3 httpq.py sample.txt 
[+] https://www.google.com/ - 200 (OK) - Google
[+] https://www.youtube.com/ - 200 (OK) - YouTube
[+] https://careers.google.com/ - 200 (OK) - Build for Everyone - Google Careers
[+] https://maps.google.com/ - 302 (Found) - 302 Moved
```

```bash
Here is another example with redirection:
➜  httpq git:(master) ✗ python3 httpq.py sample.txt -r
[+] https://www.google.com/ - 200 (OK) - Google
[+] https://www.youtube.com/ - 200 (OK) - YouTube
[+] https://careers.google.com/ - 200 (OK) - Build for Everyone - Google Careers
[+] https://www.google.com/maps - 200 (OK) -  Google Maps 
```

## Installation

This tool requires some modules. You can install them by running the following commands:

```bash
$ git clone https://github.com/axcheron/httpq.git
$ cd httpq
$ pip3 install -r requirements.txt
```

## License

This project is released under the Apache 2 license. See LICENCE file.
