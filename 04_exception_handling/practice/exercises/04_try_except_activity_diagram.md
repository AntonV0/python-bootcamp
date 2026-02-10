# UML Activity Diagram For A ...except...else...finally Block
```text

                   Start
                     |
                     |
                `try` block
                 (run code)
                     |
                     |
           Any exceptions raised?
           |                     |
           |                     |
          Yes                    No
      Success Case          Failure Case
     (no exception)      (exception caught)
           |                     |                    
           |                     |
      `else` block        `except` block          
           |                     |
           |                     |
           \                     /
            \                   /
             \                 /
              \               /
               `finally` block
              (always executed)
                      |
                      |
                     End