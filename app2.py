import getopt
import sys

def main():
    help_text = """
    Usage: python app2.py [OPTIONS]
    Options:
        -h, --help      Display this help message
        -n NAME, --name=NAME  Greet the specified NAME
    """
    try:
        # Define the command line options the script accepts
        opts, args = getopt.getopt(sys.argv[1:], 'hn:', ['help', 'name='])
    except getopt.GetoptError as err:
        # Handle any option errors
        print(err)
        print(help_text)
        sys.exit(2)

    name = None  # Default if no name is provided
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help_text)
            sys.exit()
        elif opt in ('-n', '--name'):
            name = arg  # Set the name if provided

    # Personalize greeting based on whether a name was provided
    if name:
        print(f"Good Morning {name}!")
    else:
        print("Good Morning folks!")

if __name__ == "__main__":
    main()