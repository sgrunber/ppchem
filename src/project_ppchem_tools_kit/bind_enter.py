from project_ppchem_tools_kit.process_input import process_input
window = None

def bind_enter(event):
    """Binds the Enter key to the process_input function.

    Args:
        event: The event that triggered the function.
    """
    try:
        if event.keysym == "Return":
            process_input()
    except Exception as e:
        print("Error while binding Enter key:", e)

if window:
    window.bind("<KeyPress>", bind_enter)