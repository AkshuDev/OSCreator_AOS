gcc -c -o "C:\Dev-Cpp\OS Creator\templates\C\kernel.o" "C:\Dev-Cpp\OS Creator\templates\C\kernel.c" 
nasm -f win32 -o "C:\Dev-Cpp\OS Creator\templates\C\asmkernel.o" "C:\Dev-Cpp\OS Creator\templates\C\kernel.asm"
ld -o "C:\Dev-Cpp\OS Creator\templates\C\kernel.bin" "C:\Dev-Cpp\OS Creator\templates\C\kernel.o" "C:\Dev-Cpp\OS Creator\templates\C\asmkernel.o" 

