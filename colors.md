base03:    #002b36;
base02:    #073642;
base01:    #586e75;
base00:    #657b83;
base0:     #839496;
base1:     #93a1a1;
base2:     #eee8d5;
base3:     #fdf6e3;
yellow:    #b58900;
orange:    #cb4b16;
red:       #dc322f;
magenta:   #d33682;
violet:    #6c71c4;
blue:      #268bd2;
cyan:      #2aa198;
green:     #859900;

ACCENT:
#b58900 > instance?
#cb4b16 > include/import
#dc322f > support function, escape
#d33682 > TODO
#6c71c4 > md link, number
#268bd2 > variable, tag
#2aa198 > string
#859900 > punctuation.definition


LIGHT:
base3   > bg
base2   > highlights bg (current line, gutter)
base1   > comments
base0   > unused
base00  > default
base01  > emphasis
base02  > caret
base03  > unused

base2 50% opacity on top of base3: #f5efdc
base1 50% opacity on top of base2: #c0c4bb
red   33% opacity on top of background: #ec9489

DARK:
base03 bg
base02 highlight
base01 comments
base0  fg
base1  emphasis
base2  caret

base01 50% opacity on top of base03: #2C4C55
base01 50% opacity on top of base02: #c0c4bb
red    33% opacity on top of background: #6E2E32
