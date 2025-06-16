import ast
import argparse

# This is a new Python module for code analysis.
# It will contain functions to analyze Python code.

def check_syntax(code_string: str):
    """
    Checks the syntax of a string of Python code.

    Args:
        code_string: The Python code to check.

    Returns:
        A tuple (syntax_ok, error_message).
        If syntax is valid, syntax_ok is True and error_message is None.
        If a SyntaxError occurs, syntax_ok is False and error_message is the string representation of the error.
    """
    try:
        ast.parse(code_string)
        return (True, None)
    except SyntaxError as e:
        return (False, str(e))

def execute_code(code_string: str):
    """
    Executes a string of Python code and returns a tuple indicating success or failure.

    Args:
        code_string: The Python code to execute.

    Returns:
        A tuple (success, error_message).
        If syntax is invalid or an exception occurs during execution, success is False and error_message is provided.
        Otherwise, success is True and error_message is None.
    """
    syntax_ok, error_message = check_syntax(code_string)
    if not syntax_ok:
        return (False, error_message)

    try:
        exec(code_string)
        return (True, None)
    except Exception as e:
        return (False, str(e))

def example_function():
    """
    This is an example function.
    It currently does nothing.
    """
    pass

def main():
    """
    Parses command-line arguments, executes the provided code string, and prints the result.
    """
    parser = argparse.ArgumentParser(description="Execute a string of Python code and print the result.")
    parser.add_argument("code_string", help="The Python code string to execute.")
    args = parser.parse_args()

    code_string = args.code_string
    success, error_message = execute_code(code_string)

    if success:
        print("Code executed successfully.")
    else:
        print(f"Error: {error_message}")

if __name__ == "__main__":
    main()
