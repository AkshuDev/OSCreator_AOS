kernel_x80 = """; Entry point for the kernel
section .text
global _start

_start:
    ; Infinite loop to halt execution
    hang:
        jmp hang"""

bootloader_x80 = """; Bootloader code
[BITS 16]            ; 16-bit mode

section .text
    global _start

_start:
    ; Set up segments
    xor ax, ax       ; Clear ax register
    mov ds, ax       ; Set ds to 0
    mov es, ax       ; Set es to 0
    mov ss, ax       ; Set ss to 0
    mov sp, 0x7C00   ; Set stack pointer to 0x7C00

    ; Load kernel
    mov bx, KERNEL_LOAD_ADDR  ; Destination address for loading kernel
    mov dh, 0                 ; Head number (for floppy disks)
    mov dl, BOOT_DRIVE         ; Boot drive number (e.g., 0x80 for hard drive)

    mov cx, SECTORS_TO_LOAD   ; Number of sectors to load
    mov ax, 0x0201            ; Function 2 of INT 13h (read sectors)
    int 0x13                  ; Call BIOS interrupt for disk I/O

    ; Jump to kernel
    jmp KERNEL_LOAD_ADDR      ; Jump to loaded kernel code

; Constants
KERNEL_LOAD_ADDR   equ 0x1000        ; Address where kernel will be loaded
SECTORS_TO_LOAD    equ 1             ; Number of sectors to load
BOOT_DRIVE         equ 0x80          ; Boot drive (e.g., 0x80 for first hard drive)"""

IDT_x80 = """;; Set up Interrupt Descriptor Table (IDT)
section .data
    ; Define IDT for divide by zero error
    idt_entry_divide_error:
        ; Print an error message or handle the exception as needed
        mov eax, 0x02    ; BIOS video services function to set cursor position
        mov bh, 0x00     ; Page number (usually 0)
        mov dh, 0x0A     ; Row number
        mov dl, 0x00     ; Column number
        int 0x10         ; Call BIOS interrupt to set cursor position
        mov ah, 0x0E     ; BIOS video services function to print character
        mov al, 'D'      ; ASCII code for 'D'
        int 0x10         ; Call BIOS interrupt to print character
        ; You can add more error handling or halt the system if necessary
        jmp $            ; Infinite loop to halt execution

    ; Define IDT entry for keyboard interrupt
    idt_entry_keyboard:
        isr_keyboard:
        ; Read the scancode from the keyboard controller (typically port 0x60)
        in al, 0x60
        ; Process the scancode (interpret key presses, handle special keys, etc.)
        ; Check if the scancode represents a key press (bit 7 set)
        test al, 0x80
        jnz key_release  ; If bit 7 is set, it's a key release event
        ; Acknowledge the interrupt by sending an End Of Interrupt (EOI) signal to the PIC
        mov al, 0x20      ; Command to send EOI signal to PIC
        out 0x20, al      ; Send EOI signal to PIC
        iret              ; Return from interrupt

    ;; Define IDT for Timer
    isr_timer:
    ; Perform any necessary actions (e.g., scheduling tasks, updating system time)
    ; Your code here...
    ; Acknowledge the interrupt by sending an End Of Interrupt (EOI) signal to the PIC
    mov al, 0x20      ; Command to send EOI signal to PIC
    out 0x20, al      ; Send EOI signal to PIC
    iret              ; Return from interrupt

section .text
    global _start

_start:
    ; Initialize IDT
    mov edx, idt_table
    lidt [edx]

    ; Enable interrupts
    sti

    ; Enter infinite loop to halt execution
    hang:
        jmp hang

idt_table:
    dw idt_end - idt_start - 1 ; IDT limit
    dd idt_start               ; IST base addr

idt_start:
    w idt_entry_divide_error   ; Divide by zero error (INT 0)
    dw 0                        ; Unused
    dw 0                        ; Unused
    dw idt_entry_keyboard       ; Keyboard interrupt (INT 9)
    dw 0                        ; Unused
    dw idt_entry_timer          ; Timer interrupt (INT 8)
    ; Add more IDT entries as needed..."""