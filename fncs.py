#!/usr/bin/python3
#https://github.com/rxfa
import sys
from colorama import Fore, Style

app_name = sys.argv[0]

def main():
    wordlist = sys.argv[1]
    try:
        target = int(input("Get words of how many characters? "))
        with open(wordlist, "r", encoding="utf8", errors="ignore") as file:
            if "." in wordlist:
                split_filename = wordlist.split(".")
                split_filename = split_filename[0]
            
            open("filtered.txt", "x")
            output = open("filtered.txt", "w")
            for line in file:
                if len(line.strip()) == target:
                    output.write(line)
            output.close()
        print(f"[+] {Fore.GREEN}{wordlist} filtered sucessfully!{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"[-] {Fore.RED}{wordlist} could not be found.{Style.RESET_ALL}")
    except FileExistsError:
        print(f"[-] {Fore.RED}{split_filename}_filtered.txt already exists.{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"[-] {Fore.RED}{app_name} requires two arguments!{Style.RESET_ALL}")
        print(f"[-] Usage: {app_name} <wordlist>")
    else:
        main()