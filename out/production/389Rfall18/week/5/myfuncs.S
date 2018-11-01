section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        mov rax, rsi  ;copy over value to change chars to.
        mov rsi, rdi  ;copy over the string to rsi for stos


m_loop:

        movb            ;move a byte of the string over
        mov rcx, rax    ;change the bytes value to the correct character
        stosb           ;store the changed byte into the string
        inc r11         ;increment the loop counter
        cmp r11, rdx    ;compare to see if we are at the end of the loop
        jne m_loop      ;repeat loop if not at the end of the string.


        leave           ;moves down the stack pointer to the current base pointer,
                        ;and restores our saved base pointer, effectively
                        ;restoring our previous stack frame
        ret             ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame
        mov rcx, rdx  ;move the length to the counter registers
        rep movsb     ;repeat copying the values of source into destination

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
