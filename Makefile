all: main

main.o: main.s
	nasm -f elf32 -O0 main.s

main: main.o
	ld -m elf_i386 -s -O0 -o main main.o

debug.o: main.s
	nasm -f elf32 -g -O0 main.s

debug: debug.o
	ld -m elf_i386 -O0 -o debug main.o

.PHONY: clean

clean:
	rm -f main.o main debug.o debug
