import os
import time

frames = [
    """
    starting
    [░░░░░░░░░░] 0%
    """,
    """
    loading
    [████░░░░░░] 50%
    """,
    """
    loading
    [███████░░░] 75%
    """,
    """
    complete
    [██████████] 100%
    """
]

for i in range(len(frames)):
    os.system ('cls' if os.name == 'nt' else 'clear' )
    print(frames[i])
    time.sleep(2) 
