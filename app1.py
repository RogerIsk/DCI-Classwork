import sys

def main():
    help_text = """
    Usage: python app1.py [OPTIONS]
    Options:
        --help          Display this help message
        --fast          Enable fast mode
        --version       Display the version
    """
    
    if '--help' in sys.argv:
        print(help_text)
    elif '--fast' in sys.argv:
        print("fast mode enabled")
    elif '--version' in sys.argv:
        print("v1.0.0")
    elif '--verbose' in sys.argv:
        print("verbose mode enabled")
    else:
        print("slow mode enabled")
        

if __name__ == "__main__":
    main()