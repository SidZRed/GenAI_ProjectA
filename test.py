def code_execute(file_path):
    ctr = 0
    try:
        with open(file_path, 'r') as file:
            code = file.read()
            compiled_code = compile(code, file_path, 'exec')
            exec(compiled_code)
        print(f"Execution of '{file_path}' succeeded.")
        ctr += 1
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except SyntaxError as se:
        print(f"SyntaxError in '{file_path}': {se}")
    except NameError as ne:
        print(f"NameError in '{file_path}': {ne}")
    except Exception as e:
        print(f"Error executing the file: {e}")
    # TODO : Add more exceptions

    if ctr == 1:
        print("This code generation is valid.")
        # TODO : Add this file name to the list of valid files
    return ctr


if __name__ == "__main__":
    file_to_execute = r"C:\Users\rolla\OneDrive\Desktop\GenAI_ProjectA\prog1.py"
    print(code_execute(file_to_execute))
