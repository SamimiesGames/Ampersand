BITS = 16

section _start
    mov 1, a


section .data
    fib_reset_a:
        pop
        mov c, a
        jmp fib
    fib:
        add a, b
        psh
        mov b, a
        pop
        mov c, b

        mov a, c
        psh
        mov a, 256
        sub a, b

        jnz fib_reset_a

