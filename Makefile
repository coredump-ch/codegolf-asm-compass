all: main

main.o: main.s
	nasm -f elf32 main.s

main: main.o
	ld -m elf_i386 -s -o main main.o

debug.o: main.s
	nasm -f elf32 -g main.s

debug: debug.o
	ld -m elf_i386 -o debug main.o

.PHONY: clean

clean:
	rm -f main.o main debug.o debug
