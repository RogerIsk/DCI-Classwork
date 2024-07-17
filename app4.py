class FileHandler:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.file_path, self.mode)
        except Exception as e:
            print(f"Error opening file: {e}")
            raise
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            try:
                self.file.close()
            except Exception as e:
                print(f"Error closing file: {e}")
                raise
        if exc_type is not None:
            print(f"An exception occurred: {exc_type}, {exc_val}")
        # Returning False will re-raise the exception if it occurred
        return False


# Usage example
if __name__ == "__main__":
    # Writing to the file
    with FileHandler('sample.txt', 'w') as file:
        file.write('Hello, World!')

    # Reading from the file
    with FileHandler('sample.txt', 'r') as file:
        content = file.read()
        print(content)