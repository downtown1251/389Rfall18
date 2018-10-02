section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rcx, rdx  ;moves the string length to rcx
        lea r12, [rdi]  ;moves the string pointer to a permanent register so that it may be recovered
        xor rax, rax  ;ensure return register is empty
        mov r11, 0

m_loop:

        mov [r12 + r11], rsi    ;copy the value over
        inc r11
        loop m_loop             ;repeat loop until rcx is 0


        leave                   ;moves down the stack pointer to the current base pointer,
                                ;and restores our saved base pointer, effectively
                                ;restoring our previous stack frame
        ret                     ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


        ;;;;;;;;;;;;;;;;;;;;;
        ;your code goes here!
        ;;;;;;;;;;;;;;;;;;;;;


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
