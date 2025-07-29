import traceback

# TASK 1
try:

    with open('diary.txt', 'a') as diary_file:

        line = input("What happened today? ")
        diary_file.write(line + '\n')
        
        if line == "done for now":
            exit()
        
        while True:
            line = input("What else? ")
            diary_file.write(line + '\n')
            
            if line == "done for now":
                break
                
except Exception as e:
    print("An exception occurred.")
    print(f"Exception type: {type(e).__name__}")
    print(f"Exception message: {str(e)}")
    print("Traceback information:")
    traceback.print_exc()

