# Intel x86 ASM Codegolf

Write an Intel x86 assembly program that -- when compiled with the
provided Makefile -- returns an ASCII compass.

The goal is to minimize the binary size.

## Expected output

The template for the output is provided in `compass.txt`. The program is passed
a digit (ASCII) between 0 and 7. The numbers stand for directions:

- 0: North
- 1: Northeast
- 2: East
- 3: Southeast
- 4: South
- 5: Southwest
- 6: West
- 7: Northwest

The expected output for all those directions can be found in `expected.txt`.

Example:

    $ ./main 3
       _N_
      /   \
    W|  .  |E
     |   \ |
      \_ _/
        S

## Constraints

- The code needs to be written in 32 bit Intel (x86) assembly (NASM syntax).
- No library calls are allowed, use syscalls instead

## Hall of Fame

Sorted by binary size (in bytes).

We used to have a website with an auto-verifier, but it's been offline for a
few years now. If you have a working solution, send the assembly file and your
nickname to danilo@coredump.ch and I'll add you to the highscore list!

- ken & tbrunner: 292 bytes (2015-04-20)
- tbrunner: 328 (2015-04-20)
- schmijos & rnestler: 336 (2014-10-11)
- schmijos: 372 (2014-08-11)
- rnestler: 396 (2014-09-29)
- Danilo: 436 (2014-10-09)
- Danilo & Chrigi: 452 (2014-07-25)
- Stéphane: 536 (2016-08-17)
- maccesch: 644 (2015-07-27)
- Matthias: 712 (2016-08-10)
- rruettimann: 732 (2015-08-17)
- macav: 752 (2016-02-22)
- tobias: 768 (2016-02-02)
- shuber: 820 (2015-07-10)
- chuvisco88: 820 (2016-09-22)
- Ali @renuo: 824 (2015-06-24)

## Verification

Build the binary using `Make`.

    $ make
    nasm -f elf32 -O0 main.s
    ld -m elf_i386 -s -O0 -o main main.o

Run the test script with Python 3:

    $ python3 test.py
    Success!
    Binary size is 460 bytes.

## Debugging

If you want a binary with debug symbols included, use the `debug` Make target:

    $ make debug
    nasm -f elf32 -g -O0 main.s
    ld -m elf_i386 -O0 -o debug main.o
    $ gdb ./debug
    (gdb) ...

## Docker

You can also verify the code within an isolated
[Docker](http://www.docker.com/) instance.

    $ docker build -t codegolf .
    ...
    $ export SRC=/path/to/source/dir
    $ export FILE=filename.s
    $ docker run --rm \
      -v $SRC:/code \
      -u compass -w /home/compass/codegolf \
      codegolf \
      /bin/bash -c "cp /code/$FILE main.s && make && python test.py"
