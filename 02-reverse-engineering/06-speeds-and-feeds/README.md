# Reverse engineering: speeds and feeds

There is something on my shop network running at `nc mercury.picoctf.net 33596`, but I can't tell what it is. Can you?

## Solution

```bash
$ nc mercury.picoctf.net 33596
```

This produced a bunch of text.

```bash
$ nc mercury.picoctf.net 33596 > out.txt # ctrl+d after this
```

I looked at the produced text and noticed that each line started with the letter *G*. I did recall that 3D printers use G code and thought to myself, that the text may just be it. I searched for *gcode simulator* and found [this online tool]([g-code simulator](https://nraynaud.github.io/webgcode/)). I copy pasted the text into the tool and ran the simulation.

The flag was drawn. I simply wrote it into the answers window.


